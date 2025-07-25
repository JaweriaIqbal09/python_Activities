from random import randint

def calc_digital_root(n):
    global steps
    steps = []  

    while len(n) > 1:
        count = 0
        for i in n:
            count += int(i)
        steps.append(f"{n} becomes {count}")
        n = str(count)
        
    return int(n)  

def printing_steps():
    for step in steps:
        print(step)

def sp_num(num):
    add = 0
    multiply = 1
    a = list(str(num))
    
    for numbers in a:
        add += int(numbers)
        multiply *= int(numbers)

    #slicing
    if str(num)==str(num)[::-1] or str(add) == str(multiply):
        return "y"
    else:
        return "n"

print("This Game has 3 Rounds\nAnd you have to guess the digital root of the given number in each round")
score = 0

for i in range(3):

    if i == 0:
        print("ROUND", i + 1, ":")
        x = str(randint(100, 199))
    elif i == 1:
        print("ROUND", i + 1, ":")
        x = str(randint(200, 299))
    elif i == 2:
        print("ROUND", i + 1, ":")
        x = str(randint(300, 399))

    z = int(input(f"Enter the digital root of {x}: "))
    y = calc_digital_root(x)

    if y == z:
        print("Good Job")
        print("You are Correct! +5 points")
        score += 5
    else:
        print("Wrong! The correct answer is:", y)
    print("Here's how it is done : ")
    printing_steps()

    ans = input(f"Is it a special number (y/n): ")
    b = sp_num(x)
    if ans.lower() == b:
        print("Good Job")
        print("You are Correct! +3 points")
        score += 3

print(f"Your total score is {score}/24")