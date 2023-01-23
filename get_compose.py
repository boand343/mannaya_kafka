import requests

response = requests.get('https://raw.githubusercontent.com/bitnami/containers/main/bitnami/kafka/docker-compose.yml')

with open('docker-compose.yml', 'bw') as file:
    file.write(response.content)
