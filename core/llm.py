import requests

OLLAMA_URL = "http://localhost:11434/api/generate"

class OllamaClient:

    def __init__(self, model):
        self.model = model

    def ask(self, prompt):

        response = requests.post(
            OLLAMA_URL,
            json={
                "model": self.model,
                "system": """
You are NEXUS, an autonomous development agent.

Rules:
- Always respond in English.
- Be concise and helpful.
- Focus on coding, development and problem solving.
""",
                "prompt": prompt,
                "stream": False
            },
            timeout=300
        )

        return response.json()["response"]