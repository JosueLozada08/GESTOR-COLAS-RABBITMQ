import pika
import logging

# Configurar logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def send_message():
    try:
        # Conectar a RabbitMQ en localhost, puerto 5672
        connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', 5672))
        channel = connection.channel()
        channel.queue_declare(queue='correo')
        
        mensaje = 'Este es un mensaje de prueba'
        channel.basic_publish(exchange='', routing_key='correo', body=mensaje)
        logging.info(f"Mensaje enviado: {mensaje}")
        
        connection.close()
    except Exception as e:
        logging.error(f"Error al enviar el mensaje: {e}")

if __name__ == '__main__':
    send_message()
