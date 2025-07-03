-- Lists all shows and their genres from the hbtn_0d_tvshows database
-- If a show doesn’t have a genre, display NULL in the genre column
-- Results sorted by show title and genre name in ascending order

SELECT tv_shows.title, tv_genres.name
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
LEFT JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id
ORDER BY tv_shows.title ASC, tv_genres.name ASC;

