#!/usr/bin/env python3
"""
DECODELABS - PROJECT 1: RULE-BASED AI CHATBOT
Industrial Training Kit - Batch 2026

Architecture: IPO Model (Input → Process → Output)
Key Skills: Control Flow, Decision-Making Logic, Basic AI Concepts
Status: Foundation Phase (Logic Engine + Deterministic Guardrails)
"""

class RuleBasedChatbot:
    """
    A deterministic chatbot using rule-based logic.
    Zero hallucination risk. 100% hard-coded.
    """
    
    def __init__(self):
        """Initialize the chatbot with knowledge base and configuration."""
        # Knowledge Base: Intent → Response Dictionary
        self.responses = {
            # Greeting intents
            'hello': 'Hi there! How can I help you today?',
            'hi': 'Hello! Great to see you. What do you need?',
            'hey': 'Hey! What\'s on your mind?',
            'greetings': 'Greetings! I\'m here to assist.',
            'wassup': 'Wassup! What can I do for you?',
            
            # Inquiry intents
            'how are you': 'I\'m functioning at 100% capacity. How are you?',
            'how are you doing': 'All systems operational! Thanks for asking.',
            'what is your name': 'I\'m your AI Assistant. What\'s your name?',
            'who are you': 'I\'m a rule-based AI chatbot trained by DecodeLabs.',
            
            # Help intents
            'help': 'I can assist with greetings, answer basic questions, and provide information. Just ask away!',
            'what can you do': 'I can respond to greetings, answer questions about myself, and have a conversation with you.',
            'can you help me': 'Of course! What do you need help with?',
            
            # Gratitude intents
            'thank you': 'You\'re welcome! Happy to help.',
            'thanks': 'Anytime! Feel free to ask more.',
            'thank you so much': 'My pleasure! Anything else?',
            
            # Farewell intents
            'goodbye': 'Goodbye! Have a great day!',
            'bye': 'See you later! Take care!',
            'see you': 'Until next time!',
            'farewell': 'Farewell! Come back soon.',
            
            # Meta intents
            'what is your purpose': 'I\'m here to demonstrate rule-based AI logic and help you understand control flow.',
            'are you human': 'No, I\'m an AI—a deterministic decision-making system.',
            'are you real': 'I\'m as real as logic and rules make me.',
        }
        
        # System configuration
        self.exit_commands = ['exit', 'quit', 'bye', 'goodbye', 'see you', 'farewell']
        self.default_response = 'I do not understand. Could you rephrase that? (Type "help" for options.)'
        self.running = True
        
    def sanitize_input(self, raw_input):
        """
        PHASE 1: INPUT & SANITIZATION
        Convert to lowercase and strip whitespace.
        """
        return raw_input.lower().strip()
    
    def process_intent(self, clean_input):
        """
        PHASE 2: INTENT MATCHING & STATE MANAGEMENT
        Lookup user input in knowledge base.
        Use .get() for atomic lookup + fallback operation.
        """
        # Check for exit commands first
        if clean_input in self.exit_commands:
            self.running = False
            return 'Goodbye! Thanks for chatting. Keep learning! 🚀'
        
        # Atomic lookup with fallback
        response = self.responses.get(clean_input, self.default_response)
        return response
    
    def generate_response(self, response):
        """
        PHASE 3: OUTPUT & RESPONSE GENERATION
        Return processed response to user.
        """
        return response
    
    def run(self):
        """
        THE HEARTBEAT: INFINITE LOOP
        Continuous cycle until kill command.
        while True -> input -> process -> output -> break on exit
        """
        print("\n" + "="*60)
        print("DECODELABS RULE-BASED AI CHATBOT - PROJECT 1")
        print("="*60)
        print("Type 'help' to see what I can do.")
        print("Type 'exit' or 'quit' to leave.")
        print("="*60 + "\n")
        
        while self.running:
            try:
                # INPUT: Get user input
                raw_input = input("You: ").strip()
                
                # Validate input is not empty
                if not raw_input:
                    print("Bot: (Waiting for input...)\n")
                    continue
                
                # SANITIZATION: Clean the input
                clean_input = self.sanitize_input(raw_input)
                
                # PROCESS: Match intent and retrieve response
                response = self.process_intent(clean_input)
                
                # OUTPUT: Generate and display response
                bot_response = self.generate_response(response)
                print(f"Bot: {bot_response}\n")
                
            except KeyboardInterrupt:
                print("\n\nBot: Interrupted. Shutting down gracefully...\n")
                self.running = False
            except Exception as e:
                print(f"Bot: An error occurred: {e}\n")


def main():
    """
    Entry point: Instantiate and run the chatbot.
    """
    chatbot = RuleBasedChatbot()
    chatbot.run()
    print("="*60)
    print("Chatbot session ended. Thank you for using DecodeLabs AI!")
    print("="*60 + "\n")


if __name__ == "__main__":
    main()
