def km_to_m(km):
    return km * 1000
def mt_to_km(mt):
    return mt / 1000
def kg_to_g(kg):
    return kg * 1000
def g_to_kg(g):
    return g / 1000


while True:
    print("\n ---- Unit Converter ----")
    print("1. Kilometers to Meters")
    print("2. Meters to Kilometers")
    print("3. Kilograms to Grams")
    print("4. Grams to Kilograms")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        km=float(input("Enter kilometers: "))
        print("Meters: ",km_to_m(km))

    elif choice == "2":
        mt=float(input("Enter meters: "))
        print("Kilometers: ",mt_to_km(mt))

    elif choice == "3":
        kg=float(input("Enter kilometers: "))
        print("Grams: ",kg_to_g(kg))

    elif choice == "4":
        g=float(input("Enter grams: "))
        print("Kilograms: ",g_to_kg(g))

    elif choice == "5":
        print("Goodbye !")
        break
        
    else:
        print("Invalid choice")