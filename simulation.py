import argparse, time, json, random
from awscrt import io, mqtt
from awsiot import mqtt_connection_builder

# Set up CLI arguments
parser = argparse.ArgumentParser()
parser.add_argument('--endpoint', required=True)
parser.add_argument('--cert', required=True)
parser.add_argument('--key', required=True)
parser.add_argument('--root-ca', required=True)
parser.add_argument('--client-id', default="basicPubSub")
parser.add_argument('--topic', default="sdk/test/python")
args = parser.parse_args()

# AWS IoT MQTT setup
event_loop_group = io.EventLoopGroup(1)
host_resolver = io.DefaultHostResolver(event_loop_group)
client_bootstrap = io.ClientBootstrap(event_loop_group, host_resolver)

mqtt_connection = mqtt_connection_builder.mtls_from_path(
    endpoint=args.endpoint,
    cert_filepath=args.cert,
    pri_key_filepath=args.key,
    ca_filepath=args.root_ca,
    client_id=args.client_id,
    client_bootstrap=client_bootstrap,
    clean_session=False,
    keep_alive_secs=6
)

print(f"Connecting to {args.endpoint}...")
connect_future = mqtt_connection.connect()
connect_future.result()
print("Connected!")

# Simulación de datos
weight = round(random.uniform(0.5, 10.0), 2)  # kg
temperature = round(random.uniform(20.0, 80.0), 1)  # °C
vibration = round(random.uniform(0.1, 5.0), 2)  # m/s²

state = "OK" if weight < 5.0 else "ALERT"

message_dict = {
    "device": args.client_id,
    "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
    "sensors": {
        "weight_kg": weight,
        "temperature_c": temperature,
        "vibration_ms2": vibration
    },
    "machine_state": state
}

message_json = json.dumps(message_dict)

print(f"Publishing: {message_json}")
mqtt_connection.publish(topic=args.topic, payload=message_json, qos=mqtt.QoS.AT_LEAST_ONCE)

time.sleep(1)

mqtt_connection.disconnect().result()
print("Disconnected.")
