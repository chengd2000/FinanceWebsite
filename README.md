# Income and Outcome Management Web Application

This project is a Flask-based web application for managing income and outcomes. It allows users to track their financial activities effectively with features such as user authentication and password reset.

---

## Features

- **User Authentication:** Secure login system with hashed passwords.
- **Forgot Password:** Reset password functionality via a secure process.
- **Track Income and Outcome:** Add, view, and delete records for better financial management.
- **Interactive UI:** Responsive and user-friendly interface.

---

## Getting Started

### Prerequisites

Ensure you have the following installed on your system:

- Python 3.7 or later
- pip (Python package manager)

### Installation Steps

1. **Clone the Repository:**

   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. **Create a Virtual Environment (Optional but Recommended):**

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Upgrade Flask-SQLAlchemy:**

   To ensure compatibility, run the following command:

   ```bash
   pip install --upgrade Flask-SQLAlchemy
   ```

5. **Run the Application:**

   Use the `run.py` script to start the Flask application:

   ```bash
   python run.py
   ```

   The application will be accessible at `http://127.0.0.1:5000/`.

---

## Project Structure

```
project-folder/
├── app/
│   ├── __init__.py       # Application factory
│   ├── models.py         # Database models
│   ├── routes.py         # Application routes
│   └── templates/        # HTML templates
├── static/               # Static files (CSS, JS, images)
├── requirements.txt      # Python dependencies
├── run.py                # Application entry point
└── README.md             # Project documentation
```

---

## Usage Instructions

1. **Login/Register:** Create a user account or log in with an existing one.
2. **Add Transactions:** Use the dashboard to add income or expense records.
3. **View Records:** Track and manage your financial activities.
4. **Reset Password:** Use the "Forgot Password" option if you need to reset your credentials.

---

## License

This project is a private project and is protected under copyright laws. Unauthorized use, distribution, or modification of this code is strictly prohibited without prior written consent from the owner.

---

## Support

If you encounter any issues or have questions, please open an issue on the repository or contact the project maintainer.

