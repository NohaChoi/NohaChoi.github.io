class NumberCounter:
    def __init__(self):
        # Initialize counts for the numbers 1 through 5
        self.numbers = {
            "1": 0,
            "2": 0,
            "3": 0,
            "4": 0,
            "5": 0
        }

    def add_number(self, number):
        # Increment the count for the given number
        if number in self.numbers:
            self.numbers[number] += 1
            print(f"Added {number}. Current count: {self.numbers[number]}")
        else:
            print(f"{number} is not one of the tracked numbers.")

    def display_counts(self):
        # Display the counts for all numbers
        for number, count in self.numbers.items():
            print(f"{number}: {count}")


if __name__ == "__main__":
    counter = NumberCounter()

    while True:
        # Ask the user for a number
        number_input = input("Enter a number (1-5) or 'exit' to stop: ")

        # Exit the loop if the user types 'exit'
        if number_input == "exit":
            break

        # Add the number to the counter
        counter.add_number(number_input)

        # Display the current counts
        counter.display_counts()
