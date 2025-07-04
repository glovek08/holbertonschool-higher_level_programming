-- @block
SELECT
	shows.title, tv_genres.name
FROM
	tv_shows shows
LEFT JOIN
	tv_show_genres
		ON shows.id = tv_show_genres.show_id
LEFT JOIN
	tv_genres
		ON tv_show_genres.genre_id = tv_genres.id
	
ORDER BY 
	shows.title ASC,
    tv_genres.name ASC;