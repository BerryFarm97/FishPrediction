import time

from predictor import run_prediction
from api_conditions import run_auto_prediction

def main():
    title = "fish bite predictor"
    options = [
        "Predict channel catfish bite manually",
        "Predict channel catfish bite automatically",
        "Exit"
    ]

    while True:
        print(title.title())

        for i, item in enumerate(options, start=1):
            print(f"{i}. {item}")
        try:
            choice = int(input("What would you like to do?: "))

            if choice == 1:
                run_prediction()
                return_to_menu()

            elif choice == 2:
                run_auto_prediction()
                return_to_menu()

            elif choice == 3:
                print("Thank you for using the fish predictor.\nEnjoy your trip!\U0001F3A3")
                time.sleep(1.25)
                break

            else:
                print("Invalid option. Please choose 1, 2, or 3")

        except ValueError:
            print("Invalid option. Please choose 1, 2, or 3")

def return_to_menu():
    time.sleep(5)
    print("Returning to main menu", end="")

    for _ in range(3):
        for dots in range(4):
            print(f"\rReturning to main menu{'.' * dots}", end="", flush=True)
            time.sleep(0.5)

    print("\n")

if __name__ == "__main__":
    main()