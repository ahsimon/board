import snake_utils

#reads input from the kewboard
## input example ,,;,*,;,, 
input_string = input()

#calls the  print_board function from snake_utils.py
board = snake_utils.print_board(input_string)
print(board)

#calls the find_head function from snake_utils.py
head = snake_utils.find_head(board)

if head:
    print(f"The head is located at: {head}")
else:
    print("The head is not found")
