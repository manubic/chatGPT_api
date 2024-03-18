from chat import Chat
from prompts import Prompts
import record_voice



class Game:
    def __init__(self, client) -> None:
        self.client = client
        self.prompts = Prompts()
        self.chat_yes_no: Chat = Chat(client, self.prompts.prompt_yes_no_1, self.prompts.prompt_yes_no_2)
        self.chat_achievements: Chat = Chat(client, self.prompts.prompt_achievements)

    def yes_or_no(self, json_response: dict) -> None:
        if json_response['yes_or_no'] == '': print("La pregunta no puede ser respondida con 'si' o 'no'") 
        else: print(json_response['yes_or_no'])

    def view_achievements(self, json_response: dict) -> bool:
        facts_achieved = 0
        for key in json_response:
            if key == "reasoning": continue
            if json_response[key]: facts_achieved += 1
        if facts_achieved >= len(json_response)-1: return True
        return False

    def start(self, story, audio):
        print(story[1])
        while True:
            if not audio:
                question = input('Pregunta: ')
            else:
                input('Pulsa enter para grabar')
                question = record_voice.grabar(self.client)
            print(question)
            self.yes_or_no(self.chat_yes_no.send_message(question))
            achievements = self.chat_achievements.send_message(question)
            print(achievements)
            if self.view_achievements(achievements): break

        print('Has adivinado la historia correctamente!!!')