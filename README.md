# E-Commerce Store

This is a Django-based e-commerce application that allows users to browse products, add them to a cart, and complete the checkout process.

## Prerequisites

- Python 3.10 or higher
- pip (Python package installer)

## Setup Instructions

1. **Clone the repository:**

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Create a virtual environment:**

   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment:**

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On macOS/Linux:

     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

5. **Set up environment variables:**

   Create a `.env` file in the project root and add the following variables:

   ```
   SECRET_KEY=your_secret_key
   DEBUG=True
   ALLOWED_HOSTS=localhost,127.0.0.1
   ```

6. **Run migrations:**

   ```bash
   python manage.py migrate
   ```

7. **Create a superuser:**

   ```bash
   python manage.py createsuperuser
   ```

8. **Load initial data (optional):**

   ```bash
   python manage.py loaddata products/fixtures/initial_data.json
   ```

## Running the Project

1. **Start the development server:**

   ```bash
   python manage.py runserver
   ```

2. **Access the application:**

   Open your web browser and go to `http://127.0.0.1:8000/`.

## Features

- User registration and authentication
- Product browsing and searching
- Shopping cart functionality
- Checkout process
- Order history

## Contributing

1. Fork the repository.
2. Create a new branch for your feature.
3. Commit your changes.
4. Push to the branch.
5. Create a new Pull Request.

## License

This project is licensed under the MIT License. 