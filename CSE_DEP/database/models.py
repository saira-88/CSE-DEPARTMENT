import sqlite3

def create_tables():
    conn = sqlite3.connect("exam_system.db")
    cursor = conn.cursor()

    # Academic DB
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Students (
        student_id INTEGER PRIMARY KEY,
        name TEXT,
        department TEXT,
        class TEXT,
        email TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Subjects (
        subject_id INTEGER PRIMARY KEY,
        subject_name TEXT,
        department TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Enrollments (
        student_id INTEGER,
        subject_id INTEGER,
        FOREIGN KEY(student_id) REFERENCES Students(student_id),
        FOREIGN KEY(subject_id) REFERENCES Subjects(subject_id)
    )
    """)

    # Infrastructure DB
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Exam_Halls (
        hall_id INTEGER PRIMARY KEY,
        capacity INTEGER,
        cctv_status TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Hall_Blueprint (
        hall_id INTEGER,
        row INTEGER,
        column INTEGER,
        seat_id TEXT,
        FOREIGN KEY(hall_id) REFERENCES Exam_Halls(hall_id)
    )
    """)

    # Logistics & Security DB
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Incidents (
        student_id INTEGER,
        exam_id INTEGER,
        description TEXT,
        status TEXT
    )
    """)

    conn.commit()
    conn.close()
    print("All tables created successfully!")
