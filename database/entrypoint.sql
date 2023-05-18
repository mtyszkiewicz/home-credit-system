DROP TABLE IF EXISTS activities;
CREATE TABLE activities (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    score INTEGER NOT NULL DEFAULT 0,
    description TEXT DEFAULT '',
    group_name VARCHAR(10) NOT NULL CHECK (group_name IN ('standard', 'extra', 'penalty')),
    cooldown_minutes INTEGER NOT NULL DEFAULT 1
);

INSERT INTO activities (name, score, group_name, cooldown_minutes) VALUES
('🍛 Wstawienie zmywarki', 2, 'standard', 60),
('🍽️ Rozładowanie zmywarki', 2, 'standard', 60),
('🧽 Umycie blatu w kuchni', 3, 'standard', 5),
('🗑️ Wyrzucenie śmieci', 2, 'standard', 1),
('🧺 Wstawienie pralki', 1, 'standard', 60),
('☀️ Powieszenie prania', 2, 'standard', 60),
('👔 Ubrania do szafy', 3, 'standard', 60);

INSERT INTO activities (name, score, group_name, cooldown_minutes) VALUES
('🚰 Umycie zlewu i kranu', 3, 'extra', 120),
('🧹 Udkurzenie domu', 3, 'extra', 1440),                     -- 1 day
('🧼 Umycie umywalki i szafki', 3, 'extra', 1440),            -- 1 day
('💩 Usunięcie kłaków z prysznica', 2, 'extra', 20160),       -- 2 weeks
('🪞 Umycie kabiny i lustra', 3, 'extra', 1440); -- 1 day

INSERT INTO activities (name, score, group_name, cooldown_minutes) VALUES
('🧦 Ubrania na ziemi (od sztuki)', -3, 'penalty', 1);


CREATE TABLE IF NOT EXISTS activities_log (
    id SERIAL PRIMARY KEY,
    activity_id INTEGER NOT NULL,
    user_id VARCHAR(13) NOT NULL,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

DROP TABLE users;
CREATE TABLE users (
    id VARCHAR(13) PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    image VARCHAR(255) NULL
);
INSERT INTO users (name, id, image) VALUES
('Marcin', 'A9A518D471361', 'cat-face.png'), ('Julia', 'D3B6585C643A2', 'mouse-face.png');