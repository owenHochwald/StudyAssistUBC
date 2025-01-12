from openai import OpenAI
import os
from dotenv import load_dotenv


# Load environment variables from .env file
load_dotenv()

# Get the OpenRouter API key
open_router_key = os.getenv('OPEN_ROUTER_KEY')


client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key=open_router_key,
)

completion = client.chat.completions.create(
  extra_headers={
    "HTTP-Referer": "<YOUR_SITE_URL>", # Optional. Site URL for rankings on openrouter.ai.
    "X-Title": "<YOUR_SITE_NAME>", # Optional. Site title for rankings on openrouter.ai.
  },
  model="microsoft/phi-3-medium-128k-instruct:free",
  messages=[
    {
      "role": "user",
      "content": "What is the meaning of life?"
    }
  ]
)
print(completion.choices[0].message.content)