CREATE TABLE IF NOT EXISTS Users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT,
    phone TEXT,
    email TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    user_type TEXT DEFAULT 'User',
    date_created TEXT,
    hire_date TEXT,
    active INTEGER DEFAULT 1
);

CREATE TABLE IF NOT EXISTS Compentencies (
    comp_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    date_created TEXT
);

CREATE TABLE IF NOT EXISTS Assessments (
    assessment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    comp_id INTEGER,
    name TEXT NOT NULL,
    date_created TEXT NOT NULL,
    FOREIGN KEY (comp_id)
        REFERENCES Competencies (comp_id)
);

CREATE TABLE IF NOT EXISTS AssessmentResults (
    user_id INTEGER NOT NULL,
    comp_id INTEGER NOT NULL,
    score INTEGER DEFAULT 0,
    date_taken TEXT NOT NULL,
    manager TEXT,
    PRIMARY KEY(user_id, comp_id),
    FOREIGN KEY (user_id)
        REFERENCES Users (user_id),
    FOREIGN KEY (comp_id)
        REFERENCES Competencies (comp_id)
);

