from openai import OpenAI
from dotenv import load_dotenv
from chat import Chat
import os
import record_voice 


load_dotenv()
client = OpenAI(api_key = os.environ.get('API_KEY'))



def yes_or_no(json_response: dict):
    if json_response['yes_or_no'] == '': print("La pregunta no puede ser respondida con 'si' o 'no'") 
    else: print(json_response['yes_or_no'])

def view_achievements(json_response: dict):
    facts_achieved = 0
    for key in json_response:
        if key == "reasoning": continue
        if json_response[key]: facts_achieved += 1
    if facts_achieved >= len(json_response)-1: return True
    return False

def start(story, audio):
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
        <historia>STORY</historia>
    """.replace('STORY', story[2])

    prompt3 = """
        Tendras que averiguar si las preguntas de un usuario han adivinado ciertos puntos de una historia
        Tu respuesta sera un JSON:
        {
            "reasoning": "" #Razonamiento de tus respuestas
            "water_engine": "" #Pon True si el usuario ha adivinado especificamente que la mujer sabe como construir un motor de agua, en caso contrario, False
            "oil_industries_threat": "" #Pon True si el usuario ha adivinado que la invencion era una amenaza para las industrias petroleras, en caso contrario, False
            "oil_industries_murder": "" #Pon True si el usuario ha adivinado que las industrias petroleras mataron a la mujer, en caso contrario, False
        }
        <historia>STORY</historia>
    """.replace('STORY', story[2])
    
    
    chat_yes_no: Chat = Chat(client, prompt1, prompt2)
    chat_achievements: Chat = Chat(client, prompt3)
    print(story[1])
    while True:
        if audio == 'false':
            question = input('Pregunta: ')
        else:
            input('Pulsa enter para grabar')
            question = record_voice.grabar()
        print(question)
        yes_or_no(chat_yes_no.send_message(question))
        achievements = chat_achievements.send_message(question)
        print(achievements)
        if view_achievements(achievements): break

    print('Has adivinado la historia correctamente!!!')