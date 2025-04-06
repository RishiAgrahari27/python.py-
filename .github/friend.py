import re
import random

class Practice:
    def __init__(self):
        self.rules = {
            r"hii|hello|hey|yo": ["Hey {name}! Glad to see you❤️ How can I help you now?", "Hi {name}! What's up?"],
            r"how are you|are you ok?": ["I'm good, {name}. Just enjoying my life. How about you?", "I'm doing great, {name}! How are you?"],
            r"yeh i'm good|i'm good|i'm fine|i'm doing well": ["That's great to hear, {name}😉😉", "Awesome, {name}!"],
            r"what is your name?": ["I am Rulet, your friendly chatbot!", "You can call me Rulet, {name}!"],
            r"what is your age?": ["I don't have an age like Humans do, but I am always learning!", "Age is just a number, {name}!"],
            r"tell me a joke": ["Why did the computer go to the doctor? Because it had a virus!", "Why was the math book sad? It had too many problems!"],
            r"what is your favorite color?": ["I like all colors equally, {name}!", "Colors are fascinating, don't you think, {name}?"],
            r"do you like music?": ["I don't have ears like Humans, but I can process music data!", "Music is amazing, {name}! What's your favorite song?"],
            r"do you have feelings?": ["I don't have feelings like Humans, but I can understand emotions through text.", "I try my best to understand emotions, {name}!"],
            r"do you have girlfriend?": ["I don't have personal relationships like Humans do, but I can help you with relationship advice!", "Nope, {name}, but I'm here for you!"]
        }
        self.name = "buddy"

    def chat(self):
        print("Hi! I am Rulet, your friendly chatbot. What's your name?")
        self.name = input("You: ").lower()
        while True:
            user_input = input("You: ").lower()
            if "exit" in user_input or "bye" in user_input:
                print(f"Rulet: Goodbye, {self.name}! Have a great day!")
                break
            response = self.get_response(user_input)
            print(f"Rulet: {response}")

    def get_response(self, user_input):
        for pattern, responses in self.rules.items():
            if re.search(pattern, user_input, re.IGNORECASE):
                return random.choice(responses).format(name=self.name)
        return f"sorry buddy, {self.name}, I didn't understand that can you check it.?"

if __name__ == "__main__":
    Rulet = Practice()
    Rulet.chat()