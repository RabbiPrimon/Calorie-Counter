# Calorie Counter App

A Django-based web application for tracking daily calorie consumption and managing personal health goals. Users can register, log in, set up their profile with BMR calculations, and add daily food consumptions to monitor their intake against their basal metabolic rate (BMR).

## Features

- **User Registration and Authentication**: Secure user registration with email verification, login, and logout functionality.
- **User Profile Management**: Users can update their profile including name, age, gender, height, weight, and role (user/admin).
- **BMR Calculation**: Automatic calculation of Basal Metabolic Rate based on user profile data.
- **Daily Consumption Tracking**: Add food items with quantity and calories, view daily totals, and compare against BMR.
- **Dashboard**: Visual dashboard showing BMR, consumed calories, today's consumptions table, and weight management guidelines.
- **Responsive Design**: Bootstrap-based UI with custom CSS for a modern, gradient-themed interface.
- **Role-Based Access**: Support for user and admin roles (admin can access Django admin panel).

## Technologies Used

- **Backend**: Django 5.2.7
- **Frontend**: HTML5, CSS3, Bootstrap 5, Font Awesome icons
- **Database**: SQLite (default, can be changed to PostgreSQL/MySQL for production)
- **Python Version**: 3.8+
- **Other Libraries**:
  - django-crispy-forms (for form rendering)
  - Font Awesome (for icons)

## Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment tool (recommended: venv)

### Setup Instructions

1. **Clone the Repository** (if applicable):
   ```
   git clone <repository-url>
   cd Rabbi_20_CalorieCounter
   ```

2. **Create and Activate Virtual Environment**:
   ```
   python -m venv env
   # On Windows:
   env\Scripts\activate
   # On macOS/Linux:
   source env/bin/activate
   ```

3. **Install Dependencies**:
   ```
   pip install -r requirements.txt
   ```

4. **Apply Database Migrations**:
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create Superuser** (optional, for admin access):
   ```
   python manage.py createsuperuser
   ```

6. **Run the Development Server**:
   ```
   python manage.py runserver
   ```

7. **Access the Application**:
   - Open your browser and go to `http://127.0.0.1:8000/`
   - Register a new account or login with existing credentials.

## Usage

### User Workflow

1. **Registration**: Visit the homepage and register with username, email, and password.
2. **Profile Setup**: After registration, set up your profile with personal details (age, gender, height, weight).
3. **Dashboard**: View your BMR, daily calorie consumption, and guidelines.
4. **Add Consumption**: Click "Add New Consumption" to log food items with quantity and calories.
5. **Track Progress**: Monitor your intake on the dashboard and adjust as needed.

### Admin Features

- Admins can access the Django admin panel at `/admin/` to manage users and data.
- Role-based login ensures only admins can access admin functions.

## Project Structure

```
Rabbi_20_CalorieCounter/
├── CalorieApp/                    # Main Django app
│   ├── __init__.py
│   ├── admin.py                   # Django admin configuration
│   ├── apps.py
│   ├── forms.py                   # Django forms (UserRegisterForm, UserProfileForm, DailyConsumptionForm)
│   ├── models.py                  # Database models (UserProfile, DailyConsumption)
│   ├── tests.py                   # Unit tests
│   ├── urls.py                    # App URL patterns
│   └── views.py                   # View functions (register, login, dashboard, etc.)
├── Rabbi_20_CalorieCounter/       # Django project settings
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py                # Project settings (database, installed apps, etc.)
│   ├── urls.py                    # Root URL patterns
│   └── wsgi.py
├── static/                        # Static files (CSS, JS, images)
│   └── css/
│       └── style.css              # Custom CSS styles
├── templates/                     # HTML templates
│   ├── base.html                  # Base template with navbar and layout
│   ├── register.html              # User registration form
│   ├── login.html                 # User login form
│   ├── profile.html               # User profile update form
│   ├── dashboard.html             # Main dashboard with BMR and consumptions
│   ├── add_consumption.html       # Form to add daily consumption
│   └── profile.html               # User profile template
├── db.sqlite3                     # SQLite database file
├── manage.py                      # Django management script
├── requirements.txt               # Python dependencies
└── README.md                      # This file
```

## Models

### UserProfile
- Extends Django's User model with additional fields:
  - `name`: CharField (optional)
  - `age`: IntegerField (optional)
  - `gender`: CharField (choices: Male/Female)
  - `height`: FloatField (in cm)
  - `weight`: FloatField (in kg)
  - `role`: CharField (choices: user/admin, default: user)

### DailyConsumption
- Tracks user's daily food intake:
  - `user`: ForeignKey to User
  - `item_name`: CharField (food item name)
  - `quantity`: CharField (quantity description, e.g., "1 cup", "2 pieces")
  - `calories`: IntegerField (calories for the item)
  - `date`: DateField (auto-set to current date)

## Views

- `register(request)`: Handles user registration with form validation.
- `login_view(request)`: Authenticates users with role-based access.
- `profile(request)`: Allows users to update their profile.
- `dashboard(request)`: Displays BMR, consumed calories, and today's consumptions.
- `add_consumption(request)`: Form to add new daily consumption entries.
- `logout_view(request)`: Logs out the user.

## Forms

- `UserRegisterForm`: Extends UserCreationForm with email field.
- `UserProfileForm`: ModelForm for UserProfile.
- `DailyConsumptionForm`: ModelForm for DailyConsumption with custom widgets.

## Templates

- **base.html**: Includes Bootstrap CSS, Font Awesome, custom CSS, and navbar with login/register buttons.
- **dashboard.html**: Shows BMR, consumed calories, consumptions table, and guidelines.
- **add_consumption.html**: Form for adding food consumption with blue labels.
- Other templates for authentication and profile management.

## CSS Styling

- Custom gradient background animation.
- Card-based layout with shadows and hover effects.
- Primary color: Blue (#007bff) for labels and accents.
- Responsive design for mobile and desktop.

## Database Migrations

- Initial migration: Creates UserProfile and DailyConsumption tables.
- Subsequent migrations: Add quantity field to DailyConsumption.

## Testing

Run tests with:
```
python manage.py test
```

Current tests are basic; expand as needed for comprehensive coverage.

## Deployment

For production deployment:

1. Set `DEBUG = False` in settings.py.
2. Configure a production database (e.g., PostgreSQL).
3. Use a WSGI server like Gunicorn.
4. Serve static files with a web server like Nginx.
5. Set environment variables for secrets (SECRET_KEY, database credentials).

## Contributing

1. Fork the repository.
2. Create a feature branch.
3. Make changes and test thoroughly.
4. Submit a pull request.

## License

This project is licensed under the MIT License. See LICENSE file for details.

## Contact

📫 Connect

- **Portfolio**: [rabbi.crsyndicate.info](https://rabbi.crsyndicate.info)
- **Email**: rabbiprimon00000@gmail.com
- **LinkedIn**: [/in/md-rabbi-islam-747770231/](https://linkedin.com/in/md-rabbi-islam-747770231/)
- **Phone**: +8801644358765

For questions or support, feel free to reach out via email or LinkedIn.

