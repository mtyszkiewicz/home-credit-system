-- DROP TABLE IF EXISTS activities;
-- CREATE TABLE activities (
--     id SERIAL PRIMARY KEY,
--     name VARCHAR(255) NOT NULL,
--     icon VARCHAR(10) NOT NULL,
--     value INTEGER NOT NULL DEFAULT 0,
--     requirements TEXT ARRAY DEFAULT '{}'
--     -- group_name VARCHAR(10) NOT NULL CHECK (group_name IN ('standard', 'extra', 'penalty')),
--     -- cooldown_minutes INTEGER NOT NULL DEFAULT 1
-- );

-- INSERT INTO activities (id, name, icon, value, requirements) VALUES
-- (1, 'Wstawienie zmywarki', '🧆', 2, '{}'),
-- (2, 'Rozładowanie zmywarki', '🍽️', 2, '{}'),
-- (3, 'Umycie blatu w kuchni', '🧽', 3, '{"Cała powierzchnia włącznie z przestrzenią pod kawiarką i czajnikiem"}'),
-- (4, 'Wyrzucenie śmieci', '🗑️', 2, '{"Do opróżnionego kubła włóż nowy worek na śmieci"}'),
-- (5, 'Wstawienie pralki', '🧺', 2, '{"Wszystkie ubrania na drugą stronę.", "Pełny bęben = 2 kapsułki"}'),
-- (6, 'Powieszenie prania', '☀️', 2, '{}'),
-- (7, 'Ubrania do szafy', '👔', 3, '{}'),
-- (8, 'Umycie zlewu', '🚰', 3, '{"Umycie zlewu i kranu"}'),
-- (9, 'Odkurzenie domu', '🌪️', 5, '{"Każde pomieszczenie (pod łóżkiem, za firankami, za śmietnikiem, pod muszlą klozetową i bidetem)"}'),
-- (10, 'Umycie umywalki', '🪥', 3, '{"Umycie umywalki", "Umycie lustra", "Przetarcie szafki na kosmetyki"}'),
-- (11, 'Usunięcie owłosienia', '💩', 3, '{"Po wyciągnięciu centralnej plastikowej części usunąć materiał nagromadzony wewnątrz (on głównie blokuje przepływ)", "Umyć całą nasadę"}'),
-- (12, 'Umycie kabiny prysznicowej', '🚿', 5, '{"Usunięcie brudu pod płynami", "Umycie szyb"}'),
-- (14, 'Zakupy', '🥐', 3, '{}'),
-- (15, 'Ścieranie kurzy', '🤧', 4, '{"Szafka RTV (włącznie z przestrzenią pod subwooferem i gramofonem)", "Parapety przy stole jadalnianym", "Stolik kawowy", "Spód szafki w wiatrołapie"}'),
-- (16, 'Umycie muszli', '🐚', 3, '{"Ponad i poniżej poziomu wody", "Deska sedesowa (powierzchnia i spód)", "Przestrzeń pod deską"}');


-- CREATE TABLE IF NOT EXISTS activity_records (
--     id SERIAL PRIMARY KEY,
--     activity_id INTEGER NOT NULL,
--     user_id VARCHAR(13) NOT NULL,
--     timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
-- );

-- DROP TABLE IF EXISTS users;
-- CREATE TABLE users (
--     id VARCHAR(13) PRIMARY KEY,
--     name VARCHAR(100) NOT NULL,
--     image VARCHAR(100) NOT NULL,
--     color VARCHAR(100) NOT NULL
-- );
-- INSERT INTO users (name, id, image, color) VALUES
-- ('Marcin', 'A9A518D471361', 'cat-face.png', 'orange'), 
-- ('Julia', 'D3B6585C643A2', 'mouse-face.png', 'pink');

DROP TABLE IF EXISTS users;
CREATE TABLE users (
	  id SERIAL PRIMARY KEY,
	  access_token UUID NOT NULL,
	  name VARCHAR(30) NOT NULL,
	  image VARCHAR(30) NOT NULL,
	  color VARCHAR(30) NOT NULL
);

INSERT INTO users (name, image, color, access_token) VALUES
('Marcin', 'cat-face.png', 'orange', '622a1c86-522d-4e49-9c24-1d217db06dce'),
('Julia', 'mouse-face.png', 'pink', 'a01c51aa-41bf-4ae7-a63c-ffa732f5b38e');

CREATE TABLE IF NOT EXISTS activity_records (
	id SERIAL PRIMARY KEY,
    activity_id INTEGER NOT NULL,
    user_id INTEGER NOT NULL,
    create_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)

CREATE TABLE activities (
    id SERIAL PRIMARY KEY,
	activity_code VARCHAR(50) NOT NULL,
    name VARCHAR(255) NOT NULL,
    icon VARCHAR(10) NOT NULL,
    value INTEGER NOT NULL,
    start_date TIMESTAMP NOT NULL,
	end_date TIMESTAMP NOT NULL DEFAULT '9999-12-31 00:00:00.000'
);

INSERT INTO activities (activity_code, start_date, end_date, name, icon, value) VALUES
    (1, '2023-01-01', '9999-12-31', 'Wstawienie zmywarki', '🧆', 2),
    (2, '2023-01-01', '9999-12-31', 'Rozładowanie zmywarki', '🍽️', 2),
    (3, '2023-01-01', '9999-12-31', 'Umycie blatu w kuchni', '🧽', 3),
    (4, '2023-01-01', '9999-12-31', 'Wyrzucenie śmieci', '🗑️', 2),
    (5, '2023-01-01', '9999-12-31', 'Wstawienie pralki', '🧺', 2),
    (6, '2023-01-01', '9999-12-31', 'Powieszenie prania', '☀️', 2),
    (7, '2023-01-01', '9999-12-31', 'Ubrania do szafy', '👔', 3),
    (8, '2023-01-01', '9999-12-31', 'Umycie zlewu', '🚰', 3),
    (9, '2023-01-01', '9999-12-31', 'Odkurzenie domu', '🌪️', 5),
    (10, '2023-01-01', '9999-12-31', 'Umycie umywalki', '🪥', 3),
    (11, '2023-01-01', '9999-12-31', 'Usunięcie owłosienia', '💩', 3),
    (12, '2023-01-01', '9999-12-31', 'Umycie kabiny prysznicowej', '🚿', 5),
    (14, '2023-01-01', '9999-12-31', 'Zakupy', '🥐', 3),
    (15, '2023-01-01', '9999-12-31', 'Ścieranie kurzy', '🤧', 4),
    (16, '2023-01-01', '9999-12-31', 'Umycie muszli', '🐚', 3);