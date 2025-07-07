def chatbot_response(user_input):
    print(f"[DEBUG] Raw user input: {user_input}")
    user_input = user_input.lower()
    print(f"[DEBUG] Processed user input: {user_input}")

    if user_input in ["hi", "hello"]:
        print("[DEBUG] Greeting detected.")
        return "Hi there!"
    elif user_input in ["how are you", "how are you?"]:
        print("[DEBUG] Inquiry about well-being detected.")
        return "I'm fine, thanks! How can I help you?"
    elif user_input in ["bye", "goodbye"]:
        print("[DEBUG] Goodbye detected.")
        return "Goodbye! Have a nice day!"
    elif user_input in ["thanks", "thank you"]:
        print("[DEBUG] Thanks detected.")
        return "You're welcome!"
    else:
        print("[DEBUG] Unknown input.")
        return "I'm not sure how to respond to that."

# Main chatbot loop
print("🤖 Simple Chatbot (type 'bye' to exit)")
while True:
    user_message = input("You: ")
    reply = chatbot_response(user_message)
    print("Bot:", reply)

    if user_message.lower() in ["bye", "goodbye"]:
        print("[DEBUG] Exit condition met. Ending chat.")
        break
