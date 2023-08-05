from project.client import Client
from project.meals.meal import Meal
from project.meals.starter import Starter
from project.meals.dessert import Dessert
from project.meals.main_dish import MainDish

class FoodOrdersApp:

    VALID_MEALS = {
        "MainDish": MainDish,
        "Dessert": Dessert,
        "Starter": Starter,
    }

    def __init__(self):
        self.menu = []
        self.client_list = []

    def register_client(self, client_phone_number: str):
        for client in self.client_list:
            if client.phone_number == client_phone_number:
                raise Exception("The client has already been registered!")
        client = Client(client_phone_number)
        self.client_list.append(client)
        return f"Client {client_phone_number} registered successfully."

    def add_meals_to_menu(self, *meals):
        for meal in meals:
            if meal.__class__.__name__ not in FoodOrdersApp.VALID_MEALS:
                continue
            else:
                self.menu.append(meal)

    def show_menu(self):
        result = []
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")
        else:
            meals = [m for m in self.menu]
            for meal in meals:
                result.append(meal.details())

        return "\n".join(result)

    def add_meals_to_shopping_cart(self, client_phone_number: str, ** meal_names_and_quantities):

        # TODO this method!!!!
        client = ''
        try:
            person = [c for c in self.client_list if c.client_phone_number == client_phone_number][0]
            client = person

        except IndexError:
            person = Client(client_phone_number)
            self.client_list.append(client)
            client = person

        if len(self.menu) < 5:
            client.shopping_cart = []
            client.bill = 0.0
            raise Exception("The menu is not ready")

        meals_to_order = []
        current_bill = 0

        for meal_name, meal_quantity in meal_names_and_quantities.items():
            for meal in self.menu:
                if meal.name == meal_name:
                    if meal.quantity >= meal_quantity:
                        meals_to_order.append(meal)
                        current_bill += meal.price * meal_quantity
                        break
                    else:
                        raise Exception(f"Not enough quantity of {type(meal).__name__}: {meal_name}!")
            else:
                raise Exception(f"{meal_name} is not on the menu!")

        client.shopping_cart.extend(meals_to_order)
        client.bill += current_bill

        for meal_name, meal_quantity in meal_names_and_quantities.items():
            if meal_name not in client.ordered_meals:
                client.ordered_meals[meal_name] = 0
            client.ordered_meals[meal_name] += meal_quantity
            for meal in self.menu:
                if meal.name == meal_name:
                    meal.quantity -= meal_quantity

        return f"Client {client_phone_number} " \
               f"successfully ordered {', '.join(meal.name for meal in client.shopping_cart)} " \
               f"for {client.bill:.2f}lv."

food_orders_app = FoodOrdersApp()
print(food_orders_app.register_client("0899999999"))
french_toast = Starter("French toast", 6.50, 5)
hummus_and_avocado_sandwich = Starter("Hummus and Avocado Sandwich", 7.90)
tortilla_with_beef_and_pork = MainDish("Tortilla with Beef and Pork", 12.50, 12)
risotto_with_wild_mushrooms = MainDish("Risotto with Wild Mushrooms", 15)
chocolate_cake_with_mascarpone = Dessert("Chocolate Cake with Mascarpone", 4.60, 17)
chocolate_and_violets = Dessert("Chocolate and Violets", 5.20)
print(food_orders_app.add_meals_to_menu(
    french_toast, hummus_and_avocado_sandwich,
    tortilla_with_beef_and_pork,
    risotto_with_wild_mushrooms,
    chocolate_cake_with_mascarpone,
    chocolate_and_violets))
print(food_orders_app.show_menu())
food = {"Hummus and Avocado Sandwich": 5,
        "Risotto with Wild Mushrooms": 1,
        "Chocolate and Violets": 4}
print(food_orders_app.add_meals_to_shopping_cart('0899999999', **food))









food_orders_app = FoodOrdersApp()
print(food_orders_app.register_client("0899999999"))
french_toast = Starter("French toast", 6.50, 5)
hummus_and_avocado_sandwich = Starter("Hummus and Avocado Sandwich", 7.90)
tortilla_with_beef_and_pork = MainDish("Tortilla with Beef and Pork", 12.50, 12)
risotto_with_wild_mushrooms = MainDish("Risotto with Wild Mushrooms", 15)
chocolate_cake_with_mascarpone = Dessert("Chocolate Cake with Mascarpone", 4.60, 17)
chocolate_and_violets = Dessert("Chocolate and Violets", 5.20)
print(food_orders_app.add_meals_to_menu(
    french_toast, hummus_and_avocado_sandwich,
    tortilla_with_beef_and_pork,
    risotto_with_wild_mushrooms,
    chocolate_cake_with_mascarpone,
    chocolate_and_violets))
print(food_orders_app.show_menu())
food = {"Hummus and Avocado Sandwich": 5,
        "Risotto with Wild Mushrooms": 1,
        "Chocolate and Violets": 4}









