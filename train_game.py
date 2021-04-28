import emoji
import random
import time
import sys

def get_emoji_list(list_of_cars):
    face_list = []
    for item in list_of_cars:
        if item == '1':
            face_list.append('\U0001F31E')
        else:
            face_list.append('\U0001F31A')
    return face_list

def show_train(faces):
    time.sleep(0.1)
    add_space = False
    for i in faces:
        if add_space:
            sys.stdout.write(' ' + i)
        else:
            sys.stdout.write(i)
            add_space = True
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\n')
    sys.stdout.flush()

def show_light_switch(train_list, pos):
    sys.stdout.write(
        ' '.join(get_emoji_list(train_list[:pos])) + ' \U0001F31E'
    )
    sys.stdout.flush()
    time.sleep(1)
    sys.stdout.write(
        '\r' + ' '.join(get_emoji_list(train_list[:pos + 1]))
    )
    sys.stdout.flush()
    time.sleep(0.5)
    sys.stdout.write('\n')
    sys.stdout.flush()

print(emoji.emojize("Hi! I'm Smith :smiling_face_with_sunglasses:"))
print("I'm trapted into the circle train")
print("I need to count train cars")
print("I can mark them only one way")
print("I can turn on or turn off the light")
train = (str(bin(random.randint(8, 1024)))[2:])
car_list = list(train)
random.shuffle(car_list)
count = len(train)
saved_car_list = car_list.copy()

time.sleep(2)
print('Now I come in the start train car')
if car_list[0] == 1:
    print('The light is on \U0001F31E')
    print('I go to the second train car')
else:
    car_list[0] = '1'
    print('The light is off \U0001F31A')
    print('I turn on the light')
    print('I go to the second train car')

time.sleep(2)

count_of_iter = 0
for index in range(1, count):
    count_of_iter += 1
    print('Now I am in ' + str(count_of_iter) + ' train car from the start')
    if car_list[index] == '1':
        print('The light is on')
    else:
        print('The light is off. I go to the next train car')
    show_train(get_emoji_list(car_list[:count_of_iter + 1]))
    if car_list[index] == '1':
        car_list[index] = '0'
        print(
            'I turn off the light and return ' +
            str(count_of_iter) +
            ' train cars back'
            )
        show_light_switch(get_emoji_list(car_list), count_of_iter)
        print('I returned to the start train car. The light is still on.')
        print("It means I didn't walk the full circle")
        print(
            "So I'll walk through " +
            str(count_of_iter) +
            " train cars again and search what is next")
    time.sleep(2)


    # print('Now I explored ' + str(count_of_iter) + ' train cars')
    # show_train(get_emoji_list(car_list[:count_of_iter + 1]))

print('Now I am in ' + str(count) + ' train car from the start')
print('The light is on')
print(
    'I turn off the light and return ' +
    str(count) +
    ' train cars back'
    )
print('I returned to the start train car. The light is off.')
print("So I walked the full circle")
print(
    "It means the train consists of " +
    str(count) +
    " train cars. I'm free!!! \U0001f604"
    )

print('====================================')
print('Train looked like this')
show_train(get_emoji_list(saved_car_list))

# print(emoji.emojize(':new_moon_face:') + emoji.emojize(':sun_with_face:'))
