DROP TABLE IF EXISTS activities;
CREATE TABLE activities (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    icon VARCHAR(10) NOT NULL,
    value INTEGER NOT NULL DEFAULT 0,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL
);

INSERT INTO activities (id, start_date, end_date, icon, value, name) VALUES
(1,  '2023-01-01', '9999-12-31', '🧆', 2, 'Wstawienie zmywarki'),
(2,  '2023-01-01', '9999-12-31', '🍽️', 2, 'Rozładowanie zmywarki'),
(3,  '2023-01-01', '9999-12-31', '🧽', 3, 'Umycie blatu w kuchni'),
(4,  '2023-01-01', '9999-12-31', '🗑️', 2, 'Wyrzucenie śmieci'),
(5,  '2023-01-01', '9999-12-31', '🧺', 2, 'Wstawienie pralki'),
(6,  '2023-01-01', '9999-12-31', '☀️', 2,  'Powieszenie prania'),
(7,  '2023-01-01', '9999-12-31', '👔', 3, 'Ubrania do szafy'),
(8,  '2023-01-01', '9999-12-31', '🚰', 3, 'Umycie zlewu'),
(9,  '2023-01-01', '9999-12-31', '🌪️', 5, 'Odkurzenie domu'),
(10, '2023-01-01', '9999-12-31', '🪥', 3, 'Umycie umywalki'),
(11, '2023-01-01', '9999-12-31', '💩', 3, 'Usunięcie owłosienia'),
(12, '2023-01-01', '9999-12-31', '🚿', 5, 'Umycie kabiny prysznicowej'),
(14, '2023-01-01', '9999-12-31', '🥐', 3, 'Zakupy'),
(15, '2023-01-01', '9999-12-31', '🤧', 4, 'Ścieranie kurzy'),
(16, '2023-01-01', '9999-12-31', '🐚', 3, 'Umycie muszli');


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