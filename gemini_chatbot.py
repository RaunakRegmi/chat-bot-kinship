from google import genai
import os

client = genai.Client(
    api_key="AIzaSyB_Xn5rGszohpzfz6_q5jaNXnRRCOc3O38"
)

print("Gemini Chatbot Started (type 'exit' to stop)")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        break

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=user_input
    )

    print("Gemini:", response.text)
