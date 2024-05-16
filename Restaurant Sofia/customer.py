import logging

logger = logging.getLogger()

class Customer:
    def __init__(self) -> None:
        self.first_name = ""
        self.last_name = ""

    def get_user_information(self):
        print("Get Guest Information")
        print("*" * 10)
        self.first_name = input("First Name: ").strip().title()
        self.last_name = input("Last Name: ").strip().title()
        logger.info(f"Customer: {self.first_name} {self.last_name} is created.")

    def __repr__(self) -> str:
        return f"Customer: {self.first_name} {self.last_name}"

