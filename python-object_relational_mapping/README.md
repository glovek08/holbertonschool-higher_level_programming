# Python - Object-relational mapping

This project covers the basics of object-relational mapping (ORM) in Python, focusing on interacting with databases using Python objects.

## Files

- **0-select_states.py**: Connects to a MySQL database and lists all states from the `states` table.
- **1-filter_states.py**: Lists all states with a name starting with 'N' from the database.
- **2-my_filter_states.py**: Displays all values in the `states` table where `name` matches a given argument.
- **3-my_safe_filter_states.py**: Uses parameterized queries to prevent SQL injection when filtering states.
- **4-cities_by_state.py**: Lists all cities from the database, showing their corresponding state.
- **5-filter_cities.py**: Displays all cities of a given state, passed as an argument.
- **model_state.py**: Defines a `State` class mapped to the `states` table using SQLAlchemy ORM.
- **model_city.py**: Defines a `City` class mapped to the `cities` table using SQLAlchemy ORM.
- **7-model_state_fetch_all.py**: Lists all `State` objects from the database using SQLAlchemy.
- **8-model_state_fetch_first.py**: Prints the first `State` object from the database using SQLAlchemy.
- **9-model_state_filter_a.py**: Lists all `State` objects containing the letter 'a' using SQLAlchemy.
- **10-model_state_my_get.py**: Prints the `State` object with a specific `id` using SQLAlchemy.
- **11-model_state_insert.py**: Adds a new `State` object to the database using SQLAlchemy.
- **12-model_state_update_id_2.py**: Updates the name of a `State` object with a specific `id` using SQLAlchemy.
- **13-model_state_delete_a.py**: Deletes all `State` objects containing the letter 'a' using SQLAlchemy.
- **14-model_city_fetch_by_state.py**: Lists all `City` objects and their associated `State` using SQLAlchemy.

## Requirements

- Python 3.x
- MySQLdb or SQLAlchemy
- MySQL server
