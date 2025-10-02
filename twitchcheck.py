import requests
 
# Input your Twitch credentials
CLIENT_ID = input("Client ID: ")
OAUTH_TOKEN = input("OAuth token: ")
CHANNEL_NAME = input("Channel you wish to view the status of: ")
 
def is_channel_live(channel_name):
    url = f'https://api.twitch.tv/helix/streams?user_login={channel_name}'
    headers = {
        "Client-ID": CLIENT_ID,
        "Authorization": f'Bearer {OAUTH_TOKEN}'
    }
 
    response = requests.get(url, headers=headers)
    data = response.json()
 
    if data.get("data"):
        stream_info = data["data"][0]
        return {
            "is_live": True,
            "viewer_count": stream_info['viewer_count']
        }
    else:
        return {
            "is_live": False,
            "viewer_count": 0
        }

result = is_channel_live(CHANNEL_NAME)
if result['is_live']:
    print(f"{CHANNEL_NAME} is live with {result['viewer_count']} viewers.")
else:
    print(f"{CHANNEL_NAME} is not live.")
