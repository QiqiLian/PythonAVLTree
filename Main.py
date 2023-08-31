from avltree import AVLTree


# Function to take integer input from the user
def get_integer_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter an integer.")

avl = AVLTree()
root = None

while True:
    print("\n1. Insert")
    print("2. Delete")
    print("3. Search")
    print("4. Print Tree")
    print("5. Exit")

    choice = get_integer_input("Select an option: ")

    if choice == 1:
        key = get_integer_input("Enter the key to insert: ")
        root = avl.insert(root, key)
        print("Key inserted successfully.")
    elif choice == 2:
        key = get_integer_input("Enter the key to delete: ")
        root = avl.delete(root, key)
        print("Key deleted successfully.")

    elif choice == 3:
        key = get_integer_input("Enter the key to search: ")
        result = avl.search(root, key)
        if result:
            print(f"{key} found in the AVL Tree.")
        else:
            print(f"{key} not found in the AVL Tree.")

    elif choice == 4:
        print("AVL Tree:")
        avl.printTree(root)

    elif choice == 5:
        print("Exiting...")
        break

    else:
        print("Invalid choice. Please select a valid option.")
