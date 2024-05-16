import logging
import json

logger = logging.getLogger()

class Menu:
    def __init__(self) -> None:
        self.list_of_pizza = None
        self.valid_id = []
        self.dish = None
        self.cat = None
        self.load_menu()
        self.show_menu()
    def load_menu(self):
        with open('./config/config.json', 'r', ) as file:
            self.list_of_pizza = json.load(file)

    def show_menu(self):
        print("Wilkommen bei Miro Restaurant")
        print("=" * 29)

        for self.cat in self.list_of_pizza:
            print(self.cat)
            print("=" * 8)

            for self.dish in self.list_of_pizza[self.cat]:
                self.dish_id = int(self.dish['ID'])
                self.dish_price = int(self.dish['price'])
                print(f"{self.cat} - {self.dish_id}. {self.dish['title']}\t{self.dish['price']}€")

                self.valid_id.append(self.dish_id)

            print()
        logger.info(f"Miro Menu {self.list_of_pizza} is created.")
        return self.valid_id

