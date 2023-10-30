questions = ('how many days are there in a week ?',
             'how many letters are there in english alphabet ?',
             'rainbow consist of how many colours ?',
             'how man days are there in a year ?')

options = (('A.8' ,'B.7' ,'C.5' ,'D.9'),
           ('A.26' ,'B.24' ,'C.25' ,'D.27'),
           ('A.5' ,'B.6' ,'C.7' ,'D.8'),
           ('A.362' ,'B.363' ,'C.364' ,'D.365'))

answers = ('B','A','C','D')
guesses = []
score = 0
question_num = 0

print('------QUIZ GAME------')
for question in questions:
    print('--------------------')
    print(question)

    for option in options[question_num]:
        print(option)

    guess = input('"A","B","C","D": ').upper()
    guesses.append(guess)
    if guess==answers[question_num]:
        score+=1
        print('CORRECT!')
    else:
        print('INCORRECT!')
        print('the correct answer is {}'.format(answers[question_num]))
    question_num += 1

print('---------------------')
print('        RESULT       ')
print('---------------------')

print('answers')
for answer in answers:
    print(answer, end=' ')
print()

print('guesses')
for guess in guesses:
    print(guess, end=' ')
print()

score=score/len(questions)*100
print('your score is',score,'%')