import re

def respond(message):
  # Remove punctuation and convert to lowercase
  message = re.sub(r'[^\w\s]', '', message).lower()
  
  # Check for greeting
  if message.startswith('hi') or message.startswith('hello'):
    return "Hello! How are you?"
  # Check for goodbye
  elif message.endswith('bye'):
    return "Goodbye! Have a great day."
  # Check for question
  elif message.endswith('?'):
    return "I'm not sure, can you elaborate?"
  # Otherwise, return a generic response
  else:
    return "I see. Tell me more."

print("Welcome to the chat AI!")
while True:
  message = input("You: ")
  if message.lower() == "exit":
    break
  response = respond(message)
  print("AI:", response)

