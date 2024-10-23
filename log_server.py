import paho.mqtt.client as mqtt

# Configurações do broker MQTT
broker_address = "localhost"
topic = "logs/#"

# Callback para quando uma mensagem é recebida
def on_message(client, userdata, message):
    log_message = message.payload.decode("utf-8")
    print(f"Received log: {log_message}")

# Função principal do servidor de logs
def start_log_server():
    client = mqtt.Client("LogReceiver", protocol=mqtt.MQTTv311)  # Defina a versão do protocolo
    client.on_message = on_message

    client.connect(broker_address)
    client.subscribe(topic)

    client.loop_forever()

if __name__ == "__main__":
    start_log_server()
