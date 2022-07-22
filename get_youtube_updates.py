import requests

url = "https://www.googleapis.com/youtube/v3/search?part=snippet&channelId=UCDdKEz8e7m5g-hXg42-HBQg&order=date&maxResults=1&access_token=[Collect_From_google_dev_console]"

payload = {}
files = {}
headers= {}

response = requests.request("GET", url, headers=headers, data = payload, files = files)

# print(response.text.encode('utf8'))

rs=response.json()


youtube="https://www.youtube.com/watch?v="
video_id= rs["items"][0]["id"]["videoId"]

print("Check out "+youtube+""+video_id)
