import ollama

class LocalLLM:
    """
    Local LLM (Large Language Model) wrapper using Ollama + Phi-3
    """

    def __init__(self, model: str = "phi3"):
        self.model = model

    def generate(self, prompt: str) -> str:
        response = ollama.chat(
            model=self.model,
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful AI voice assistant. Answer clearly and briefly."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response["message"]["content"].strip()
