from openai import OpenAI
import json



class Chat:
    def __init__(self, client: OpenAI, *prompts) -> None:
        self.client: OpenAI = client
        self.messages: list[dict] = []
        for prompt in prompts: self.messages.append({"role": "user", "content": prompt})
        response = self.client.chat.completions.create(
            model = "gpt-3.5-turbo-1106",
            response_format = {"type": "json_object" },
            messages = self.messages,
        )
        self.messages.append({"role": "system", "content": response.choices[0].message.content})

    def send_message(self, question: str) -> dict[str, str]:
        self.messages.append({"role": "user", "content": question})
        response = self.client.chat.completions.create(
            model = "gpt-3.5-turbo-1106",
            response_format = {"type": "json_object" },
            messages = self.messages,
        )
        self.messages.append({"role": "system", "content": response.choices[0].message.content})
        return json.loads(response.choices[0].message.content)