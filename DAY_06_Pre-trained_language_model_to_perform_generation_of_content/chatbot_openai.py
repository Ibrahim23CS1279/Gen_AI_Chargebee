from openai import OpenAI

client = OpenAI(api_key="YOUR_GEMINI_API_KEY")

def start_chatbot():
    print("Ideaslabs chatbot, Type 'quit' to exit")

    while True:
        user_input = input("you: ")

        if user_input.lower() in ["quit", "exit"]:
            break

        response = client.responses.create(
            model="gpt-4.1-mini",
            input=user_input
        )

        reply = response.output[0].content[0].text
        print("Ideaslabs:", reply)

if __name__ == "__main__":
    start_chatbot()
