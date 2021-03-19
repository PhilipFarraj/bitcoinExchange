# bitcoinExchange

Sample Task to retrieve data from API's

## Requirments
- Docker: https://docs.docker.com/engine/installation/
- Docker-compose: https://docs.docker.com/compose/install/

## Getting Started


Steps to activate the app
1. Clone/Download the repo:
`git clone --depth 1 https://github.com/PhilipFarraj/bitcoinExchange`
2. Navigate to bitcoinExchange => docker-build
`cd bitcoinExchange/docker-build/`
3. RUN : docker-compose up -d 
4. RUN : docker-compose exec server bash
5. RUN : python manage.py createsuperuser
After creating the user 
6. On Browser: go to 127.0.0.1:8000/admin
7. Create the task from the perdioc task table
8. RUN : docker-compose restart
9. RUN : docker-compose up
