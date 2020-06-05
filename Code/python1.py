# INSTRUCTIONS

# In case it is not clear, the Question appears first, then examples, then any hints and finally the function that you need to complete appears underneath:

# <QUESTION>

# <EXAMPLES>

# <HINT>

# You are allowed access to the internet for this assessment, or you could use the DOCUMENTATION that comes bundled with your Python installation.  You should already be comfortable accessing this documentation, but to summarise:

# Access Python from you CLI

# Type help() or for example help(str)

# <QUESTION 1>

# Define a function that can accept two strings as input and returns the string with maximum length to the console.

# If two strings have the same length, then the function should return both strings separated by a " ".

# In this case, the strings should be returned in the same order in which they were given.

# <EXAMPLES>

# one("hi","hello") → "hello"
# one("three", "two") → "three"
# one("three", "hello") → "three hello"

# <HINT>

# What was the name of the function we have seen to check the length of a container?  Use your CLI to access the Python documentation and get help(len).


def one(input1, input2):
    if len(input1) > len(input2):
        return input1
    elif len(input2) > len(input1):
        return input2
    else:
        return input1 + " " + input2

    # <QUESTION 2>

    # Return the string that is between the first and last appearance of "bert" in the given string

    # Return the empty string "" if there is not 2 occurances of "bert"

    # IGNORE CASE

    # <EXAMPLES>

    # two("bertclivebert") → "clive"
    # two("xxbertfridgebertyy") → "fridge"
    # two("xxBertfridgebERtyy") → "fridge"
    # two("xxbertyy") → ""
    # two("xxbeRTyy") → ""

    # <HINT>

    # What was the name of the function we have seen to seperate a String? How can we make a string all upper or lower case?

    # Use your CLI to access the Python documentation and get help manipulating strings - help(str).


def two(input):
    lower = input.lower()
    split = lower.split("bert")
    if len(split) > 2:
        return split[int(len(split) / 2)]
    else:
        return ""

# <QUESTION 3>

# given a number
# if this number is divisible by 3 return "fizz"
# if this number is divisible by 5 return "buzz"
# if this number is divisible by both 3 and 5 return "fizzbuzz"
# if this number is not divisible by 3 or 5 return "null"

# <EXAMPLES>

# three(3) → "fizz"
# three(10) → "buzz"
# three(15) → "fizzbuzz"
# three(8) → "null"

# <HINT>

# No Hints for this question


def three(arg1):
    if arg1 % 3 == 0 and arg1 % 5 == 0:
        return "fizzbuzz"
    elif arg1 % 5 == 0:
        return "buzz"
    elif arg1 % 3 == 0:
        return "fizz"
    else:
        return "null"

    # <QUESTION 4>

    # Given a string seperate the string into the individual numbers present, then add each digit of each number to get a final value for each number

    # String example = "55 72 86"

    # "55" will = the integer 10
    # "72" will = the integer 9
    # "86" will = the integer 14

    # You then need to return the highest value, in the example above this would be 14.

    # <EXAMPLES>

    # four("55 72 86") → 14
    # four("15 72 80 164") → 11
    # four("555 72 86 45 10") → 15

    # <HINT>

    # help(int) for working with numbers and help(str) for working with Strings.


def four(arg1):

    split_string = arg1.split(" ")
    new_list = []

    for num in split_string:
        add_nums = 0
        for i in num:
            add_nums += int(i)
        new_list.append(add_nums)

    final_num = 0

    for i in new_list:
        if i > final_num:
            final_num = i
    return final_num

    # <QUESTION 5>

    # Given a large string that represents a csv, the structure of each record will be as follows:

    # owner,nameOfFile,encrypted?,fileSize

    # "Bert,helloWorld.py,True,1447,Bert,strings.py,False,1318,Jeff,dice.py,False,1445"

    # For each record, if it is not encrypted, return the names of the owners of the files in a String Array.
    # Do not include duplicate names.
    # If all records are encrypted, return an empty Array.

    # <EXAMPLES>

    # five("Jeff,random.py,False,1445") → ["Jeff"]
    # five("Bert,numberGen.py,True,1447,Bert,integers.py,True,1318,Jeff,floats.py,False,1445") → ["Jeff"]
    # five("Bert,boolean.py,False,1447,Bert,conditions.py,False,1318,Jeff,loops.py,False,1445") → ["Bert","Jeff"]
    # five("Bert,prime.py,True,1447,Bert,ISBN.py,False,1318,Jeff,OOP.py,False,1445") → ["Bert","Jeff"]

    # <HINT>

    # Dont't forget, False is a String, not a Boolean value in the Tests above.

    # help(str) and help(list), you might also need to use a function that can create a list of numbers for you, try help(range).


def five(input):
    split_list = input.split(",")

    owners_list = []
    for i in range(0, len(split_list) - 1):
        if split_list[i] == "False":
            owners_list.append(split_list[i - 2])
    owners_list = list(dict.fromkeys(owners_list))
    return owners_list

# <QUESTION 6>

    # There is a well known mnemonic which goes "I before E, except after C", which is used to determine which order "ei" or "ie" should be in a word.

    # Write a function which returns the boolean True if a string follows the mnemonic, and returns the boolean False if not.

    # <EXAMPLES>

    # six("ceiling") → True
    # six("believe") → True
    # six("glacier") → False
    # six("height") → False

    # <HINT>

    # Step through the logic here in order to solve the problem, you may find help(range) helpful.


def six(input):

    for i in range(0, len(input)-1):
        if input[i] == "i" and input[i - 1] == "e" and input[i-2] == "c":
            return True
        elif input[i] == "i" and input[i+1] == "e" and input[i-1] != "c":
            return True
        elif input[i] == "i" and input[i + 1] == "e" and input[i-1] == "c":
            return False
        elif input[i] == "i" and input[i - 1] == "e" and input[i - 1] != "c":
            return False

    # <QUESTION 7>

    # Write a function which returns the integer number of vowels in a given string.
    # You should ignore case.

    # <EXAMPLES>

    # seven("Hello") → 2
    # seven("hEelLoooO") → 6

    # <HINTS>

    # How do we ignore case in a String? help(str) may offer some insight.


def seven(input):
    count = 0
    for letter in input.upper():
        if letter == 'A' or letter == 'E' or letter == 'I' or letter == 'O' or letter == 'U':
            count += 1
    return count

    # <QUESTION 8>

    # Write a function which takes an input (between 1 and 10 inclusive) and multiplies it by all the numbers before it.
    # eg If the input is 4, the function calculates 4x3x2x1 = 24

    # <EXAMPLES>

    # eight(1) → 1
    # eight(4) → 24
    # eight(8) → 40320

    # <HINT>

    # You may need to create a list of numbers from 0 to i, take a look at help(range).


def eight(input):
    numbers_list = []
    count = 1
    for i in range(1, input + 1):
        numbers_list.append(i)
    numbers_list.reverse()
    for i in numbers_list:
        count *= i
    return count

    # <QUESTION 9>

    # Given a string and a char, returns the position in the String where the char first appears.
    # Ensure the positions are numbered correctly, please refer to the examples for guidance.
    # DO NOT ignore case
    # IGNORE whitespace
    # If the char does not occur, return the number -1.

    # <EXAMPLES>

    # nine("This is a Sentence","s") → 4
    # nine("This is a Sentence","S") → 8
    # nine("Fridge for sale","z") → -1

    # <HINT>

    # Take a look at the documentation for Strings, List and range.


def nine(inputString, char):
    string_upper = inputString.upper()
    char_upper = char.upper()
    print(char_upper)
    print(string_upper)
    count = 0
    for i in string_upper:
        if i == char_upper:
            count += 1
    return count

    # <QUESTION 10>

    # Given a string, int and a char, return a boolean value if the 'nth'
    # (represented by the int provided) char of the String supplied is the same as the char supplied.
    # The int provided will NOT always be less than than the length of the String.
    # IGNORE case and Whitespace.

    # <EXAMPLES>

    # ten("The",2,'h') → True
    # ten("AAbb",1,'b') → False
    # ten("Hi-There",10,'e') → False

    # <HINT>

    # How do we find the length of a container, take a look at help(len), you will also need to look at help(str) for String manipulation.


def ten(string, int, char):
    return False
