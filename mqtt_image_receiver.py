import os
import logging
import paho.mqtt.client as mqtt
import base64

# Configuration
broker = 'broker.hivemq.com'
port = 1883
topic = 'image'
received_folder = 'received_images'
counter_file = 'image_counter.txt'

# Set up logging
logging.basicConfig(filename='mqtt_image_receiver.log', level=logging.INFO,
                    format='%(asctime)s %(levelname)s:%(message)s')

# MQTT callbacks
def on_connect(client, userdata, flags, rc):
    logging.info(f"Connected with result code {rc}")
    print(f"Connected with result code {rc}")
    client.subscribe(topic)

def on_message(client, userdata, msg):
    try:
        # Decode image
        image_data = base64.b64decode(msg.payload)
        
        # Get the next image number
        image_number = get_next_image_number(counter_file)
        
        # Save image to file with unique numeric name
        os.makedirs(received_folder, exist_ok=True)
        image_path = os.path.join(received_folder, f'image_{image_number:04d}.jpg')
        with open(image_path, 'wb') as file:
            file.write(image_data)
        
        logging.info(f"Image saved to {image_path}")
        
        # Update the image counter
        update_image_number(counter_file, image_number + 1)
    except Exception as e:
        logging.error(f"Failed to save image: {e}")

# Get next image number
def get_next_image_number(counter_file):
    try:
        with open(counter_file, 'r') as file:
            number = int(file.read().strip())
    except FileNotFoundError:
        number = 1
    return number

# Update image number
def update_image_number(counter_file, number):
    with open(counter_file, 'w') as file:
        file.write(str(number))

# Main function
def main():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(broker, port, 60)
    client.loop_start()

    try:
        while True:
            pass  # Keep the script running to receive messages
    except KeyboardInterrupt:
        logging.info("Keyboard interrupt detected. Stopping the script.")
    except Exception as e:
        logging.error(f"Unexpected error occurred: {e}")

    client.loop_stop()
    client.disconnect()

if __name__ == "__main__":
    main()
