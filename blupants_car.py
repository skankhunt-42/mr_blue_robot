import rcpy
import rcpy.motor as motor
import rcpy.servo as servo
import rcpy.clock as clock
import rcpy.gpio as gpio
from rcpy.gpio import InputEvent
import Adafruit_BBIO.GPIO as GPIO

import time
import random

GPIO.cleanup()




#0
#unused
#1
#unused
#2
echo = "P9_23" #echo = "GPIO1_17" # resitor yellow
#3
trigger = "GPIO1_25"  # direct white
#4
vcc = "GP0_3v3"       # direct blue
#5
gnd = "GP0_GND"       # direct green


GPIO.cleanup()


#Configuration
print("trigger: [{}]".format(trigger))
GPIO.setup(trigger,GPIO.OUT) #Trigger
print("echo: [{}]".format(echo))
GPIO.setup(echo,GPIO.IN)  #Echo
GPIO.output(trigger, False)
print("Setup completed!")

#Security
GPIO.output(trigger, False)
time.sleep(0.5)
TRIG = trigger



#
#
#
# BLUE_GP01_17 = (1, 17)  # gpio1.17 P9.23
# BLUE_GP01_25 = (1, 25)  # gpio1.25 P2.23
#
# echo = gpio.Input(*BLUE_GP01_17)
# trigger = gpio.Output(*BLUE_GP01_25)
# pause_button = gpio.Input(*gpio.PAUSE_BTN)
#
# print("Press Pause")
# # if pause_button.low():
# #     print('Got <PAUSE>!')
#
#
# def pause_action(input, event):
#     if event == InputEvent.LOW:
#         print('<PAUSE> went LOW')
#     elif event == InputEvent.HIGH:
#         print('<PAUSE> went HIGH')
#
#
# pause_event = InputEvent(pause_button, InputEvent.LOW | InputEvent.HIGH, target=pause_action)
#
#
# global pulse
# global pulseStart
# global pulseEnd
# global distance
# pulse = 1
# pulseStart = 0
# pulseEnd = 0
# distance = -1
# def echo_action(input, event):
#     global pulse
#     global pulseStart
#     global pulseEnd
#     global distance
#     if pulse > 0:
#         pulseStart = time.time()
#     else:
#         pulseEnd = time.time()
#         pulseDuration = pulseEnd - pulseStart
#         distance = pulseDuration * 1715
#         distance = round(distance, 2)
#         #print("Distance: [{}]".format(distance))
#     pulse *= -1
#     # #if event == InputEvent.LOW:
#     # if event == InputEvent.HIGH:
#     #     pulse *= -1
#     #     pulseStart = time.time()
#     # #     print('ECHO went LOW')
#     # #elif event == InputEvent.HIGH:
#     # elif event == InputEvent.LOW:
#     #     pulse = 1
#     #     pulseEnd = time.time()
#     # #     print('ECHO went HIGH')
#     #     pulseDuration = pulseEnd - pulseStart
#     #     distance = pulseDuration / 100000000
#     #     distance = round(distance, 2)
#
#
# echo_event = InputEvent(echo, InputEvent.LOW | InputEvent.HIGH, target=echo_action)
#
#
#
#
# # try:
# #     if pause_button.low(timeout = 2000):
# #         print("pause_button")
# # except gpio.InputTimeout:
# #     print("Timeout")
#
# pause_event.start()
# echo_event.start()
#
# def read_distance():
#     global distance
#     distance = -1
#     counter = 0
#     while distance == -1:
#         trigger.set(rcpy.gpio.HIGH)
#         time.sleep(0.00001)
#         #time.sleep(0.001)
#         trigger.set(rcpy.gpio.LOW)
#         if counter > 1000:
#             distance = -2
#     return distance
#



#
# for i in range(0,10)
#     print(i)
#     trigger.set(rcpy.gpio.HIGH)
#     time.sleep(0.00001)
#     trigger.set(rcpy.gpio.LOW)
#     #time.sleep(0.00001)

# counter = 0
# while echo.is_low():
#     print(counter)
#     print("echo.is_low()")
#     trigger.set(rcpy.gpio.HIGH)
#     #time.sleep(0.00001)
#     time.sleep(2)
#     trigger.set(rcpy.gpio.LOW)
#     time.sleep(2)
#     pulseStart = time.time()
#     counter += 1
#     if counter > 10:
#         break
# while echo.is_high():
#     print("echo.is_high()")
#     #trigger.set(rcpy.gpio.HIGH)
#     time.sleep(0.00001)
#     trigger.set(rcpy.gpio.LOW)
#     pulseEnd = time.time()
#     if counter > 300:
#         break

# pause_event.stop()
# echo_event.stop()

duty = 0.3
interval = 2
period = 0.02

motor1 = motor.Motor(1)
motor2 = motor.Motor(2)

servo_hor = servo.Servo(1)
servo_vert = servo.Servo(2)
clckh = clock.Clock(servo_hor, period)
clckv = clock.Clock(servo_vert, period)

rcpy.set_state(rcpy.RUNNING)
# enable servos
servo.enable()

# start clock
clckh.start()
clckv.start()

# for i in range(0,5):
#     print(i)
#     print("HIGH")
#     trigger.set(rcpy.gpio.HIGH)
#     time.sleep(2)
#     print("LOW")
#     trigger.set(rcpy.gpio.LOW)
#     time.sleep(2)


def distanceMeasurement(TRIG,ECHO):
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)
    pulseStart = time.time()
    pulseEnd = time.time()
    counter = 0
    while GPIO.input(ECHO) == 0:
        pulseStart = time.time()
        counter += 1
    while GPIO.input(ECHO) == 1:
        pulseEnd = time.time()

    pulseDuration = pulseEnd - pulseStart
    distance = pulseDuration * 17150
    distance = round(distance, 2)
    return distance


def look_back():
    print("look_back()")
    servo_vert.set(-1.5)
    time.sleep(0.2)


def look_angle(angle=90):
    print("look_angle({})".format(angle))
    time.sleep(0.2)
    if angle > 0 and angle > 90:
        angle = 90
    if angle < 0 and angle < -90:
        angle = -90
    position = angle * 0.015
    servo_hor.set(position)
    servo_vert.set(0)
    time.sleep(0.2)

def say_yes():
    print("say_yes()")
    servo_vert.set(0)
    time.sleep(0.2)
    servo_vert.set(1.5)
    time.sleep(0.2)
    servo_vert.set(-1.5)
    time.sleep(0.2)
    servo_vert.set(1.5)
    time.sleep(0.2)
    servo_vert.set(0)
    time.sleep(0.2)


def say_no():
    print("say_no()")
    servo_vert.set(0)
    time.sleep(0.2)
    servo_hor.set(0)
    time.sleep(0.4)
    servo_hor.set(1.5)
    time.sleep(0.2)
    servo_hor.set(-1.4)
    time.sleep(0.4)
    servo_hor.set(0)
    time.sleep(0.2)


def move_block(blocks):
    d = duty
    if blocks < 0:
        d = d * -1
        blocks = blocks * -1

    motor1.set(d)
    motor2.set(d)

    time.sleep(interval * blocks)

    motor1.set(0)
    motor2.set(0)


def turn_right(angle=90):
    look_angle(angle* -1)
    print("turn_right()".format(angle))
    motor1.set(duty)
    time.sleep(0.0077777 * angle)
    motor1.set(0)


def turn_left(angle=90):
    look_angle(angle)
    print("turn_left({})".format(angle))
    motor2.set(duty)
    time.sleep(0.0077777 * angle)
    motor2.set(0)


def forward(blocks=1):
    print("forward({})".format(blocks))
    if blocks > 0:
        look_angle(0)
    else:
        look_back()
    return move_block(blocks)


def backward(blocks=1):
    print("backward({})".format(blocks))
    return forward(-blocks)


def random_move(force=False):
    rand = random.randint(0, 100)
    if force or rand < 25:
        rand = random.randint(15, 180)
        print("random_move({}) step1".format(str(rand)))
        look_back()
        left = bool(random.getrandbits(1))
        if left:
            turn_left(rand)
        else:
            turn_right(rand)
        backward()
        print("random_move({}) step2".format(str(rand)))
        left = not left
        if left:
            turn_left(rand)
        else:
            turn_right(rand)


def main():
    print("Init")

    recoveredDIstance = distanceMeasurement(trigger,echo)
    while True:
        if recoveredDIstance <= 0 or recoveredDIstance > 400:
            recoveredDIstance = 1.111
        while recoveredDIstance > 80.0:
            print("Distance: [{}] cm. Clear path!".format((str(recoveredDIstance))))
            say_yes()
            forward()
            time.sleep(1)
            recoveredDIstance = distanceMeasurement(trigger, echo)
            if recoveredDIstance <= 0 or recoveredDIstance > 400:
                recoveredDIstance = 1.111
            random_move()
        # Found obstacle
        print("Distance: [{}] cm. Dead end!".format(str(recoveredDIstance)))
        say_no()
        backward(0.5)
        #left = bool(random.getrandbits(1))
        rand = random.randint(0,100)
        print("rand: [{}]".format(str(rand)))
        if rand >= 0 and rand < 40:
            turn_left()
        if rand >= 40 and rand < 80:
            turn_right()
        if rand >= 80:
            random_move(force=True)
        recoveredDIstance = distanceMeasurement(trigger, echo)






    for i in range(0,5):
        d = distanceMeasurement(trigger, echo)
        print("Distance: [{}]".format(d))
        time.sleep(1)

    say_yes()
    time.sleep(1)
    say_no()


    forward()
    forward()
    forward()
    for i in range(0,5):
        d = distanceMeasurement(trigger, echo)
        print("Distance: [{}]".format(d))
        time.sleep(1)
    turn_left()
    forward()
    say_yes()
    time.sleep(1)
    say_no()
    turn_left()
    forward()
    forward()
    forward()
    for i in range(0,5):
        d = distanceMeasurement(trigger, echo)
        print("Distance: [{}]".format(d))
        time.sleep(1)
    turn_left()
    forward()
    turn_left()

    say_yes()

    #
    # say_yes()
    # time.sleep(1)
    # say_no()
    #
    # say_yes()
    # time.sleep(1)
    # say_no()

    # forward()
    # forward()
    # forward()
    # turn_left()
    # forward()
    # turn_left()
    # forward()
    # forward()
    # forward()
    # turn_left()
    # forward()
    # turn_left()


    # forward()
    # forward()
    # forward()
    # turn_right()
    # forward()
    # turn_right()
    # forward()
    # forward()
    # forward()
    # turn_right()
    # forward()
    # turn_right()


    # stop clock
    clckh.stop()
    clckv.stop()

    # disable servos
    servo.disable()
    print("Done")
