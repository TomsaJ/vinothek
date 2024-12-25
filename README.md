docker build -t vino .


docker run -e DB_HOST=mydbhost \
           -e DB_PORT=3306 \
           -e DB_USER=root \
           -e DB_PASSWORD=securepassword \
           -e DB_NAME=mydatabase \
           -p 5000:5000 \
           vino
