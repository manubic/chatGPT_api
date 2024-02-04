import json


class Chat:
    def __init__(self, client, *prompts) -> None:
        self.client = client
        self.messages = []
        for prompt in prompts: self.messages.append({"role": "user", "content": prompt})
        response = self.client.chat.completions.create(
            model = "gpt-3.5-turbo-1106",
            response_format = {"type": "json_object" },
            messages = self.messages,
        )
        self.messages.append({"role": "system", "content": response.choices[0].message.content})

    def send_message(self, question) -> dict:
        self.messages.append({"role": "user", "content": question})
        
        response = self.client.chat.completions.create(
            model = "gpt-3.5-turbo-1106",
            response_format = {"type": "json_object" },
            messages = self.messages,
        )
        self.messages.append({"role": "system", "content": response.choices[0].message.content})
        return json.loads(response.choices[0].message.content)