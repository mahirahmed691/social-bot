import sys
import requests
import json

# Replace 'YOUR_ACCESS_TOKEN' with your actual access token
access_token = 'EAAFg7Vk1Ol0BOZCtYOXxahEHcKRYu8dXcOS7gfpwXgWvRJDPWUgNTRipzfgaKmGwCbTKiF7w9UeSVZBk5m1aPK8ELZCupvxJTsdZBKa1vyRDcZArmg0vn7yNZBtQ8PR8cwsE0CkN8EKZBdwLAb5MmdmFsr7GuEFv8nhLoFqxdX0PgPSj2jfZBAEXk7C5CBjNBZBBdzoJQdA7p4nF1IKPax0Qfh5a56DgRqy3bUzJtFGcGgm6w9pnPHNaLX613mA8ZD'
user_id = '8999508672040200888'

# Instagram API endpoint URLs
upload_url = f'https://graph.instagram.com/v12.0/{user_id}/media'
media_url = f'https://graph.instagram.com/v12.0/{user_id}/media?fields=id,caption,media_type,thumbnail_url,permalink,media_url,timestamp,username&access_token={access_token}'

def upload_photo(file_path, caption):
    headers = {'Authorization': f'Bearer {access_token}'}
    files = {'media': open(file_path, 'rb')}
    data = {'caption': caption}
    response = requests.post(upload_url, headers=headers, files=files, data=data)

    print(response.content)

    if response.status_code == 200:
        try:
            media_id = response.json().get('id')
            return media_id
        except json.decoder.JSONDecodeError:
            print("Error decoding JSON in upload response.")
            return None
    else:
        print(f"Error uploading photo. Status code: {response.status_code}")
        print(response.content)
        return None

def retrieve_media():
    response = requests.get(media_url)

    if response.status_code == 200:
        data = response.json()
        for media_item in data.get('data', []):
            media_id = media_item.get('id')
            media_info_url = f'https://graph.instagram.com/v12.0/{media_id}?fields=id,caption,media_type,thumbnail_url,permalink,media_url,timestamp,username&access_token={access_token}'

            media_info_response = requests.get(media_info_url)

            if media_info_response.status_code == 200:
                media_info = media_info_response.json()
                print(f"Media ID: {media_info.get('id')}")
                print(f"Caption: {media_info.get('caption', '').get('text')}")
                print(f"Media Type: {media_info.get('media_type')}")
                print(f"Thumbnail URL: {media_info.get('thumbnail_url')}")
                print(f"Permalink: {media_info.get('permalink')}")
                print(f"Timestamp: {media_info.get('timestamp')}")
                print(f"Username: {media_info.get('username')}")
                print(f"Instagram Post: https://www.instagram.com/p/{media_info.get('id')}")
                print("\n---\n")
            else:
                print(f"Error getting media info. Status code: {media_info_response.status_code}")
                print(media_info_response.content)
    else:
        print(f"Error getting media. Status code: {response.status_code}")
        print(response.content)



if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python insta_automation_script.py <file_path> <caption> <link>")
        sys.exit(1)

    file_path = sys.argv[1]
    caption = sys.argv[2]
    link = sys.argv[3]

    print("Uploading photo...")
    media_id = upload_photo(file_path, caption)

    if media_id:
        print("Media uploaded successfully!")
        print("Retrieving user's media:")
        retrieve_media()
    else:
        print("Failed to upload media. Aborting retrieval.")
