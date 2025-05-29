SELECT hashtag, COUNT(*) AS frequency
FROM (
  SELECT SPLIT(hashtags, ",") AS tags
  FROM `YOUR_PROJECT_ID.youtube.trending_videos`
  WHERE publishedAt >= TIMESTAMP_SUB(CURRENT_TIMESTAMP(), INTERVAL 1 DAY)
), UNNEST(tags) AS hashtag
WHERE LENGTH(hashtag) > 1
GROUP BY hashtag
ORDER BY frequency DESC
LIMIT 10
