# About

- This is a Python command line application.
- This application is used to add, find, update, and delete your bookmark.

# Environment setting

- In order to use this application you must have [Postgres](https://www.postgresql.org/) and [Pipenv](https://pipenv.pypa.io/en/latest/) installed.

## Set the database

1. Open Postgres in your terminal.
   ```
   psql
   ```
2. Create a new database with name of bookmark.
   ```
   create database bookmark
   ```
3. Open `main.py` file with the editor you like, and change the user and password to be yours
   ```
   db=PostgresqlDatabase(
    'bookmark',
    user='yours',
    password='yours',
    host='localhost',
    port=5432
   )
   ```

## Install dependencies

1. Clone this repo and change into the new directory.
2. Use pipenv shell.
   ```
   pipenv shell
   ```
3. Install all the dependencies.
   ```
   pipenv install
   ```

# How to use

In `python-bookmark` directory

1.  add: you can add new bookmark with this command

    ```
    python main.py add
    ```

    example:

    ```
    (python-bookmark) bash-3.2$ python main.py add
    Enter the tilte of the bookmark: YouTube
    Enter the link of the bookmark: https://www.youtube.com/
    YouTube: https://www.youtube.com/ added
    ```

2.  find: you can find a bookmark you have added with this command

    ```
    python main.py find
    ```

    example:

    ```
    (python-bookmark) bash-3.2$ python main.py find
    Enter the bookmark title that you want to look for: YouTube
    ['YouTube: https://www.youtube.com/']
    ```

3.  find_all: you can find all bookmarks you have added with this command

    ```
    python main.py find_all
    ```

    example:

    ```
    (python-bookmark) bash-3.2$ python main.py find_all
     ['YouTube: https://www.youtube.com/']
    ```

4.  update: you can update one bookmark you have added with this command
    ```
    python main.py update
    ```
    example:
    ```
    (python-bookmark) bash-3.2$ python main.py update
    Enter the title of the boonkmark you want to update: YouTube
    Enter the new title of the boonkmark you want to update: MeTube
    Enter the new link of the boonkmark you want to update: https://www.metube.com/
    updated to MeTube: https://www.metube.com/
    ```
5.  delete: you can delete one bookmark you have added with this command
    ```
    python main.py delete
    ```
    example:
    ```
    (python-bookmark) bash-3.2$ python main.py delete
    Enter the title of the boonkmark you want to delete: MeTube
    MeTube deleted
    ```
