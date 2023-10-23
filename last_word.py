# Task 1 - Length of last word in string

def LengthOfLastWord(string):
    if len(string) > 104:
        return "Max length allowed is 104"
    elif string == "":
        return "No string found"
    return len(string.strip().split(" ")[-1])

# Test cases
test_1 = LengthOfLastWord("Hello World")
test_2 = LengthOfLastWord("   fly me   to   the moon  ")

print(test_1, test_2, sep="\n")