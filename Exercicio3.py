def verify(string):
    count = 0
    for index in string:
        if index == "?":
            count += 1
        if count > 3:
            break
    return count



def question_mark(string):
    question = False
    if verify(string) == 3:
        question = True
    return question

if question_mark(input()):
    print("OK")