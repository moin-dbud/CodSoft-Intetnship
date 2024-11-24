import re
import time

class RuleBasedChatbot:
    def __init__(self):
        """
        Initializes the chatbot with predefined rules and exit commands.
        """
        self.responses = {
            "product": "Our products are of top quality! You can explore more on our website: www.example.com/products.",
            "technical support": "For technical support, please visit www.example.com/support or call our helpline.",
            "return policy": "We offer a 30-day return policy. Ensure the product is in its original condition to be eligible for returns.",
            "help": "I'm here to assist you! Please let me know your specific query.",
            "exchange": "We have a return 7-days policy, the product should be in the original condition.",
        }
        self.exit_commands = ["quit", "pause", "exit", "goodbye", "bye", "farewell"]

    def display_message(self, message, delay=1):
        """
        Displays messages with an optional typing delay to simulate realism.
        """
        for char in message:
            print(char, end="", flush=True)
            time.sleep(0.02)
        print()
        time.sleep(delay)

    def greet(self):
        """
        Greets the user and starts the interaction.
        """
        self.display_message("Chatbot: Hello! Welcome to our customer support chat.")
        name = input("Chatbot: May I know your name? ").strip()
        self.display_message(f"Chatbot: Hi {name}! It's a pleasure to assist you.")
        self.display_message("Chatbot: You can ask me about our products, technical support, exchange, return policies, or general help.")

    def get_response(self, user_input):
        """
        Matches user input to predefined responses using rules.
        """
        user_input = user_input.lower()

        # Check for exit commands
        if any(command in user_input for command in self.exit_commands):
            return "Thanks for chatting with us! Have a great day!"

        # Match patterns or keywords
        if "product" in user_input:
            return self.responses["product"]
        elif "technical support" in user_input or re.search(r'technical.*support', user_input):
            return self.responses["technical support"]
        elif "return policy" in user_input or "return" in user_input:
            return self.responses["return policy"]
        elif "help" in user_input:
            return self.responses["help"]
        elif "exchange" in user_input:
            return self.responses["exchange"]

        # Default fallback response
        return "I'm sorry, I didn't quite understand that. Could you rephrase?"

    def chat(self):
        """
        Main conversation loop.
        """
        self.display_message("Chatbot: How can I assist you today?")
        while True:
            user_input = input("You: ").strip()
            response = self.get_response(user_input)
            self.display_message(f"Chatbot: {response}")
            if response == "Thanks for chatting with us! Have a great day!":
                break


# Main Program
if __name__ == "__main__":
    chatbot = RuleBasedChatbot()
    chatbot.greet()
    chatbot.chat()
