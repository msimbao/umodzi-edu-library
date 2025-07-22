import base64
import requests
import os

def download_and_convert_to_base64(image_url, output_txt_path):
    try:
        # Get the image content from the URL
        response = requests.get(image_url)
        response.raise_for_status()  # Raise an error if the request failed

        # Encode image content to base64
        encoded_string = base64.b64encode(response.content).decode('utf-8')

        # Save to text file
        with open(output_txt_path, 'w') as text_file:
            text_file.write(encoded_string)

        print(f"Base64 saved to {output_txt_path}")

    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    image_url = input("")
    output_file = input("Enter the path to save the Base64 text (e.g., output.txt): ")
    download_and_convert_to_base64(image_url, output_file)
