import sys
import re
from youtube_transcript_api import YouTubeTranscriptApi

def get_transcript(url):
    # Extract the Video ID from the URL
    pattern = r'(?:v=|\/)([0-9A-Za-z_-]{11}).*'
    match = re.search(pattern, url)
    
    if not match:
        return "Error: Invalid YouTube link."
    
    video_id = match.group(1)
    
    try:
        # NEW SYNTAX: We must initialize the API first
        api = YouTubeTranscriptApi()
        
        # Fetch the transcript data directly
        transcript_data = api.fetch(video_id)
        
        # Join the list of text blocks into one massive paragraph
        full_text = " ".join([item.text for item in transcript_data])
        return full_text
    
    except Exception as e:
        # This generic exception gracefully catches "No transcript found" edge cases!
        return f"Error: Could not fetch transcript. Details: {str(e)}"

# This allows OpenClaw to pass the URL to the script via the command line
if __name__ == "__main__":
    sys.stdout.reconfigure(encoding='utf-8')
    if len(sys.argv) > 1:
        video_url = sys.argv[1]
        print(get_transcript(video_url))
    else:
        print("Error: No URL provided.")