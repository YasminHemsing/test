import logging
import os
from pathlib import Path
from order import Order
from logging.config import fileConfig

os.chdir(Path(__file__).parent)

fileConfig("./config/logging.ini")


logger = logging.getLogger()

def main():
    logger.info("Miro App Started")
    order1 = Order()
    order1.order_start(print_receipt=True, save_receipt=True)


if __name__ == '__main__':
    main()





