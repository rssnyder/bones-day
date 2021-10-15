from TikTokApi import TikTokApi
from tinydb import TinyDB, Query
from requests import post
from os import getenv


if __name__ == "__main__":

    db = TinyDB("jongraz.json")
    videos = Query()

    api = TikTokApi()
    user_videos = api.by_username("jongraz", count=5)

    for video in user_videos:
        video_id = video.get("video", {}).get("id", "")

        if db.search(videos.id == video_id):
            print("already sent video")
            continue

        video_url = f"https://www.tiktok.com/@jongraz/video/{video_id}"
        try:
            resp = post(
                "https://api.groupme.com/v3/bots/post",
                json={"text": video_url, "bot_id": getenv("BOT_ID")},
            )
            resp.raise_for_status()
        except:
            print("unable to send message")
            print(resp.text)
        else:
            db.insert({"id": video_id})
