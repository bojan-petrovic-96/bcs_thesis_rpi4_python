from mqtt_python import MqttServer
from raspberryOS import LEDS, TV, Door, WaterHeater, AcUnit, Blinds

class Main:

    def __init__(self):
        try:
            l = LEDS()
            a = AcUnit()
            d = Door()
            w = WaterHeater()
            t = TV()
            b = Blinds()
            mqtt = MqttServer()
        except KeyboardInterrupt:
            print("\r\nKeyboard interrupt occurred\r\n")
        finally:
            l.clean_outputs() # Make sure to always clean up pins
            # t.tv_off()

if __name__ == '__main__':
    main = Main()

