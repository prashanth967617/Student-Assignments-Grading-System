
# Student Assignment Management System

This project is a backend application for managing student assignments, grades, and teacher interactions. It allows principals to manage teachers and assignments, while students can create and submit their assignments.

## Features

- **Principal Management**:
  - View all teachers.
  - List all submitted and graded assignments.
  - Re-grade assignments already graded by teachers.

- **Student Management**:
  - Create and edit draft assignments.
  - List all created assignments.
  - Submit draft assignments to teachers.

- **Teacher Management**:
  - List assignments submitted to him.
  - Grade assignments submitted to him.

## Technologies

- Python
- Flask
- SQLAlchemy
- SQLite (for development)
- pytest (for testing)

## API Endpoints

### Principal Endpoints

#### 1. GET /principal/assignments

**Description**: Retrieve all submitted and graded assignments.

**Request Header**:

**Response**:
```json
{
    "data": [
        {
            "id": 1,
            "content": "ESSAY T1",
            "created_at": "2021-09-17T03:14:01.580126",
            "grade": "A",
            "state": "GRADED",
            "student_id": 1,
            "teacher_id": 1,
            "updated_at": "2021-09-17T03:20:42.896947"
        }
    ]
}
GET /principal/teachers
Description: Retrieve all teachers.

Request Header:
X-Principal: {"user_id": 5, "principal_id": 1}
Response:
{
    "data": [
        {
            "id": 1,
            "created_at": "2024-01-08T07:58:53.131970",
            "updated_at": "2024-01-08T07:58:53.131972",
            "user_id": 3
        }
    ]
}
POST /principal/assignments/grade

Description: Grade or re-grade an assignment.

Request Header:

X-Principal: {"user_id": 5, "principal_id": 1}

Request Body:

{
    "id": 1,
    "grade": "A"
}
Response:
{
    "data": {
        "id": 1,
        "content": "ESSAY T1",
        "created_at": "2021-09-17T03:14:01.580126",
        "grade": "A",
        "state": "GRADED",
        "student_id": 1,
        "teacher_id": 1,
        "updated_at": "2021-09-17T03:20:42.896947"
    }
}

