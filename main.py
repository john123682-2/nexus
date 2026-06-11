import requests
from ui.dashboard import show_dashboard

OWNER = "Harshil Goyal"


def get_models():
    try:
        response = requests.get(
            "http://localhost:11434/api/tags",
            timeout=5
        )

        return response.json()["models"]

    except:
        return []


def ask_ollama(model, prompt):

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": model,
            "system": """
You are NEXUS.

Rules:
- Always answer in English.
- Be helpful and concise.
- Never switch languages unless requested.
""",
            "prompt": prompt,
            "stream": False
        },
        timeout=300
    )

    return response.json()["response"]


# Detect Ollama Models

models = get_models()

if not models:

    print("\nERROR: Ollama not detected.")
    print("Make sure Ollama is running.\n")
    input("Press Enter...")
    exit()


# Model Selector

print("\nAvailable Models:\n")

for i, model in enumerate(models, start=1):

    print(f"[{i}] {model['name']}")

while True:

    try:

        choice = int(input("\nSelect Model: "))

        if 1 <= choice <= len(models):
            break

    except:
        pass

    print("Invalid selection.")


MODEL = models[choice - 1]["name"]


# Dashboard

show_dashboard(
    OWNER,
    MODEL
)


print("\nCommands:")
print("/model")
print("/help")
print("/exit")


# Main Chat Loop

while True:

    user = input("\nNEXUS ❯ ")

    if user.lower() == "/exit":

        print("\nShutting down NEXUS...\n")
        break

    elif user.lower() == "/model":

        print(f"\nCurrent Model: {MODEL}")
        continue

    elif user.lower() == "/help":

        print("""
Available Commands

/model   Show Current Model
/help    Show Commands
/exit    Exit NEXUS
""")
        continue

    try:

        print("\n[NEXUS THINKING...]\n")

        answer = ask_ollama(
            MODEL,
            user
        )

        print(answer)

    except Exception as e:

        print("\nERROR:")
        print(e)