import RPi.GPIO as GPIO
import time


D = [24, 25, 8, 7, 12, 16, 20, 21]


def lightUp(ledNumber, period):
    GPIO.output(D[ledNumber], 1)
    time.sleep(period)
    GPIO.output(D[ledNumber], 0)


def blink(ledNumber, blinkCount, blinkPeriod):
    for _ in range(blinkCount):
        lightUp(ledNumber, blinkPeriod)
        time.sleep(blinkPeriod)


def runningLight(count, period):
    for _ in range(count):
        for i in range(8):
            lightUp(i, period)


def runningDark(count, period):
    for i in range(1, 8):
        GPIO.output(D[i], 1)
    for _ in range(count):
        for i in range(8):
            time.sleep(period)
            GPIO.output(D[i], 1)
            GPIO.output(D[(i + 1) % 8], 0)
    for i in range(1, 8):
        GPIO.output(D[i], 0)


def decToBinList(decNumber, left=False, right=False):
    binary_array = [0 for _ in range(8)]
    binary_string = bin(decNumber).lstrip('0b')
    for i in range(len(binary_string)):
        binary_array[i] = int(binary_string[len(binary_string) - 1 - i])
    return binary_array


def lightNumber(number, left=False, right=False):
    light = decToBinList(number)
    for i in range(len(light)):
        if light[i] == 1:
            GPIO.output(D[i], 1)
        else:
            GPIO.output(D[i], 0)


def runningPattern(pattern, direction, period=0.7):
    for _ in range(2):
        if direction:
            lightNumber(pattern)
            for i in range(7 + _ * 2):
                time.sleep(period)
                pattern = shift_left(pattern << 1)
                lightNumber(pattern)
        else:
            lightNumber(pattern)
            for i in range(7 + _ * 2):
                time.sleep(period)
                pattern = shift_right(pattern << 1)
                lightNumber(pattern)


def shift_right(number):
    return (number >> 2) + ((number % 4) << 6) 


def shift_left(number):
    return number % 256 + number // 256
    



GPIO.setmode(GPIO.BCM)
GPIO.setup(D, GPIO.OUT)
# GPIO.output(D[0], 1)
# time.sleep(1)
# GPIO.output(D[0], 0)
# lightUp(int(input()), float(input()))
# blink(int(input()), int(input()), float(input()))
# runningLight(int(input()), float(input()))
# runn
# ingDark(int(input()), float(input()))
# print(decToBinList(input()))
# lightNumber(int(input()))
runningPattern(int(input()), int(input()))
x = input()
for i in range(8):
    GPIO.output(D[i], 0)