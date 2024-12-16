import RPi.GPIO as GPIO
import light_pins as light
import time
from rpi_lcd import LCD
import board
import adafruit_dht

lcd = LCD()
dht11_pin = adafruit_dht.DHT11(board.D10)


def ac_unit_get_temp():
    return dht11_pin.temperature


class AcUnit:
    def ac_unit_on(self):
        print("AC Unit on\r\n")
        temp = ac_unit_get_temp()
        if temp >= 28:
            print("Turning fan blade on\r\n")
            GPIO.output(light.AC_PIN, GPIO.HIGH)

    def ac_unit_off(self):
        print("AC Unit off\r\n")
        GPIO.output(light.AC_PIN, GPIO.LOW)

    def ac_unit_set_temp(self):
        print("Set temp\r\n")

    def __init__(self):
        print("\r\nAcUnit Init\r\n")
        GPIO.setup(light.AC_PIN, GPIO.OUT)


class LEDS:
    def set_outPins(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(light.WORK_SCENE_PIN, GPIO.OUT)
        GPIO.setup(light.MOVIE_SCENE_PIN, GPIO.OUT)
        GPIO.setup(light.LUNCH_SCENE_PIN, GPIO.OUT)
        GPIO.setup(light.NIGHT_SCENE_PIN, GPIO.OUT)

        GPIO.output(light.WORK_SCENE_PIN, GPIO.LOW)
        GPIO.output(light.LUNCH_SCENE_PIN, GPIO.LOW)
        GPIO.output(light.MOVIE_SCENE_PIN, GPIO.LOW)
        GPIO.output(light.NIGHT_SCENE_PIN, GPIO.LOW)

    def manage_lights(self, pin, level):
        return GPIO.output(self.pin, self.level)

    def clean_outputs(self):
        return GPIO.cleanup()

    def work_scene(self):
        GPIO.output(light.WORK_SCENE_PIN, GPIO.HIGH)

        GPIO.output(light.LUNCH_SCENE_PIN, GPIO.LOW)
        GPIO.output(light.MOVIE_SCENE_PIN, GPIO.LOW)
        GPIO.output(light.NIGHT_SCENE_PIN, GPIO.LOW)

    def lunch_scene(self):
        GPIO.output(light.WORK_SCENE_PIN, GPIO.LOW)
        GPIO.output(light.LUNCH_SCENE_PIN, GPIO.HIGH)
        GPIO.output(light.MOVIE_SCENE_PIN, GPIO.LOW)
        GPIO.output(light.NIGHT_SCENE_PIN, GPIO.LOW)

    def movie_scene(self):
        GPIO.output(light.WORK_SCENE_PIN, GPIO.LOW)
        GPIO.output(light.LUNCH_SCENE_PIN, GPIO.LOW)
        GPIO.output(light.MOVIE_SCENE_PIN, GPIO.HIGH)
        GPIO.output(light.NIGHT_SCENE_PIN, GPIO.LOW)

    def night_scene(self):
        GPIO.output(light.WORK_SCENE_PIN, GPIO.LOW)
        GPIO.output(light.LUNCH_SCENE_PIN, GPIO.LOW)
        GPIO.output(light.MOVIE_SCENE_PIN, GPIO.LOW)
        GPIO.output(light.NIGHT_SCENE_PIN, GPIO.HIGH)

    def turn_light_on(self):
        GPIO.output(light.WORK_SCENE_PIN, GPIO.HIGH)
        GPIO.output(light.LUNCH_SCENE_PIN, GPIO.HIGH)
        GPIO.output(light.MOVIE_SCENE_PIN, GPIO.HIGH)
        GPIO.output(light.NIGHT_SCENE_PIN, GPIO.HIGH)

    def turn_light_off(self):
        GPIO.output(light.WORK_SCENE_PIN, GPIO.LOW)
        GPIO.output(light.LUNCH_SCENE_PIN, GPIO.LOW)
        GPIO.output(light.MOVIE_SCENE_PIN, GPIO.LOW)
        GPIO.output(light.NIGHT_SCENE_PIN, GPIO.LOW)

    def __init__(self):
        self.set_outPins()
        print("LED Init\r\n")


class TV:
    def tv_on(self):
        print("TV is on\r\n")

    def tv_off(self):
        print("TV is off\r\n")
        lcd.clear()

    def tv_set_channel(channel):
        lcd.text(f"Channel: {channel}", 1)

    def tv_set_time(time):
        if int(time) == 0:
            lcd.text("Turn TV on 06:00", 2)
        elif int(time) == 1:
            lcd.text("Turn TV on 06:15", 2)
        elif int(time) == 2:
            lcd.text("Turn TV on 06:30", 2)
        elif int(time) == 3:
            lcd.text("Turn TV on 06:45", 2)
        elif int(time) == 4:
            lcd.text("Turn TV on 07:00", 2)
        elif int(time) == 5:
            lcd.text("Turn TV on 07:15", 2)
        elif int(time) == 6:
            lcd.text("Turn TV on 07:30", 2)

    def __init__(self):
        print("TV init\r\n")


class Door:
    def lock_door():
        print("Door is locked/unlocked\r\n")

    def open_door():
        print("Door is opened/closed\r\n")

    def __init__(self):
        print("Door init\r\n")


class WaterHeater:
    def water_heater_on(self):
        print("Water Heater turned on\r\n")

    def water_heater_off(self):
        print("Water Heater turned off\r\n")

    def water_heater_set_temp(temperature):
        print(f"Setting water heater temperature to: {temperature}")

    def __init__(self):
        print("Water Heater init\r\n")


class Blinds:
    def __init__(self):
        print("Blinds init\r\n")
