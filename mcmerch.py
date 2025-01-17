import argparse

def main():
    #configure first cli arg to be price of item
    parser = argparse.ArgumentParser()
    parser.add_argument("price", type=float, help="the price of the item")
    args = parser.parse_args()
    price = args.price

    #add tax
    total = price*1.13 #ontario

    print(f"The total price is {total: .2f}")
if __name__ == '__main__':
    main()