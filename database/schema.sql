DROP TABLE IF EXISTS search_db;

CREATE TABLE search_db (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    summoner_name TEXT NOT NULL,
    phone_number INTEGER NOT NULL,
    phone_call_choice BOOLEAN NOT NULL,
    text_message_choice BOOLEAN NOT NULL
);
