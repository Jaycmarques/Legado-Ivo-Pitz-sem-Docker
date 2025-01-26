#!/bin/bash

docker compose down
sudo rm -r ./data
docker compose up -d
docker compose run --rm web python makemigrations
docker compose run --rm web python migrate
docker compose run --rm web python manage.py populate_tree ./familytree/TreeFromWebsite.txt
docker compose up -d
docker compose run --rm web python manage.py runserver 8000
