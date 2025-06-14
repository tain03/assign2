# Django E-Commerce Store

A full-featured e-commerce application built with Django.

## Features

- User authentication and profile management
- Product catalog with categories
- Shopping cart functionality
- Order management
- Responsive design using Bootstrap

## Setup Instructions

1. Create a virtual environment:
```bash
python -m venv venv
```

2. Activate the virtual environment:
- Windows:
```bash
venv\Scripts\activate
```
- Linux/Mac:
```bash
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a .env file in the project root with the following content:
```
DEBUG=True
SECRET_KEY=your-secret-key-here
```

5. Run migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

6. Create a superuser:
```bash
python manage.py createsuperuser
```

7. Run the development server:
```bash
python manage.py runserver
```

8. Access the application at http://127.0.0.1:8000/

## Admin Interface

Access the admin interface at http://127.0.0.1:8000/admin/ using your superuser credentials.

## Project Structure

- `core/`: Core application with home page and base templates
- `users/`: User authentication and profile management
- `products/`: Product catalog and management
- `cart/`: Shopping cart functionality
- `orders/`: Order processing and management

## Development

- The application uses Django 5.0.2
- Frontend is built with Bootstrap 5
- Forms are styled using django-crispy-forms
- Image handling is done with Pillow 