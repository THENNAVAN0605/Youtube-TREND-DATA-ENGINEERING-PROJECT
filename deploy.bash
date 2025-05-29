gcloud functions deploy fetch_youtube_trends \
  --runtime python310 \
  --trigger-http \
  --allow-unauthenticated \
  --entry-point fetch_youtube_trends \
  --timeout 540s \
  --memory 256MB
