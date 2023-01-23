# mannaya_kafka

Поднимаем контейнеры:
docker compose up --build


После того, как запустится kafka можно запустить писателя и читателя, для наглядности сделать это из контейнера:
Вход в контейнер consumer

docker exec -it consumer bash

python consumer/consumer/py

Вход в контейнер producer

docker exec -it producer bash

python producer/producer/py
