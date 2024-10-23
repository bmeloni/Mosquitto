import paho.mqtt.client as mqtt
import time
import random

# Configurações do broker MQTT
broker_address = "localhost"
topic = "logs/service1"

# Função para publicar logs
def publish_logs():
    client = mqtt.Client("LogPublisher1")
    client.connect(broker_address)

    while True:
        # Simula diferentes níveis de logs
        log_level = random.choice(["INFO", "WARNING", "ERROR"])
        log_message = f"{log_level}: Log message from service 1"
        
        # Publica a mensagem no tópico MQTT
        client.publish(topic, log_message)
        print(f"Log sent: {log_message}")
        
        time.sleep(5)

if __name__ == "__main__":
    publish_logs()
