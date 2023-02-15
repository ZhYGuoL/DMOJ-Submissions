instructions = input()

letters = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'W', 'X', 'Y', 'Z')
numbers = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0')
string = ''

for idx in range(len(instructions)):
    if instructions[idx] in letters:
        if len(string) == 0:
            string += instructions[idx]
        elif string[-1] in numbers:
            print(string)
            string = instructions[idx]
        else:
            string += instructions[idx]
    elif instructions[idx] == '+':
        string += ' tighten '
    elif instructions[idx] == '-':
        string += ' loosen '
    elif instructions[idx] in numbers:
        string += instructions[idx]
print(string)