import os
from pathlib import Path

from groq import Groq
from dotenv import load_dotenv

# Charge les variables d'environnement (.env)
load_dotenv()

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

def load_prompt() -> str:
    prompt_path = Path(__file__).parents[1] / "prompts" / "fix_prompt.txt"
    return prompt_path.read_text(encoding="utf-8")

def query_ai(code_content: str, traceback: str) -> str:
    """
    Envoie le code + traceback au modèle Groq et renvoie
    la réponse JSON sous forme de texte.
    """
    system_prompt = load_prompt()

    user_message = f"""
=== CODE PYTHON ===
{code_content}

=== TRACEBACK ===
{traceback}
"""

    completion = client.chat.completions.create(
        model="openai/gpt-oss-120b",   # modèle utilisé
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_message},
        ],
        temperature=0.1,
    )

    return completion.choices[0].message.content
