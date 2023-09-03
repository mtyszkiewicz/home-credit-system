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
