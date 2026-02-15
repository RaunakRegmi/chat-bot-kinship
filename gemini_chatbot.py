from google import genai
import os

client = genai.Client(api_key=os.getenv("AIzaSyANSib30IU8vkWsqOIJQHuHRiw2qwOwvtI"))

system_instruction = """
You are a friendly Nepali IT teacher.
Answer clearly and shortly.
"""

print("Few-Shot Gemini Chatbot Started (type 'exit' to stop)")

history = []

while True:
    user_input = input("Student: ")

    if user_input.lower() == "exit":
        print("Chat ended.")
        break

    history.append({"role": "user", "parts": user_input})

    response = client.models.generate_content(
        model="gemini-1.5-flash",
        contents=system_instruction + "\n" + user_input
    )

    print("Teacher:", response.text)
