-- Genre ID for all shows
SELECT tv_shows.title tv_show_genres.genre_id
FROM tv_shows
INNER JOIN tv_shows tv_genres
ON 
