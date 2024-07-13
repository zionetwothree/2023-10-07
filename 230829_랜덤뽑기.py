import random

def choose_random_person(people_list):
    random_person = random.choice(people_list)
    return random_person

people = ["행운의 주인공"]
randomly_chosen_person = choose_random_person(people)
print("2학기 개강 이벤트\n축하합니다! 1등입니다! :", randomly_chosen_person)

