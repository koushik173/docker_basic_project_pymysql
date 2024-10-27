def store_name():
    name = input("Enter your name: ")
    if not name:
        print("Name cannot be empty.")
        return store_name()
    else:
        with open('all_name.txt','a') as f:
            f.write(name + ',')
            print(f"Your name '{name}' has been stored successfully.")

def display_name():
    try:
        with open('all_name.txt','r') as f:
            names = f.readlines()
            if names:
                print("\nStored names:")
                for name in names:
                    print(name.strip())
            else:
                print("No names stored yet.")
    except FileNotFoundError:
        print("No file found.")

if __name__ == '__main__':
    flag = True
    while flag:
        print("\nChoose an option:")
        print("1. Store name")
        print("2. Display stored names")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            store_name()
        elif choice == '2':
            display_name()
        elif choice == '3':
            flag = False
            print("Program Exit..")
            break
        else:
            print("Invalid choice. Please try again.")

    print("program Exit..")

