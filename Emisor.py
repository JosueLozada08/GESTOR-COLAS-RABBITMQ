import pika

def send_message():
    # Configuración de conexión con RabbitMQ
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    # Declarar una cola
    channel.queue_declare(queue='correo')

    # Enviar un mensaje a la cola
    mensaje = 'Este es un mensaje de prueba'
    channel.basic_publish(exchange='', routing_key='correo', body=mensaje)

    print(f"Mensaje enviado: {mensaje}")

    # Cerrar la conexión
    connection.close()

if __name__ == '__main__':
    send_message()
