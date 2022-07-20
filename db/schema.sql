DROP TABLE IF EXISTS urls;

CREATE TABLE urls (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    shorten_id TEXT NOT NULL,
    original_url TEXT NOT NULL,
    deletion_url TEXT NOT NULL
)

-- update schema
-- generate deletion_url portion 
-- add it into db
-- provide it to user with proper route + deletion_url localhost:5000/delete/dk123j1
-- create delete route that checks the database to delete the url created