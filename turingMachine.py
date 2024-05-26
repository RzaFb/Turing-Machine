class TuringMachine:
    def __init__(self, tape):
        self.tape = tape
        self.head_position = 0
        self.state = 'q0'

        # Transitions dictionary representing the Turing machine's state transitions
        self.transitions = {
            'q0': {
                ' ': ('#', 'R', 'q1'),  # If current symbol is ' ', replace with '#' and move right to state q1
                '#': ('#', 'R', 'q0')  # If current symbol is '#', keep it and move right to state q0
            },
            'q1': {
                ' ': ('3', 'R', 'q2'),  # If current symbol is ' ', replace with '3' and move right to state q2
                '#': ('#', 'R', 'q1')  # If current symbol is '#', keep it and move right to state q1
            },
            'q2': {
                ' ': (' ', 'L', 'q3'),  # If current symbol is ' ', replace with ' ' and move left to state q3
                '#': ('#', 'R', 'q2')  # If current symbol is '#', keep it and move right to state q2
            },
            'q3': {
                ' ': (' ', 'L', 'q4'),  # If current symbol is ' ', replace with ' ' and move left to state q4
                '#': ('#', 'R', 'q5'),  # If current symbol is '#', keep it and move right to state q5
                '3': ('3', 'L', 'q3')  # If current symbol is '3', keep it and move left to state q3
            },
            'q4': {
                '3': ('3', 'L', 'q4'),  # If current symbol is '3', keep it and move left to state q4
                '#': ('#', 'R', 'q5')  # If current symbol is '#', keep it and move right to state q5
            },
            'q5': {
                '#': ('#', 'R', 'q6'),  # If current symbol is '#', keep it and move right to state q6
                '3': ('3', 'R', 'q5')  # If current symbol is '3', keep it and move right to state q5
            },
            'q6': {
                ' ': ('5', 'R', 'qf'),  # If current symbol is ' ', replace with '5' and move right to final state qf
                '#': ('#', 'R', 'q6')  # If current symbol is '#', keep it and move right to state q6
            }
        }

    def transition(self):
        while self.state != 'qf':  # Continue transitions until the final state qf is reached
            symbol = self.tape[self.head_position]
            if symbol in self.transitions[self.state]:
                # If current symbol and state have a defined transition,
                # update symbol, direction, and state based on the transition rules
                new_symbol, direction, new_state = self.transitions[self.state][symbol]
                self.tape[self.head_position] = new_symbol
                self.move_head(direction)
                self.state = new_state
            else:
                break  # If there is no defined transition, exit the loop

        return ''.join(self.tape)

    def move_head(self, direction):
        if direction == 'R':  # Move the head position to the right
            self.head_position += 1
            if self.head_position >= len(self.tape):
                self.tape.append(' ')  # If head goes beyond tape boundary, extend the tape with an empty symbol
        elif direction == 'L':  # Move the head position to the left
            self.head_position -= 1
            if self.head_position < 0:
                self.tape.insert(0, ' ')  # If head goes beyond tape boundary, extend the tape with an empty symbol


def calculate_factorial(n):
    if n == 0 or n == 1:
        return 1
    factorial = 1
    for i in range(2, n + 1):
        factorial *= i
    return factorial


if __name__ == "__main__":
    while True:
        try:
            input_number = int(input("Enter a positive integer (0 to exit): "))
            if input_number <= 0:
                print("Exiting the program...")
                break

            # Calculate the result (3 * n!) + 5
            factorial = calculate_factorial(input_number)
            result = (3 * factorial) + 5

            print(f"The result is: {result}")

            # Initialize the tape for the Turing machine
            tape = [' '] * (len(str(result)) + 2)
            tape[0] = ' '  # Start with an empty symbol at the beginning of the tape
            tape[-1] = ' '  # End with an empty symbol at the end of the tape

            # Create an instance of the TuringMachine class and perform the transition
            tm = TuringMachine(tape)
            tm_result = tm.transition()

            print(f"The Turing machine result is: {tm_result}")

        except ValueError:
            print("Invalid input! Please enter a positive integer.")
