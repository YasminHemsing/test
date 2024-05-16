from menu import Menu
from customer import Customer

class Order:
    def __init__(self) -> None:
        self.customer = None
        self.list_of_wishes = []
        self.menu = None
        self.total = 0

    def order_start(self, print_receipt:bool = True, save_receipt: bool = False):
        # Cust info:
        self.customer = Customer()
        self.customer.get_user_information()

        # Show Menu
        self.menu = Menu()

        # Get User Wishes
        self.get_user_wishes()

        # receipt
        self.export_receipt(print_receipt, save_receipt)

    def get_user_wishes(self):
        print("Was möchten Sie bestellen?")
        print("=" * 29)

        while True:
            try:
                choice = int(input("Geben Sie die ID des Gerichts ein (0 zum Beenden): "))
            except ValueError:
                print("Bitte geben Sie eine gültige Zahl ein.")
                continue

            if choice == 0:
                break

            if choice not in self.menu.valid_id:
                print("Leider bieten wir das nicht an.")
                continue

            self.list_of_wishes.append(choice)

            more = input("Möchten Sie noch etwas bestellen? (ja/nein): ").strip().lower()
            if more != "ja":
                break

        self.list_of_wishes.sort()
        print("Ihre Bestellliste: ", self.list_of_wishes)
    def export_receipt(self, print_receipt:bool = True, save_receipt: bool = False):

        self.prepare_receipt_text()

        if print_receipt:
            self.print_receipt_text()

        if save_receipt:
            self.save_receipt_to_text()


    def prepare_receipt_text(self):
        self.receipt_text = ""
        self.receipt_text += f"Receipt: {self.customer.first_name} {self.customer.last_name}\n"
        self.receipt_text += "*" * 10 + "\n"

        for wish_id in self.list_of_wishes:
            for cat in self.menu.list_of_pizza:
                for dish in self.menu.list_of_pizza[cat]:
                    if dish["ID"] == wish_id:
                        self.receipt_text += f"{dish['title']} - {dish['price']}€\n"
                        self.total += dish['price']

        self.receipt_text += f"Die Summe beträgt: {self.total}€"

    def print_receipt_text(self):
        print(self.receipt_text)
        print("Vielen Dank für Ihren Besuch!")

    def save_receipt_to_text(self):
        with open("./receipt.txt", "w", encoding="UTF-8") as file:
            file.write(self.receipt_text)
