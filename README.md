# mqtt-image-capture-and-reception
MQTT-based image capture and reception system using Python


# MQTT Image Capture and Receiver

This project consists of two Python scripts using MQTT to capture images from a camera and send them to a receiver system. The receiver system saves the received images with unique filenames.

## Prerequisites

- Python 3.x
- `paho-mqtt` library

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/shahroz8899/mqtt-image-capture-and-reception.git
    cd mqtt-image-capture-and-reception
    ```

2. Create and activate a virtual environment:

    ```bash
    python3 -m venv myenv
    source myenv/bin/activate
    ```

3. Install required packages:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

### Publisher Script

1. Ensure your camera is connected and properly configured.
2. Run the image publisher script:

    ```bash
    python3 mqtt_image_publisher.py
    ```

### Receiver Script

1. Run the image receiver script on the receiver system:

    ```bash
    python3 mqtt_image_receiver.py
    ```

## Configuration

- **Broker**: `broker.hivemq.com`
- **Port**: `1883`
- **Topic**: `image`

Images will be saved in the `your desired` directory with incremented numeric filenames.

## Logging

Logs are stored in `mqtt_image_publisher.log` and `mqtt_image_receiver.log`.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
