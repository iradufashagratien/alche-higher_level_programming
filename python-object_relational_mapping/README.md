# python-object_relational_mapping

Python scripts connecting to a MySQL database two ways: directly with
MySQLdb (raw SQL queries, tasks 0-5) and through SQLAlchemy's ORM
(Python objects instead of SQL, tasks 6-14).

## Requirements
- Python 3.8.5, MySQL 8.0
- MySQLdb 2.0.x, SQLAlchemy 1.4.x
- pycodestyle 2.7.*

## Files
- 0-select_states.py to 5-filter_cities.py : raw MySQLdb scripts
- model_state.py, model_city.py            : SQLAlchemy model classes
- 6-...py to 14-...py                      : SQLAlchemy ORM scripts

## Usage
./script.py <mysql_username> <mysql_password> <database_name> [extra args]
