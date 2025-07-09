from fastapi import FastAPI, Query
from youtube_transcript_api import YouTubeTranscriptApi
import re

app = FastAPI()

def extract_video_id(url: str):
    match = re.search(r"(?:v=|youtu.be/)([a-zA-Z0-9_-]{11})", url)
    return match.group(1) if match else None

@app.get("/get_transcript")
def get_transcript(video_url: str = Query(...)):
    video_id = extract_video_id(video_url)
    if not video_id:
        return {"error": "Invalid YouTube URL"}

    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        return {"video_id": video_id, "transcript": transcript}
    except Exception as e:
        return {"error": str(e)}
