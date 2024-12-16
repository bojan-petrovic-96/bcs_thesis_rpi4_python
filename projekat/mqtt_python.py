import paho.mqtt.client as mqtt
import random
from raspberryOS import LEDS, TV, Door, WaterHeater, AcUnit
import light_pins as lights

# MQTT configuration
broker = "yourip"
port = 1 # your port
topic = [("/lights/setting/", 0), ("/ac/temp/", 0),
         ("/ac/unit/", 0), ("/blinds/pos/", 0),
         ("/tv/state/", 0), ("/tv/channel/", 0),
         ("/tv/time/", 0),
         ("/heater/temp/", 0),
         ("/heater/status/", 0),
         ("/door/open/", 0),
         ("/door/lock/", 0),
         ]

username = "yourusername"
password = "yourpassword"
client_id = f'python-mqtt-{random.randint(0, 1000)}'


class MqttServer:

    def default_func(state):
        print("Error")

    ac_unit_state_functions = {
        0: AcUnit.ac_unit_off,
        1: AcUnit.ac_unit_on
    }

    light_functions = {
        0: LEDS.turn_light_on,
        1: LEDS.turn_light_off,
        2: LEDS.work_scene,
        3: LEDS.lunch_scene,
        4: LEDS.movie_scene,
        5: LEDS.night_scene
    }

    tv_functions = {
        0: TV.tv_on,
        1: TV.tv_off
    }

    water_heater_funcions = {
        0: WaterHeater.water_heater_off,
        1: WaterHeater.water_heater_on
    }

    # establish the connection with MQTT broker
    def connect_to_broker() -> mqtt:
        def on_connect(client, userdata, flags, rc, properties):
            if rc == 0:
                print("Connected to broker\r\n")
            else:
                print(f"Failed to connect... response:{rc}\r\n")
        client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
        client.username_pw_set(username, password)
        client.on_connect = on_connect
        client.connect(broker, port)
        return client

    # subscribe to the MQTT topic

    def subscribe(client: mqtt):
        def on_message(client, userdata, msg):
            print(
                f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
            if msg.topic in topic[0]:
                lfunction = MqttServer.light_functions.get(
                    int(msg.payload.decode()), MqttServer.default_func)
                lfunction(1)
            elif msg.topic in topic[1]:
                print("Managing temperature")
            elif msg.topic in topic[2]:
                ac_function = MqttServer.ac_unit_state_functions.get(
                    int(msg.payload.decode()), MqttServer.default_func)
                ac_function(1)
            elif msg.topic in topic[3]:
                print("Blinds config")
            elif msg.topic in topic[4]:
                tv_function = MqttServer.tv_functions.get(
                    int(msg.payload.decode()), MqttServer.default_func)
                tv_function(1)
            elif msg.topic in topic[5]:
                TV.tv_set_channel(msg.payload.decode())
            elif msg.topic in topic[6]:
                TV.tv_set_time(msg.payload.decode())
            elif msg.topic in topic[7]:
                WaterHeater.water_heater_set_temp(msg.payload.decode())
            elif msg.topic in topic[8]:
                water_heater_funcion = MqttServer.water_heater_funcions.get(
                    int(msg.payload.decode()), MqttServer.default_func)
                water_heater_funcion(1)
            elif msg.topic in topic[9]:
                Door.open_door()
            elif msg.topic in topic[10]:
                Door.lock_door()

        client.subscribe(topic)
        client.on_message = on_message

    def run(self):
        client = MqttServer.connect_to_broker()
        MqttServer.subscribe(client)
        client.loop_forever()

    def __init__(self):
        print("MQTT Init\r\n")
        self.run()
