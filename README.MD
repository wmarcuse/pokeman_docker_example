# Start RabbitMQ locally

    docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3-management

# Build the Dockerfile

    docker build -t pokeman-sandbox:latest .
    
# Run the Dockerfile

    docker run pokeman-sandbox:latest
    
# Check the RabbitMQ Management Dashboard

Go to http://localhost:15672/ and check the Pokeman activities.