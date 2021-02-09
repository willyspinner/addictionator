DROP TABLE IF EXISTS search_db;

CREATE TABLE user_db (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    summoner_name TEXT NOT NULL,
    phone_number INTEGER NOT NULL,
    phone_call_choice BOOLEAN,
    text_message_choice BOOLEAN
);
