print('Welcome to the Quiz Game!')
score = 0

# Question 1
answer = input('What is the capital of Nepal? ')
if answer.lower() == 'kathmandu':
    print('Correct!')
    score += 1
else:
    print('Wrong! The correct answer is Kathmandu.')

# Question 2
answer = input('What is the largest planet in our solar system? ')
if answer.lower() == 'jupiter':
    print('Correct!')
    score += 1
else:
    print('Wrong! The correct answer is Jupiter.')

# Question 3
answer = input('Who wrote the play "Romeo and Juliet"? ')
if answer.lower() == 'william shakespeare':
    print('Correct!')
    score += 1
else:
    print('Wrong! The correct answer is William Shakespeare.')

# Question 4
answer = input('What is the chemical symbol for water? ')
if answer.lower() == 'h2o':
    print('Correct!')
    score += 1
else:
    print('Wrong! The correct answer is H2O.')

# Question 5
answer = input('What is the largest mammal in the world? ')
if answer.lower() == 'blue whale':
    print('Correct!')
    score += 1
else:
    print('Wrong! The correct answer is Blue Whale.')

print(f'Your total score is {score} out of 5.')
print(f'Your percentage score is {score / 5 * 100}%')
print('Thank you for playing the Quiz Game!')