import asyncio
import datetime
import os
import sys
import time

import spotify

client_id = os.environ["SPOTIFY_ID"]
client_secret = os.environ["SPOTIFY_SECRET"]
username = os.environ.get("SPOTIFY_USERNAME", "court-jus")
playlist_url = os.environ.get("SPOTIFY_PLAYLIST", "https://open.spotify.com/playlist/6AMT4wWjtZ0m6hKgKjiz4G")
clearscreen = lambda: os.system("clear")


async def main():
    async with spotify.Client(client_id, client_secret) as client:
        user = await client.get_user(username)

        print("User found: ", user)
        playlists = await user.get_all_playlists()
        for p in playlists:
            if p.url == playlist_url:
                break
        else:
            print("Playlist not found")
            return

        should_stop_at = datetime.datetime.now().replace(
            hour=9, minute=1, second=0, microsecond=0
        )
        length = 0
        all_tracks = await p.get_all_tracks()
        playlist = []
        for t in all_tracks[::-1]:
            length += t.duration
            sta = should_stop_at - datetime.timedelta(milliseconds=length)
            playlist.append(t)
            if sta <= datetime.datetime.now():
                break

    while True:
        time.sleep(1)
        clearscreen()
        should_stop_at = datetime.datetime.now().replace(
            hour=9, minute=1, second=0, microsecond=0
        )
        length = 0
        print(should_stop_at.strftime("%H:%M:%S"), "End of playlist", p.name)
        for t in playlist:
            length += t.duration
            sta = should_stop_at - datetime.timedelta(milliseconds=length)
            playlist.append(
                {"track": t.name, "sta": sta,}
            )
            if sta > datetime.datetime.now():
                print(sta.strftime("%H:%M:%S"), t.name)
            else:
                print(
                    sta.strftime("%H:%M:%S"),
                    t.name,
                    "(currently at",
                    datetime.datetime.now() - sta,
                    ")",
                )
                break


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
