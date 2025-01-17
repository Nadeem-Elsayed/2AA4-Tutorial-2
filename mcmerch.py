import argparse

def main():
    #configure first cli arg to be price of item
    parser = argparse.ArgumentParser()
    parser.add_argument("price", type=float, help="the price of the item")
    parser.add_argument("--province", type = str, default="Ontario", choices=["Ontario", "Quebec"], help="The province where the tax is applied, default is ontario")
    
    args = parser.parse_args()

    if args.province == "Ontario":
        tax_rate = 1.13
    elif args.province == "Quebec":
        tax_rate = 1.14975
    
    price = args.price

    #add tax
    total = price*tax_rate

    print(f"The total price in {args.province} is {total: .2f}")
if __name__ == '__main__':
    main()