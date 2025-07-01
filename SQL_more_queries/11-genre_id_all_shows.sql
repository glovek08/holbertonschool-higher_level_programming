-- @block
SELECT
	tv_genres.name AS '<TV Show genre>',
	COUNT(tv_show_genres.show_id) AS '<Number of shows linked to this genre>'
FROM 
	tv_genres,
	tv_show_genres
WHERE
	tv_genres.id = tv_show_genres.genre_id
GROUP BY tv_genres.name
ORDER BY COUNT(tv_show_genres.show_id) DESC;