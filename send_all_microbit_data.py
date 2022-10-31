from microbit import *

last0 = pin0.is_touched()
last1 = pin0.is_touched()
last2 = pin0.is_touched()

display.show(Image.HAPPY)
sleep(2000)
display.clear()

while True:
    acc = accelerometer

    ax, ay, az = acc.get_values()

    light_level = display.read_light_level()

    up = acc.is_gesture('up')
    down = acc.is_gesture('down')
    left = acc.is_gesture('left')
    right = acc.is_gesture('right')
    face_up = acc.is_gesture('face up')
    face_down = acc.is_gesture('face down')

    bA = button_a.is_pressed()
    bB = button_b.is_pressed()

    p0 = pin0.is_touched()
    p1 = pin1.is_touched()
    p2 = pin2.is_touched()

    if button_a.was_pressed():
        print('buttonA_was_pressed')
    if button_b.was_pressed():
        print('buttonB_was_pressed')
    if acc.was_gesture('shake'):
        print('shake')

    p0 = pin0.is_touched()
    if p0 != last0:
        if p0:
            print('pin0_was_touched')
        else:
            print('pin0_was_released')
        last0 = p0

    p1 = pin1.is_touched()
    if p1 != last1:
        if p1:
            print('pin1_was_touched')
        else:
            print('pin1_was_released')
        last1 = p1

    p2 = pin2.is_touched()
    if p2 != last2:
        if p2:
            print('pin2_was_touched')
        else:
            print('pin2_was_released')
        last2 = p2



    print(ax, ay, az,
    light_level,
    up, down, left, right, face_up, face_down,
    bA, bB,
    p0, p1, p2)

    sleep(10)