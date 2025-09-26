from pytubefix import YouTube
from pytubefix.cli import on_progress

url = "https://www.youtube.com/watch?v=P0Fk-K2eZF8"

yt = YouTube(url, on_progress_callback=on_progress)
print(f"Title: {yt.title}")

ys = yt.streams.filter(only_audio=True).first()
ys.download()