# Day 28: CLI Calculator
# my first mini project - simple terminal operations calculator loop

def add(x, y): return x + y
def subtract(x, y): return x - y
def multiply(x, y): return x * y
def divide(x, y):
    if y == 0:
        return "Division by zero!"
    return x / y

def show_menu():
    print("\n--- Calculator ---")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

def run_calculator(mock_inputs=None):
    input_idx = 0
    
    def get_input(prompt):
        nonlocal input_idx
        if mock_inputs is not None:
            if input_idx < len(mock_inputs):
                val = mock_inputs[input_idx]
                input_idx += 1
                print(f"{prompt}{val}")
                return val
            return "5"
        return input(prompt)

    while True:
        show_menu()
        choice = get_input("Enter choice (1-5): ")
        
        if choice == '5':
            print("Exit calculator.")
            break
            
        if choice in ('1', '2', '3', '4'):
            try:
                num1 = float(get_input("First number: "))
                num2 = float(get_input("Second number: "))
            except ValueError:
                print("Bad numeric inputs!")
                continue
                
            if choice == '1':
                print("Result:", add(num1, num2))
            elif choice == '2':
                print("Result:", subtract(num1, num2))
            elif choice == '3':
                print("Result:", multiply(num1, num2))
            elif choice == '4':
                print("Result:", divide(num1, num2))
        else:
            print("Select a valid option!")

if __name__ == "__main__":
    # mock inputs for test verification run
    run_calculator(mock_inputs=['1', '10', '20', '5'])

# added division check and validation loop
