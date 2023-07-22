CREATE TABLE IF NOT EXISTS raw.activity_records (
    id SERIAL PRIMARY KEY,
    activity_icon VARCHAR(10) NOT NULL,
    user_id INTEGER NOT NULL,
    create_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);