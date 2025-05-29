SELECT title, channel, viewCount, publishedAt
FROM YOUR_PROJECT_ID.youtube.trending_videos
WHERE publishedAt >= TIMESTAMP_SUB(CURRENT_TIMESTAMP(), INTERVAL 1 DAY)
ORDER BY viewCount DESC
LIMIT 10
