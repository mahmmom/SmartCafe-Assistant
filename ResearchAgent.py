import json
import re


class ResearchAgent():
    def __init__(self):
        with open("cafe_data.json") as f:
            self.data = json.load(f)

    # method to list available drinks
    def list_drinks(self):
        return "Here are the drinks we offer:\n- " + "\n- ".join(self.data["drinks"])
    
    # method to list opening hours
    def list_opening_hours(self):
        hours = []
        for day, time in self.data["opening_hours"].items():
            hours.append(f"{day}: {time}")
        return "\n".join(hours)

    # method to get the price of a drink
    def get_price(self, user_input):
        for drink in self.data["menu"]:
            if re.search(drink, user_input, re.IGNORECASE):
                return f"The price of {drink} is ${self.data['menu'][drink]['price_usd']:.2f}"
        return "I'm not sure which drink you're asking about."

    # method to get ingredients of a drink
    def get_ingredients(self, user_input):
        for drink in self.data["menu"]:
            if re.search(drink, user_input, re.IGNORECASE):
                ingredients = ", ".join(self.data["menu"][drink]["ingredients"])
                return f"The ingredients in {drink} are: {ingredients}."
        return "I'm not sure which drink you're asking about."
    
    # method to get nutrition facts of a drink
    def get_nutrition(self, user_input):
        for drink in self.data["menu"]:
            if re.search(drink, user_input, re.IGNORECASE):
                calories = self.data["menu"][drink]["nutrition"]["calories"]
                sugar_g = self.data["menu"][drink]["nutrition"]["sugar_g"]
                return f"The nutrition facts for {drink} are: {calories} calories, {sugar_g}g of sugar."
        return "I’m not sure which drink you're asking about."
    
    # method to get opening hours based on user input
    def get_hours(self, user_input):
        for day in self.data["opening_hours"]:
            if re.search(day, user_input, re.IGNORECASE):
                return f"Our hours on {day} are: {self.data['opening_hours'][day]}"
        return self.list_opening_hours()
    



