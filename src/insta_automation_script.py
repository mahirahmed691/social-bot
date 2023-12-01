import sys
import requests
import json

# Instagram API endpoint URLs
upload_url = "https://graph.instagram.com/v12.0/me/media"
publish_url = "https://graph.instagram.com/v12.0/{media_id}?fields=id,caption,media_type,thumbnail_url,permalink,thumbnail_url,media_url,thumbnail_url,timestamp,username"

# Replace 'ACCESS_TOKEN' with your actual access token
access_token = 'ACCESS_TOKEN'

# Function to upload a photo and get the media ID
def upload_photo(file_path):
    headers = {'Authorization': f'Bearer {access_token}'}
    files = {'media': open(file_path, 'rb')}
    response = requests.post(upload_url, headers=headers, files=files)
    print(response.content)  # Print the response content

    # Check if the response is successful (status code 200)
    if response.status_code == 200:
        try:
            # Try to parse the response as JSON and get the media ID
            media_id = response.json().get('id')
            return media_id
        except json.decoder.JSONDecodeError:
            print("Error decoding JSON in upload response.")
            return None
    else:
        # Print an error message for non-successful responses
        print(f"Error uploading photo. Status code: {response.status_code}")
        print(response.content)
        return None

# Function to publish a photo with a caption and link
def publish_photo(media_id, caption, link):
    headers = {'Authorization': f'Bearer {access_token}'}
    params = {'caption': caption, 'media_id': media_id}

    # Add the link to the caption
    if link:
        caption += f"\n{link}"

    # Publish the photo with caption and link
    response = requests.post(publish_url.format(media_id=media_id), headers=headers, params=params)

    # Print the response
    print(response.json())

# Example usage
if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python insta_automation_script.py <file_path> <caption> <link>")
        sys.exit(1)

    file_path = sys.argv[1]
    caption = sys.argv[2]
    link = sys.argv[3]

    media_id = upload_photo(file_path)

    if media_id:
        publish_photo(media_id, caption, link)
