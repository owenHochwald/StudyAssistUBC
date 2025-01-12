from collections import deque
import aiohttp
import asyncio
import os

# Load environment variables
API_KEY = os.getenv('OPEN_ROUTER_KEY')
# for debugging
if not API_KEY:
    raise ValueError("OPEN_ROUTER_KEY not found in environment variables")

class OpenRouterChatApp:
    def __init__(self):
        self.session = None
        self.selected_model = "google/gemini-2.0-flash-exp:free"
        self.conversation_history = deque(maxlen=30)
        self.semaphore = asyncio.Semaphore(10)

    async def init_session(self):
        self.session = aiohttp.ClientSession()

    async def close_session(self):
        if self.session:
            await self.session.close()

    async def get_chat_completion(self, user_input):
        async with self.semaphore:
            self.add_to_conversation_history("user", user_input)
            api_url = "https://openrouter.ai/api/v1/chat/completions"
            headers = {
                "Authorization": f"Bearer {API_KEY}",
                "HTTP-Referer": "http://localhost:3000",  # Replace with your actual site URL
                "X-Title": "OpenRouter Chat App",  # Replace with your app name
            }
            data = {
                "model": self.selected_model,
                "messages": [{"role": msg["role"], "content": msg["content"]} 
                           for msg in self.conversation_history]
            }

            try:
                async with self.session.post(url=api_url, headers=headers, json=data) as response:
                    response.raise_for_status()
                    api_result = await response.json()
                    assistant_message = api_result["choices"][0]["message"]
                    self.add_to_conversation_history("assistant", assistant_message["content"])
                    return assistant_message
            except Exception as e:
                print(f"Error during API call: {str(e)}")
                return {"role": "assistant", "content": "Sorry, I encountered an error processing your request."}

    def add_to_conversation_history(self, role, content):
        message = {"role": role, "content": content}
        self.conversation_history.append(message)

    async def main(self):
        print("Welcome to the OpenRouter Chat App!")
        await self.init_session()

        try:
            while True:
                user_input = input("\nYou: ").strip()
                if not user_input:
                    continue
                    
                if user_input.lower() in ["exit", "quit"]:
                    print("Exiting the app. Goodbye!")
                    break

                print("Processing...")
                assistant_response = await self.get_chat_completion(user_input)
                print(f"\nAssistant: {assistant_response['content']}")

        except KeyboardInterrupt:
            print("\nUser interrupted. Exiting the app. Goodbye!")
        except Exception as e:
            print(f"\nAn error occurred: {str(e)}")
        finally:
            await self.close_session()

if __name__ == "__main__":
    asyncio.run(OpenRouterChatApp().main())