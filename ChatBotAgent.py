import re
from ResearchAgent import ResearchAgent
from random_responses import random_string, random_greetings

class ChatBotAgent:
    def __init__(self):
        # Initialize the research agent for data queries
        self.research_agent = ResearchAgent()

    #method to greet the user and display available help options    
    def greet_user(self):
        """Display welcome message and available help options"""
        print("=" * 55)
        print("🍵 Welcome to SmartCafe Assistant! 🍵")
        print("=" * 55)
        print("I'm here to help you with information about our cafe!")
        print("\nYou can ask me about:")
        print("🍽- Menu items and ingredients")
        print("💰- Prices of drinks")
        print("🥗- Nutritional information")
        print("🕒- Our opening hours")
        print("🥤- Available drinks")
        print("\nType 'exit' or 'quit' to end the conversation.")
        print("=" * 55)
    

        # method to count how many times patterns match in the user input
    def get_pattern_count(self, user_input_lower, patterns):
        """Count how many times patterns match in the user input"""
        count = 0
        for pattern in patterns:
            count += re.search(pattern, user_input_lower) is not None
        return count
    
    # method to detect user intent using regex patterns
    def detect_intent(self, user_input):
        """Use regex to detect user intent and route to appropriate response"""
        user_input_lower = user_input.lower()
        
        # Intent patterns using regex
        greeting_patterns = [r'\b(hello|hi|hey|greetings|how are you|how are you doing)\b']
        price_patterns = [
                            r'\b(price|cost|how much|expensive|amount|fee|pay|charge|what.*cost|what.*price|how.*much)\b',
                            r'\$[0-9]+(\.[0-9]+)?',
                            r'worth.*',
                            r'sell.*for.*',
                            r'can.*afford',
                            r'what do.*cost'
                        ]
        
        ingredient_patterns = [
                                r'\b(ingredient|ingredients|made of|contains|consists of|what.*in|what’s.*in|inside|composition)\b',
                                r'what.*made.*of',
                                r'what.*use.*to make',
                                r'what goes into',
                                r'how.*made'
                             ]
        
        nutrition_patterns = [
                                r'\b(calorie|calories|nutrition|nutrients|sugar|healthy|fat|health|diet|protein|carbs|energy)\b',
                                r'how many.*calories',
                                r'is.*healthy',
                                r'does it have.*sugar',
                                r'nutritional.*value',
                                r'nutrition.*info',
                                r'does.*contain.*fat'
                            ]
        
        hours_patterns = [
                            r'\b(hour|hours|open|close|time|when|schedule|timing|business hours|opening|closing)\b',
                            r'what time.*open',
                            r'what time.*close',
                            r'when.*open',
                            r'when.*close',
                            r'start.*time',
                            r'end.*time',
                            r'working.*hours',
                            r'daily.*timing',
                            r'available.*hours',
                            r'are you open.*(monday|tuesday|wednesday|thursday|friday|saturday|sunday)'
                        ]

        menu_patterns = [
                            r'\b(menu|drink|drinks|beverage|beverages|available|offer|options|selection|choices|list.*drinks)\b',
                            r'what.*(do you have|serve|sell|offer)',
                            r'show.*(menu|drinks|options)',
                            r'can i see.*menu',
                            r'do you have.*',
                            r'give me.*menu',
                            r'list.*(items|beverages|drinks)'
                        ]


       
        # Check for exit commands
        if re.search(r'\b(exit|quit)\b', user_input_lower):
            return 'exit'
        
        # Count occurrences of each intent pattern
        categories = {
            'price': self.get_pattern_count(user_input_lower, price_patterns),
            'ingredients': self.get_pattern_count(user_input_lower, ingredient_patterns),
            'nutrition': self.get_pattern_count(user_input_lower, nutrition_patterns),
            'hours': self.get_pattern_count(user_input_lower, hours_patterns),
            'menu': self.get_pattern_count(user_input_lower, menu_patterns),
            'greetings': self.get_pattern_count(user_input_lower, greeting_patterns)     
        }

        # Determine the intent with the highest count
        max_count = max(categories.values())
        if max_count == 0:
            return 'unknown'
        for key in categories:
            if categories[key] == max_count:
                return key
        return 'unknown'

    # method to route the user input to the appropriate ResearchAgent method based on intent with highest count
    def route_response(self, user_input, intent):
        """Route the user input to the appropriate ResearchAgent method based on intent"""
        try:
            if intent == 'price':
                return self.research_agent.get_price(user_input)
            elif intent == 'ingredients':
                return self.research_agent.get_ingredients(user_input)
            elif intent == 'nutrition':
                return self.research_agent.get_nutrition(user_input)
            elif intent == 'hours':
                return self.research_agent.get_hours(user_input)
            elif intent == 'menu':
                return self.research_agent.list_drinks()
            elif intent == 'greetings':
                return random_greetings()
            elif intent == 'unknown':
                return random_string()
            else:
                return "I'm not sure how to help with that. Please try rephrasing your question."
        except Exception as e:
            return f"Sorry, I encountered an error: {str(e)}"
    
    # method to start the conversation with the user
    def start_conversation(self):
        """Main conversation loop"""
        self.greet_user()

        # Start the main conversation loop
        while True:
            try:
                # Get user input
                user_input = input("\n🤔 You: ").strip()
                
                # Check if user wants to exit
                if not user_input:
                    print("🤖 Bot: Please type something or 'exit' to quit.")
                    continue
                
                # Detect intent using regex
                intent = self.detect_intent(user_input)
                
                # Handle exit
                if intent == 'exit':
                    print("🤖 Bot: Thank you for visiting SmartCafe! Have a great day! ☕")
                    break
                
                # Get response from research agent
                response = self.route_response(user_input, intent)
                print(f"🤖 Bot: {response}")
                
            except KeyboardInterrupt:
                print("\n🤖 Bot: Goodbye! Thanks for using SmartCafe Assistant! ☕")
                break
            except Exception as e:
                print(f"🤖 Bot: Sorry, something went wrong: {str(e)}")
