from core.llm import OllamaClient

class NexusAgent:

    def __init__(self, model):
        self.llm = OllamaClient(model)

    def run(self, prompt):
        return self.llm.ask(prompt)