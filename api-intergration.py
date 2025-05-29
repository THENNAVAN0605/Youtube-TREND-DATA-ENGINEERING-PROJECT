import base64
import json
import re
from googleapiclient.discovery import build
from google.cloud import bigquery

def fetch_youtube_trends(request):
    YOUTUBE_API_KEY = "YOUR_YOUTUBE_API_KEY"
    youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)
    
    bq_client = bigquery.Client()
    table_id = 'YOUR_PROJECT_ID.youtube.trending_videos'
    
    request = youtube.videos().list(
        part="snippet,statistics",
        chart="mostPopular",
        regionCode="IN",
        maxResults=10
    )
    
    response = request.execute()
    rows_to_insert = []
    
    for item in response['items']:
        description = item['snippet'].get('description', '')
        hashtags = extract_hashtags(description)

        row = {
            "video_id": item["id"],
            "title": item["snippet"]["title"],
            "channel": item["snippet"]["channelTitle"],
            "categoryId": item["snippet"]["categoryId"],
            "viewCount": int(item["statistics"].get("viewCount", 0)),
            "publishedAt": item["snippet"]["publishedAt"],
            "description": description,
            "hashtags": hashtags
        }
        rows_to_insert.append(row)

    errors = bq_client.insert_rows_json(table_id, rows_to_insert)
    if errors:
        return f"Errors: {errors}", 500
    return f"Inserted {len(rows_to_insert)} rows", 200

def extract_hashtags(text):
    return ','.join(re.findall(r"#\w+", text))
