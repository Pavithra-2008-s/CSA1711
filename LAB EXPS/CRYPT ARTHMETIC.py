from itertools import permutations

# INPUT first_word
word1 = input("Enter First Word  : ").upper()

# INPUT second_word
word2 = input("Enter Second Word : ").upper()

# INPUT result_word
result = input("Enter Result Word : ").upper()

# Find all unique letters
letters = ""

for ch in word1 + word2 + result:
    if ch not in letters:
        letters += ch

# IF length(letters) > 10
if len(letters) > 10:
    print("No Solution Possible")
    exit()

# Store first letter of each word
first_letters = [word1[0], word2[0], result[0]]

# FOR each possible digit assignment
for p in permutations(range(10), len(letters)):

    # Assign each letter a unique digit
    values = {}
    for i in range(len(letters)):
        values[letters[i]] = p[i]

    # Check if any first letter is assigned 0
    valid = True
    for ch in first_letters:
        if values[ch] == 0:
            valid = False
            break

    if not valid:
        continue

    # Convert first word into a number
    first_number = 0
    for ch in word1:
        first_number = first_number * 10 + values[ch]

    # Convert second word into a number
    second_number = 0
    for ch in word2:
        second_number = second_number * 10 + values[ch]

    # Convert result word into a number
    result_number = 0
    for ch in result:
        result_number = result_number * 10 + values[ch]

    # Check the equation
    if first_number + second_number == result_number:

        print("\nSolution Found\n")

        print(word1)
        print("+", word2)
        print("-" * len(result))
        print(result)

        print("\nLetter Assignments")
        for ch in letters:
            print(ch, "=", values[ch])

        print("\nAfter Substitution")
        print(first_number)
        print("+", second_number)
        print("-" * len(str(result_number)))
        print(result_number)

        print("\nVerification")
        print(first_number, "+", second_number, "=", result_number)

        break

else:
    print("No Solution Found")
 
