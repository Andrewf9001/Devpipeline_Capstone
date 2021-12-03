CREATE TABLE IF NOT EXISTS Users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT,
    phone TEXT,
    email TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    active INTEGER DEFAULT 1,
    date_created TEXT,
    hire_date TEXT,
    user_type TEXT
);

CREATE TABLE IF NOT EXISTS Assessments (
    assessment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    date_created TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS Competencies (
    comp_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    assessment_id INTEGER,
    name TEXT NOT NULL,
    FOREIGN KEY (user_id)
        REFERENCES Users (user_id),
    FOREIGN KEY (assessment_id)
        REFERENCES Assessments (assessment_id)
);

CREATE TABLE IF NOT EXISTS AssessmentResults (
    user_id INTEGER NOT NULL,
    comp_id INTEGER NOT NULL,
    score INTEGER DEFAULT 0,
    date_taken TEXT NOT NULL,
    manager TEXT,
    PRIMARY KEY(student_id, cohort_id),
    FOREIGN KEY (student_id)
    REFERENCES People (person_id),
    FOREIGN KEY (cohort_id)
    REFERENCES Cohort (cohort_id)
);