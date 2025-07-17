# Django Todo App

A full-featured todo application built with Django REST Framework and a modern HTML/CSS/JavaScript frontend.

## Features

- User authentication (register/login)
- Create, read, update, and delete todos
- Mark todos as complete/incomplete
- Priority levels (High, Medium, Low)
- Due dates for todos
- Filter todos by status (All, Pending, Completed)
- Responsive web interface
- Admin interface for managing todos

## Installation

1. **Clone the repository**
   ```bash
   cd /Users/TPL/projects/web-apps/dj-ng/backend
   ```

2. **Activate virtual environment**
   ```bash
   source venv/bin/activate
   ```

3. **Install dependencies** (already installed)
   - Django
   - Django REST Framework
   - django-cors-headers

4. **Run migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create sample data** (optional)
   ```bash
   python manage.py create_sample_data
   ```

## Usage

### Start the development server
```bash
python manage.py runserver
```

### Access the application
- **Frontend:** http://localhost:8000
- **Admin Panel:** http://localhost:8000/admin
- **API Documentation:** http://localhost:8000/api/todos/

### Login Credentials
- **Admin:** username: `admin`, password: `admin123`
- **Test User:** username: `testuser`, password: `testpass123`

## API Endpoints

### Authentication
- `POST /api/auth/register/` - Register a new user
- `POST /api/auth/login/` - Login user

### Todos
- `GET /api/todos/` - List all todos for authenticated user
- `POST /api/todos/` - Create a new todo
- `GET /api/todos/{id}/` - Get a specific todo
- `PUT /api/todos/{id}/` - Update a todo
- `DELETE /api/todos/{id}/` - Delete a todo
- `POST /api/todos/{id}/toggle_complete/` - Toggle completion status
- `GET /api/todos/completed/` - Get completed todos
- `GET /api/todos/pending/` - Get pending todos

## Frontend Features

- **Authentication Form:** Register and login functionality
- **Todo Creation:** Add new todos with title, description, priority, and due date
- **Todo Management:** View, complete, and delete todos
- **Filtering:** Filter todos by status (All, Pending, Completed)
- **Responsive Design:** Works on desktop and mobile devices
- **Priority Indicators:** Visual indicators for different priority levels

## Project Structure

```
backend/
├── manage.py
├── db.sqlite3
├── static/
│   └── index.html          # Frontend HTML file
├── backend/
│   ├── __init__.py
│   ├── settings.py         # Django settings
│   ├── urls.py            # Main URL configuration
│   └── wsgi.py
└── todo/
    ├── __init__.py
    ├── admin.py           # Admin configuration
    ├── apps.py
    ├── models.py          # Todo model
    ├── serializers.py     # API serializers
    ├── views.py           # API views
    ├── urls.py            # Todo URL patterns
    ├── migrations/
    └── management/
        └── commands/
            └── create_sample_data.py
```

## Technologies Used

- **Backend:** Django 5.2.4, Django REST Framework
- **Database:** SQLite
- **Frontend:** HTML5, CSS3, JavaScript (ES6+)
- **Authentication:** Django built-in authentication
- **CORS:** django-cors-headers for cross-origin requests

## Development Notes

- The app uses Django's built-in authentication system
- CORS is configured to allow requests from common frontend development ports
- The frontend is a single-page application with no build process required
- All API endpoints require authentication except registration and login
- The admin interface provides full CRUD operations for todos

## Future Enhancements

- Add categories/tags for todos
- Implement search functionality
- Add file attachments to todos
- Email notifications for due dates
- Collaborative todos (sharing between users)
- REST API pagination for large datasets
- Progressive Web App (PWA) features
