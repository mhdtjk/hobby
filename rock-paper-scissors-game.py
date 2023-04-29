import inquirer
import random

possible_answer = ['Rock', 'Paper', 'Scissors']

questions = [
  inquirer.List('pick',
                message="What's your choose?",
                choices=possible_answer,
            ),
]

user_answer = inquirer.prompt(questions)["pick"]
user_answer_index = possible_answer.index(user_answer)

machine_answer = random.choice(possible_answer)
machine_answer_index = possible_answer.index(machine_answer)

def cal(user, machine):
    return (user % 3 - machine % 3 + 3) % 3

result = cal(user_answer_index, machine_answer_index)

if result == 0:
    print(user_answer, "\N{neutral face}", machine_answer)
elif result == 1:
    print(user_answer, "\N{slightly smiling face}", machine_answer)
else:
    print(user_answer, "\N{slightly frowning face}", machine_answer)


