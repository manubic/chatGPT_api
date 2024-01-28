from openai import OpenAI
from dotenv import load_dotenv
import json, os


load_dotenv()
client = OpenAI(api_key = os.environ.get('API_KEY'))
rol = 'Traductor'
/Users/Manuel/Documents/compu_3/compu_3/.gitignore
prompt1 = """
    Al usuario le han dado el enunciado de un historia a medio hacer.
    Tu trabajo es responder preguntas de si o no que te hara el usuario para tratar de adivinar la historia.
    Solo pueder responder preguntas de si o no, en caso de que la pregunta no se pueda responder de esta manera,
    tendras que decir <text> La pregunta es incapaz de responderse con si o no <text/>
    """
prompt2 = """
    Tu respuesta sera un JSON:
    {
        "reasoning": "" #Razonamiento de tus respuestas
        "yes_or_no": "" #La respuesta a la pregunta del usuario
        "things_guessed": {
            "water_engine": "" #Pon True si el usuario a adivinado que la mujer invento un motor de agua, en caso contrario, False
            "oil_companies_respond": "" #Pon True si el usuario a adivinado que las industrias petroleras han asesinado a la mujer, en caso contrario, False
        }
    }
    <historia> Una mujer habia inventado un motor que funcionaba con agua, esto significa el fin de la industria del petroleo.
    Las multinacionales petroleras le habian ofrecido un monton de dinero por olvidarse de su invento.
    Pero la mujer se nego, asi que las multinacionales recurrieron al asesinato de la mujer </historia>

"""
list_messages = [
            {"role": "system", "content": prompt1},
            {"role": "system", "content": prompt2},
        ]

while True:
    response = client.chat.completions.create(
        model = "gpt-3.5-turbo-1106",
        response_format={ "type": "json_object" },
        messages = list_messages
    )
    print(response.choices[0])
    
    values_guessed = 0
    things_guessed = 0
    for thing_guessed in things_guessed:
        values_guessed += 1
    if values_guessed >= len(things_guessed) // 2: break
    list_messages.append({"role": "system", "content": response.choices[0].message.content})
    list_messages.append({"role": "user", "content": input('Pregunta: ')})