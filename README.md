# EduAssist

EduAssist is a comprehensive web-based application designed to enhance the learning experience for students by integrating educational tools like note-taking, task management ,and providing access to curated study materials through a single platform.

---

## Table of Contents
1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)

---

## Project Overview

EduAssist serves as an all-in-one educational assistant that empowers students by providing:
- Task and schedule management.
- Organized note-taking functionality.
- Curated study materials to support self-study.
- A user-friendly interface tailored to student needs.

---

## Features

- **Task Management:**
  - Create, edit, and delete tasks.
  - Set deadlines.
- **Note Taking:**
  - Create, edit, and delete notes.
  - Search functionality for quick access.
- **Study Materials:**
  - Filter materials through category.
  - Supports PDF and other file formats.
- **User Profile:**
  - Update profile and manage preferences.

---

## Installation

### Prerequisites
- Python 3.11.5
- Django 4.2.2
- Virtual Environment Tool (`venv`)

### Steps
1. Clone the repository:
   ```bash
   git clone git@github.com:Dipshina/EDUASSIST.git

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate     # For Windows

3. Install dependencies:
    ```bash
    pip install -r requirements.txt

4. Apply migrations:
    ```bash
    python manage.py makemigrations
    python manage.py migrate

5. Run the development server:
    ```bash
    python manage.py runserver

6. Open the app in your browser at http://127.0.0.1:8000/.

---

## Usage
1. Register and log in to access the platform.
2. Use the To-Do feature to manage tasks with deadlines and priorities.
3. Create and organize notes for study purposes.
4. Search and access provided files via Study Materials.
