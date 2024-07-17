import pika
import smtplib
import logging

# Configurar logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def callback(ch, method, properties, body):
    try:
        mensaje = body.decode('utf-8')
        destinatario = 'ejemplo@dominio.com'
        remitente = 'remitente@dominio.com'
        asunto = 'Mensaje recibido desde la cola'

        servidor_smtp = 'smtp.ejemplo.com'
        puerto_smtp = 587
        cuerpo_mensaje = f'Asunto: {asunto}\n\n{mensaje}'

        with smtplib.SMTP(servidor_smtp, puerto_smtp) as servidor:
            servidor.starttls()
            servidor.login('usuario@dominio.com', 'contraseña')
            servidor.sendmail(remitente, destinatario, cuerpo_mensaje)
        
        logging.info(f"Mensaje enviado por correo electrónico: {mensaje}")
    except Exception as e:
        logging.error(f"Error al procesar el mensaje: {e}")

def main():
    try:
        # Conectar a RabbitMQ en localhost, puerto 5672
        connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', 5672))
        channel = connection.channel()
        channel.queue_declare(queue='correo')
        channel.basic_consume(queue='correo', on_message_callback=callback, auto_ack=True)
        
        logging.info('Esperando mensajes. Presiona CTRL+C para salir.')
        channel.start_consuming()
    except Exception as e:
        logging.error(f"Error al conectar con RabbitMQ: {e}")

if __name__ == '__main__':
    main()
