import pyautogui as pt
from time import sleep
import pyperclip as pyp

#Helper function

def nav_to_image(image,clicks,off_x=0,off_y=0):
    position = pt.locateCenterOnScreen(image, confidence =.7)

    if position is None :
        print((f'{image} not found...'))
        return 0
    else:
        pt.moveTo(position, duration=.1)
        pt.moveRel(off_x,off_y,duration=.1)
        pt.click(clicks=clicks,interval=.3)



# Moves the Character
# v = attack
# c = place

def move_character(key_press, duration, action ='walking'):
    pt.keyDown(key_press)

    if action == "walking":
        print('walking')
    elif action == 'attack':
        pt.keyDown('v')

    sleep(duration)
    pt.keyUp('v')
    pt.keyUp(key_press)


def storage_to_learn():
    position_learn = pt.locateCenterOnScreen('Images/Bad_Damage.png', confidence=5)

    if position_learn is None:
        return False
    else:
        pt.keyDown('k',1)
        pt.keyDown('7',1)
        pt.keyDown('c',3)
        print('Took Damage!!')
        return True
def eat_food():
    position_food = pt.locateCenterOnScreen('Images/eat_food.png',confidence = 4)

    if position_food is None:
        return False
    else:
        pt.keyDown('3',1)
        pt.keyDown('c',3)
        pt.keyDown('5',1)
        return True
def locate_lava():
    position = pt.locateCenterOnScreen('Images/lava.png.png', confidence = .4)

    if position is None:
        return False
    else:
        move_character('s',2)
        print('Found Lava!!!!')
        return True



def chat():
    position = pt.locateCenterOnScreen('', confidence = 6)

    if position is None:
        return False

    else:
        storage_to_learn()
        decipher(latest_picture)
        pt.press('/',1)
        pt.write('responses')
        pt.press('enter',1)

sleep(3)
nav_to_image('Images/start_game.png', 3)

duration = 30
while duration != 0:
    if not locate_lava():
        move_character('w',2,'attack')
    else:
        break
    if storage_to_learn():
        break
    if eat_food():
        print('Ate food!!')


    duration -= 1
    print('Time remaining =',duration)