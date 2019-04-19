def resultCheck(user_answer, correct_answer):
    correct_result = 0
    wrong_result = 0
    for i in range(len(user_answer)):
        for j in range(len(user_answer)):
            if float(user_answer[i][j]) == correct_answer[i][j]:
                correct_result += 1
            else:
                wrong_result += 1
    return correct_result, wrong_result