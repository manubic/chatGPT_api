from openai import OpenAI
from dotenv import load_dotenv
import json, os


load_dotenv()
client = OpenAI(api_key = os.environ.get('API_KEY'))
rol = 'Traductor'
prompt1 = """
    Al usuario le han dado el enunciado de un historia a medio terminar.
    Tu trabajo es responder preguntas de si o no que te hara el usuario para tratar de adivinar la historia.
    Solo pueder responder preguntas de si o no.
"""

prompt2 = """
    Tu respuesta sera un JSON:
    {
        "reasoning": "" #Razonamiento de tus respuestas
        "reasoning_yes_or_no_question": # Razonamiento de porque la pregunta se puede responder con si o con no
        "yes_or_no": "" #La respuesta a la pregunta del usuario, no pongas nada si la pregunta del usuario no se puede responder con 'si' o 'no'
    }
    <historia> Una mujer habia inventado un motor que funcionaba con agua, esto significa el fin de la industria del petroleo.
    Las multinacionales petroleras le habian ofrecido un monton de dinero por olvidarse de su invento.
    Pero la mujer se nego, asi que las multinacionales recurrieron al asesinato de la mujer</historia>
"""
print("Bienvenido a las black stories")
list_messages = [
            {"role": "system", "content": prompt1},
            {"role": "system", "content": prompt2},
        ]
list_messages.append({"role": "user", "content": input('Pregunta: ')})
while True:
    response = client.chat.completions.create(
        model = "gpt-3.5-turbo-1106",
        response_format = {"type": "json_object" },
        messages = list_messages
    )
    json_response = json.loads(response.choices[0].message.content)
    print(json_response)
    if json_response['yes_or_no'] == '': print("La pregunta no puede ser respondida con 'si' o 'no'") 
    else: print(json_response['yes_or_no'])
    facts_guessed = 0
    # for fact in json_response['things_guessed'].values():
    #     if fact: facts_guessed += 1
    # if facts_guessed == 2: break
    list_messages.append({"role": "system", "content": response.choices[0].message.content})
    list_messages.append({"role": "user", "content": input('Pregunta: ')})
print('Has adivinado la historia correctamente!!!')