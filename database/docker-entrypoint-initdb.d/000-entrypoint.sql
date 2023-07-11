CREATE SCHEMA IF NOT EXISTS "raw" AUTHORIZATION CURRENT_USER;

TRUNCATE TABLE IF EXISTS raw.activities;
CREATE TABLE raw.activities (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    icon VARCHAR(10) NOT NULL,
    value INTEGER NOT NULL DEFAULT 0
    
);

INSERT INTO activities (id, name, icon, value) VALUES
(1, 'Wstawienie zmywarki', '🧆', 2),
(2, 'Rozładowanie zmywarki', '🍽️', 2),
(3, 'Umycie blatu w kuchni', '🧽', 3),
(4, 'Wyrzucenie śmieci', '🗑️', 2),
(5, 'Wstawienie pralki', '🧺', 2),
(6, 'Powieszenie prania', '☀️', 2),
(7, 'Ubrania do szafy', '👔', 3),
(8, 'Umycie zlewu', '🚰', 3),
(9, 'Odkurzenie domu', '🌪️', 5),
(10, 'Umycie umywalki', '🪥', 3),
(11, 'Usunięcie owłosienia', '💩', 3),
(12, 'Umycie kabiny prysznicowej', '🚿', 5),
(14, 'Zakupy', '🥐', 3),
(15, 'Ścieranie kurzy', '🤧', 4),
(16, 'Umycie muszli', '🐚', 3);


CREATE TABLE IF NOT EXISTS activity_records (
    id SERIAL PRIMARY KEY,
    activity_id INTEGER NOT NULL,
    user_id VARCHAR(13) NOT NULL,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

DROP TABLE IF EXISTS users;
CREATE TABLE users (
    id VARCHAR(13) PRIMARY KEY,
    access_token UUID NOT NULL,
    name VARCHAR(100) NOT NULL,
    image VARCHAR(100) NOT NULL,
    color VARCHAR(100) NOT NULL
);
INSERT INTO users (name, id, image, color, access_token) VALUES
('Marcin', 'A9A518D471361', 'cat-face.png', 'orange', 'ef1bc109-7495-4c2c-8307-3a0f9430603d'), 
('Julia', 'D3B6585C643A2', 'mouse-face.png', 'pink', '4a8eaa83-dbdf-4c8c-b340-cadb434d21ad');