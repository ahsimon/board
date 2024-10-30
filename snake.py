import snake_utils

#reads input from the kewboard
input_string = input()

#calls the board function from snake_utils.py
board = snake_utils.print_board(input_string)
print(board)

head = snake_utils.find_head(board)

if head:
    print(f"The head is located at: {head}")
else:
    print("The head is not found")