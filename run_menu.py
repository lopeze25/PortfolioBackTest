
def run_volatility():
    pass

def run_macro():
    pass


def main():
    while True:
        print("\n=== Strategy Menu ===")
        print("1) Volatility Backtester ")
        print("2) SSO/ZROZ/Gold")
        print("q) Quit")
        choice = input("Choose an option: ").strip().lower()
        if choice == "1":
            run_volatility()
        elif choice == "2":
            run_macro()
        elif choice in ("q", "quit", "exit"):
            print("Goodbye.")
            break
        else:
            print("Invalid choice. Please try again.")


main()