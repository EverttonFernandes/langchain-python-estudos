import os

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

model_name = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")
model = ChatGoogleGenerativeAI(model=model_name, temperature=0.5)
message = model.invoke("Tell me hello world message in portuguese and spanish.")

print(message.content)
