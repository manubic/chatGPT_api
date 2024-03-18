class Prompts:
    def __init__(self) -> None:
        self.prompt_yes_no_1 = """
            Al usuario le han dado el enunciado de un historia a medio terminar.
            Tu trabajo es responder preguntas de si o no que te hara el usuario para tratar de adivinar la historia.
            Solo pueder responder preguntas de si o no.
        """

        self.prompt_yes_no_2 = """
            Tu respuesta sera un JSON:
            {
                "reasoning": "" #Razonamiento de tus respuestas
                "reasoning_yes_or_no_question": # Razonamiento de porque la pregunta se puede responder con si o con no
                "yes_or_no": "" #La respuesta a la pregunta del usuario, no pongas nada si la pregunta del usuario no se puede responder con 'si' o 'no'
            }
            <historia>STORY</historia>
        """

        self.prompt_achievements = """
            Tendras que averiguar si las preguntas de un usuario han adivinado ciertos puntos de una historia
            Tu respuesta sera un JSON:
            {
                "reasoning": "" #Razonamiento de tus respuestas
                "water_engine": "" #Pon True si el usuario ha adivinado especificamente que la mujer sabe como construir un motor de agua, en caso contrario, False
                "oil_industries_threat": "" #Pon True si el usuario ha adivinado que la invencion era una amenaza para las industrias petroleras, en caso contrario, False
                "oil_industries_murder": "" #Pon True si el usuario ha adivinado que las industrias petroleras mataron a la mujer, en caso contrario, False
            }
            <historia>STORY</historia>
        """ 