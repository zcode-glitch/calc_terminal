print("=============================================")
print("=== Welcome In Calculator Terminal Python ===")
print("=============================================")

while True:
    angka1 = int(input("Input First Number: "))
    angka2 = int(input("Input Second Number: "))

    option = input("Choice Operator (+, -, *, /): ")

    if option == "+":
        print (angka1 + angka2)
    elif option == "-":
        print (angka1 + angka2)
    elif option == "*":
        print (angka1 + angka2)
    elif option == "/":
        print (angka1 + angka2)
    else :
        print("There is no such option!")

    option_confirm = input("do you want to stop? (y/n): ")
    if option_confirm == "y":
        print("Thank You Support This Github With Give Me Stars In This Repository")
        break