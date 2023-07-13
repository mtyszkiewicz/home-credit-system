CREATE SCHEMA IF NOT EXISTS raw AUTHORIZATION CURRENT_USER;

CREATE TABLE IF NOT EXISTS raw.activities (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    icon VARCHAR(10) NOT NULL,
    value INTEGER NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL
);

TRUNCATE TABLE raw.activities RESTART IDENTITY;
INSERT INTO raw.activities (id, start_date, end_date, icon, value, name) VALUES
(1,  '2023-01-01', '9999-12-31', '🧆', 2, 'Wstawienie zmywarki'),
(2,  '2023-01-01', '9999-12-31', '🍽️', 2, 'Rozładowanie zmywarki'),
(3,  '2023-01-01', '9999-12-31', '🧽', 3, 'Umycie blatu w kuchni'),
(4,  '2023-01-01', '9999-12-31', '🗑️', 2, 'Wyrzucenie śmieci'),
(5,  '2023-01-01', '2023-07-11', '🧺', 2, 'Wstawienie pralki'),
(6,  '2023-01-01', '9999-12-31', '☀️', 2,  'Powieszenie prania'),
(7,  '2023-01-01', '2023-07-11', '👔', 3, 'Ubrania do szafy'),
(8,  '2023-01-01', '9999-12-31', '🚰', 3, 'Umycie zlewu'),
(9,  '2023-01-01', '9999-12-31', '🌪️', 5, 'Odkurzenie domu'),
(10, '2023-01-01', '9999-12-31', '🪥', 3, 'Umycie umywalki'),
(11, '2023-01-01', '9999-12-31', '💩', 3, 'Usunięcie owłosienia'),
(12, '2023-01-01', '9999-12-31', '🚿', 5, 'Umycie kabiny prysznicowej'),
(14, '2023-01-01', '2023-07-11', '🥐', 3, 'Zakupy'),
(15, '2023-01-01', '9999-12-31', '🤧', 4, 'Ścieranie kurzy'),
(16, '2023-01-01', '9999-12-31', '🐚', 3, 'Umycie muszli'),
(17, '2023-07-12', '9999-12-31', '🧺', 4, 'Wstawienie pralki'),
(18, '2023-07-12', '9999-12-31', '👔', 4, 'Ubrania do szafy'),
(19, '2023-07-12', '9999-12-31', '🥐', 4, 'Zakupy');

CREATE TABLE IF NOT EXISTS raw.activity_records (
    id SERIAL PRIMARY KEY,
    activity_icon VARCHAR(10) NOT NULL,
    user_id INTEGER NOT NULL,
    create_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS raw.users (
    id INTEGER PRIMARY KEY,
    access_token UUID NOT NULL,
    name VARCHAR(100) NOT NULL,
    image VARCHAR(100) NOT NULL,
    color VARCHAR(100) NOT NULL
);

TRUNCATE TABLE raw.users RESTART IDENTITY;
INSERT INTO raw.users (name, id, image, color, access_token) VALUES
('Marcin', 1, 'cat-face.png', 'orange', 'ef1bc109-7495-4c2c-8307-3a0f9430603d'), 
('Julia',  2, 'mouse-face.png', 'pink', '4a8eaa83-dbdf-4c8c-b340-cadb434d21ad');