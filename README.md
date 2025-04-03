# InjurySupport (Solution Challenge 2025)

## About the Project
InjurySupport is a Django-based web application designed to help users track injuries, symptoms, and recovery progress. It also integrates AI (Gemini API) to provide personalized recovery suggestions.

## Features
- Log injury history and current symptoms.
- Track sleep quality, medication intake, and recovery progress.
- AI-generated recovery suggestions based on user data.
- User authentication (login, signup, logout).

## Tech Stack
- **Backend**: Django, SQLite
- **Frontend**: HTML, CSS
- **AI Integration**: Google Gemini API
- **Deployment**: PythonAnywhere

## Setup Instructions
1. Clone the repository: git clone https://github.com/s-k-y-7/SolutionChallenge25.git
2. Navigate to the project directory: cd SolutionChallenge25
3. Create and activate a virtual environment: python -m venv env source env/bin/activate (Linux/macOS) env\Scripts\activate (Windows)
4. Install dependencies: pip install -r requirements.txt
5. Apply migrations: python manage.py migrate
6. Create a superuser: python manage.py createsuperuser
7. Run the server: python manage.py runserver

