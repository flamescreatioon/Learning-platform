CREATE DATABASE course_recommendation;
USE course_recommendation;

CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    course VARCHAR(255),
    class_level VARCHAR(50),
    field VARCHAR(255),
    gpa FLOAT
    cgpa FLOAT
);

CREATE TABLE courses (
    id INT AUTO_INCREMENT PRIMARY KEY,
    course_name VARCHAR(255),
    field VARCHAR(255),
    difficulty_level ENUM('Beginner', 'Intermediate', 'Advanced'),
);

CREATE TABLE materials (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255),
    course_id INT,
    material_type ENUM('Video', 'Article', 'Book'),
    difficulty_level ENUM('Beginner', 'Intermediate', 'Advanced'),
    FOREIGN KEY (course_id) REFERENCES courses(id)
);
