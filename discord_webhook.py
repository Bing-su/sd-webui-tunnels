import requests


def send_to_discord(message: str, webhook_url: str) -> bool:
    """
    Sends a message to a Discord channel using a webhook URL.
    Args:
        message (str): The message to send to the Discord channel.
        webhook_url (str): The Discord webhook URL for the channel to send the message to.
    Returns:
        bool: True if the message was successfully sent, False otherwise.
    """
    try:
        # Define the JSON payload to send to the webhook URL.
        payload = {"content": message}

        # Make a POST request to the webhook URL with the JSON payload.
        response = requests.post(webhook_url, json=payload)

        # Check the response status code and return True if it was successful.
        response.raise_for_status()
        return True

    except Exception as e:
        # If there was an error sending the message, print the error message and return False.
        print(f"Error sending message to Discord channel: {e}")
        return False
