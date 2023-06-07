DROP TABLE IF EXISTS activities;
CREATE TABLE activities (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    icon VARCHAR(10) NOT NULL,
    value INTEGER NOT NULL DEFAULT 0,
    description TEXT DEFAULT ''
    -- group_name VARCHAR(10) NOT NULL CHECK (group_name IN ('standard', 'extra', 'penalty')),
    -- cooldown_minutes INTEGER NOT NULL DEFAULT 1
);

INSERT INTO activities (name, icon, value) VALUES
('Wstawienie zmywarki', '🍛', 2),
('Rozładowanie zmywarki', '🍽️', 2),
('Umycie blatu w kuchni', '🧽', 3),
('Wyrzucenie śmieci', '🗑️', 2),
('Wstawienie pralki', '🧺', 2),
('Powieszenie prania', '☀️', 2),
('Ubrania do szafy', '👔', 3),
('Umycie zlewu', '🚰', 3),
('Odkurzenie domu', '🌪️', 5),
('Umycie umywalki', '🧼', 3),
('Usunięcie owłosienia', '💩', 2),
('Umycie kabiny prysznicowej', '🚿', 5),
('Ubrania na ziemi', '🧦', -3),
('Zakupy', '🥐', 3),
('Ścieranie kurzy', '🤧', 4);

CREATE TABLE IF NOT EXISTS activity_records (
    id SERIAL PRIMARY KEY,
    activity_id INTEGER NOT NULL,
    user_id VARCHAR(13) NOT NULL,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

DROP TABLE IF EXISTS users;
CREATE TABLE users (
    id VARCHAR(13) PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    image VARCHAR(100) NOT NULL,
    color VARCHAR(100) NOT NULL
);
INSERT INTO users (name, id, image, color) VALUES
('Marcin', 'A9A518D471361', 'cat-face.png', 'orange'), 
('Julia', 'D3B6585C643A2', 'mouse-face.png', 'pink');