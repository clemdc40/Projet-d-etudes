from fastapi import FastAPI
from google import genai

app = FastAPI()

# Instanciation du client avec ta clé API
client = genai.Client(api_key="AIzaSyCgaTTlv_BBLB3Zbb-0x9Ih7X5vr5fJYV4")

def get_gemini_response(prompt: str) -> str:
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt
    )
    return response.text

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/api/gemini")
def read_gemini(message: str = None):
    if message is None:
        message = get_gemini_response("Pour un pentest sur site web, quels sont les outils les plus utilisés ?")
    return {"message": message}
