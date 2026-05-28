SELECT_FILM = """
SELECT title
FROM film
WHERE UPPER(title) LIKE %s
ORDER BY film_id LIMIT 10
"""

SELECT_GENRE = """
SELECT name
FROM category
"""

SELECT_FILM_BY_GENRE = """
SELECT title
FROM film f            
JOIN film_category fc ON f.film_id = fc.film_id
JOIN category c ON fc.category_id = c.category_id
WHERE c.category_id = %s
"""


SELECT_FILM_BY_GENRE_AND_YEAR = """
SELECT title
FROM film f            
JOIN film_category fc ON f.film_id = fc.film_id
JOIN category c ON fc.category_id = c.category_id
WHERE c.category_id = %s AND f.release_year = %s
"""