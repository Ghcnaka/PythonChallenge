def verify(string):
    count = 0
    for index in string:
        if index == "?":
            count += 1
        if count > 3:
            break
    return count


def verify_interval(string):
    question = False
    if verify(string) == 3:
        question = True
    return question


def question_mark(string):
    first_num = -1
    second_num = -1
    count = -1
    first_index = 0
    boolean = True
    for index in string:
        count += 1
        if not boolean:
            break
        try:
            if first_num == -1:
                first_num = int(index)
                first_index = count + 1
            elif second_num == -1:
                second_num = int(index)
            if first_num + second_num >= 10:
                boolean = verify_interval(string[first_index:count])
                if not boolean:
                    break
            if second_num != -1:
                first_num = second_num
                second_num = -1
                first_index = count + 1
        except ValueError or TypeError:
            True

    return boolean


if question_mark(input()):
    print("OK")
else:
    print("not OK")