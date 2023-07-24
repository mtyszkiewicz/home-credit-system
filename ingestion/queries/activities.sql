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
(6,  '2023-01-01', '9999-12-31', '☀️', 2,  'Rozwieszenie prania'),
(7,  '2023-01-01', '2023-07-11', '👔', 3, 'Ubrania do szafy'),
(8,  '2023-01-01', '9999-12-31', '🚰', 3, 'Umycie zlewu w kuchni'),
(9,  '2023-01-01', '9999-12-31', '🌪️', 5, 'Odkurzenie domu'),
(10, '2023-01-01', '9999-12-31', '🪥', 3, 'Umycie umywalki'),
(11, '2023-01-01', '9999-12-31', '💩', 4, 'Odetkanie odpływu w kabinie prysznicowej'),
(12, '2023-01-01', '9999-12-31', '🚿', 5, 'Umycie kabiny prysznicowej'),
(14, '2023-01-01', '2023-07-11', '🥐', 3, 'Zakupy'),
(15, '2023-01-01', '9999-12-31', '🤧', 4, 'Starcie kurzy w salonie'),
(16, '2023-01-01', '9999-12-31', '🐚', 3, 'Umycie muszli'),
(17, '2023-07-12', '9999-12-31', '🧺', 4, 'Wstawienie pralki'),
(18, '2023-07-12', '9999-12-31', '👔', 4, 'Ubrania do szafy'),
(19, '2023-07-12', '9999-12-31', '🥐', 4, 'Zakupy'),
(20, '2023-01-01', '9999-12-31', '🦠', 6, 'Odetkanie odpływu w umywalce'),
(21, '2023-01-01', '9999-12-31', '🫧', 5, 'Umycie podłogi w salonie');
