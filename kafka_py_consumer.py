from kafka import KafkaConsumer

consumer = KafkaConsumer('stock')
for msg in consumer:
    print (msg)
