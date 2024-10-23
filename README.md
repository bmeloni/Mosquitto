# Projeto de Sistema de Logs com Mosquitto (MQTT)
Este projeto implementa um sistema de logs centralizado utilizando o protocolo MQTT com o broker Mosquitto. A aplicação é composta por dois serviços principais: Log Publisher e Log Server, que se comunicam de forma desacoplada através do Mosquitto.

### Projeto Acadêmico
Este projeto foi desenvolvido como parte de um trabalho acadêmico para a disciplina de Fundamentos de Comunicação de Dados e Redes de Computadores, no curso de Engenharia de Softare da PUC-Campinas.

### Arquitetura da Aplicação
A aplicação segue o modelo publish/subscribe:
* **Log Publisher:** Publica logs no tópico logs/service1.
* **Mosquitto Broker:** Atua como intermediário, recebendo as mensagens do Log Publisher e as distribuindo para os assinantes.
* **Log Server:** Assina o tópico logs/# e recebe todas as mensagens de log publicadas no broker.

## Requisitos
Certifique-se que os seguintes requisitos estão instalados e configurados:
* **Docker** (para rodar o Mosquitto em um contêiner)
* **Python 3.12** (usado para rodar os scripts Python)
* **Biblioteca Paho MQTT para Python:**
```pip install paho-mqtt==1.6.1``` 

## Configuração do Projeto
1. Rodar o Mosquitto no Docker
Baixe a imagem do Mosquitto e rode o broker usando o Docker:

    ```docker pull eclipse-mosquitto```

    ```docker run -d -p 1883:1883 --name mosquitto_new eclipse-mosquitto```

3. Rodar o Log Server
Abra um terminal no diretório do projeto e execute o log_server.py para começar a receber os logs:
```python log_server.py```

4. Rodar o Log Publisher
Em outro terminal, execute o log_publisher.py para começar a enviar logs ao broker Mosquitto:
```python log_publisher.py```

5. Verificar a Comunicação
O Log Server exibirá as mensagens de log que forem publicadas pelo Log Publisher. O sistema utiliza o broker Mosquitto para intermediar a comunicação.

## Instruções Adicionais
* Parar o contêiner Mosquitto:
```docker stop mosquitto_new```

* Iniciar novamente o contêiner Mosquitto:
```docker start mosquitto_new```

## Possíveis Erros e Soluções
Erro de conexão com o Mosquitto: Verifique se o broker Mosquitto está rodando corretamente no Docker usando docker ps para confirmar.

Biblioteca paho-mqtt não instalada: Certifique-se de ter instalado a biblioteca necessária para o Python:
```pip install paho-mqtt==1.6.1```