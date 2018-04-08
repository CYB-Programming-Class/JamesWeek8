import time
questions = {"have you ever used 'break' in any code ever?": "1. yes, 2. no"}

def question2():
    print("alright, you may continue")
    print("have you ever attempted a challenge, but abandoned it in frustration because it will never work")
    print("1. yes, or 2. no")
def validate(user_input):
    valid_answers = ["1", "2"]
    if user_input not in valid_answers:
        print("you are a failure")
        quit()
print("welcome to my coding purity test")
time.sleep(1)
print("with this test you will see how pure you are")
time.sleep(2)
print("let's begin")
time.sleep(1)
print(questions)
initial_purity_check = input(">>")
validate(initial_purity_check)
if initial_purity_check == "1":
    print("Alright")
    print("We are done here")
    print("the rest of the quiz is not necessary")
    print("you are 0% pure")
if initial_purity_check == "2":
    question2()
    second_question_input = input(">>")
    validate(second_question_input)
    if second_question_input == "1":
        print("rip, ur only 20% pure")
    if second_question_input == "2":
        print("alright, you may continue")
        print("have you ever used a while false loop?")
        print("1.yes, or 2. no")
        third = input(">>")
        validate(third)
        if third == "1":
            print("get out of here you 40% peasant")
        if third == "2":
            print("alright, you may continue")
            print("is there a difference between '=' and '=='?")
            print("1. no, or 2. yes")
            four = input(">>")
            validate(four)
            if four == "1":
                print("get out of here you 60% peasant")
            if four == "2":
                print("good job, you may continue")
                print("is a list editable?")
                print("1. yes, or 2. no")
                five = input(">>")
                validate(five)
                if five == "1":
                    print("get out of here you 80% peasant")
                if five == "2":
                    print("good job you 100% puritan")