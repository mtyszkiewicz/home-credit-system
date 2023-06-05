import paho.mqtt.publish as publish

publish.single(
    topic="notifications",
    payload="Nowa wiadomosc",
    qos=0,
    hostname="192.168.1.17",
    port=1883,
    client_id="backend-notify",
    auth={"username": "backend", "password": "Eb5578UNY"}
)
