from dotenv import load_dotenv
import os
from openai import OpenAI

# load .env file
load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

resp = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "Hello from CubLion Labs project!"}]
)

print(resp.choices[0].message.content)