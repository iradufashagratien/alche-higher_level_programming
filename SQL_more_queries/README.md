# SQL_more_queries

Project completed as part of the SQL curriculum. Covers user creation,
privileges, table constraints (NOT NULL, DEFAULT, UNIQUE, AUTO_INCREMENT,
FOREIGN KEY), subqueries, JOINs (INNER and LEFT), GROUP BY, and aggregate
functions in MySQL 8.0 on Ubuntu 20.04.

## How to run a script
cat <script_name>.sql | mysql -hlocalhost -uroot -p [database_name]

## Files
- 0-privileges.sql       : show grants for two users
- 1-create_user.sql      : create a user with all privileges
- 2-create_read_user.sql : create a database + read-only user
- 3-force_name.sql       : table with a required name column
- 4-never_empty.sql      : table with a default id value
- 5-unique_id.sql        : table with a unique id
- 6-states.sql           : states table (id, name)
- 7-cities.sql           : cities table linked to states by foreign key
- 8-cities_of_california_subquery.sql : subquery, no JOIN
- 9-cities_by_state_join.sql          : cities + state name via JOIN
- 10-genre_id_by_show.sql             : shows with a genre linked
- 11-genre_id_all_shows.sql           : all shows, NULL if no genre
- 12-no_genre.sql                     : shows without a genre
- 13-count_shows_by_genre.sql         : show count grouped by genre
- 14-my_genres.sql                    : genres of a specific show
- 15-comedy_only.sql                  : shows in one genre
- 16-shows_by_genre.sql               : every show + every genre, NULL-safe
