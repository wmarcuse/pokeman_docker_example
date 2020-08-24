from pokeman import Pokeman, ConnectionParameters, Exchange, Queue, RoutingKey
from pokeman.coatings import BasicMessage, Ptypes


# Always, first declare the Pokeman
# The AMQP resources will be attached to the first (default) Pokeman instance
poker = Pokeman()

# Set the connection parameters
connection_parameters = ConnectionParameters(connstr='amqp://guest:guest@host.docker.internal:5672')

# Apply the connection parameters to the Pokeman
poker.set_parameters(connection=connection_parameters)

# Start poking around, by connecting the Pokeman with your AMQP broker
poker.start()

# Create your AMQP resources objects
# The resources will be assigned to a HeapQ attached to the default Pokeman, or specific Pokeman if declared
my_exchange = Exchange(exchange_name='my_exchange')
my_routing_key = RoutingKey(key='my.routing.key')
my_queue = Queue(queue_name='my_queue', exchange=my_exchange, routing_key=my_routing_key, specific_poker=poker)

# Apply the resources to the AMQP broker, that's it!
# You can verify i.e. via the RabbitMQ Management plugin that the resources are created http://127.0.0.1:15672/
poker.apply_resources()

# Set up the basic message coating
basic_message_coating = BasicMessage(app_id='MY_APP', exchange=my_exchange, routing_key=my_routing_key)

# Declare the producer
sync_producer_1 = poker.declare_producer(coating=basic_message_coating, ptype=Ptypes.SYNC_PRODUCER)

# Publish a message
sync_producer_1.publish(message={"a": 1})

# Stop the Pokeman
poker.stop()