SELECT_FILM = """
SELECT title
FROM film
WHERE UPPER(title) LIKE %s
ORDER BY film_id LIMIT 10
"""