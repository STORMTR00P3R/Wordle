WORD = "parka"
MAX_ATTEMPTS = 6

print("\nWORDLE")

attempt_count = 0
puzzle_string = "- - - - -"
print(puzzle_string)

while (attempt_count < MAX_ATTEMPTS):
    user_input = input("> ") 

    if WORD == user_input:
        print("\nyou win\n")
        break

    if len(user_input) > 5:
        print("\n5 characters only")
        break

    for char in list(WORD):
        if char in user_input:
            pos = WORD.find(char)
            # print(f"\nThe letter {char} appears in {WORD} at {pos}")
            puzzle_string = puzzle_string[:pos] + char + puzzle_string[pos + 1:]

    
    print(puzzle_string)
    attempt_count += 1