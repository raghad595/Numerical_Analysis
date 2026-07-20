# Numerical Analysis Web Application

A Python-based web application built with the Django framework to demonstrate and compute various numerical analysis methods. The project is modularized into distinct chapters, separating the core mathematical logic from the web interface.

## 🏗️ Project Structure

The repository follows a standard Django project architecture with a primary application named `numeric`. 

### Core Application (`/numeric`)
*   **Numerical Logic Modules:** The mathematical algorithms are separated into standalone Python scripts for maintainability:
    *   `ch1.py`: Computations and logic for Chapter 1.
    *   `ch2.py`: Computations and logic for Chapter 2[cite: 10].
    *   `ch3.py`: Computations and logic for Chapter 3[cite: 10].
*   **Django MVC Components:**
    *   `views.py`: Handles HTTP requests and connects the numerical logic to the user interface[cite: 10].
    *   `models.py` & `admin.py`: Database schema definitions and admin panel configurations[cite: 10].
    *   `urls.py`: URL routing specific to the numerical analysis tools[cite: 10].
*   **Custom Template Tags:** Includes `custom_tags.py` within the `templatetags` directory for advanced rendering logic inside HTML files[cite: 10].

### Frontend Assets
*   **Templates (`/templates/numeric/`):** Contains the HTML views for the application, including a main `index.html` and dedicated pages for each chapter (`ch1.html`, `ch2.html`, `ch3.html`)[cite: 10].
*   **Static Files (`/static/numeric/`):** Houses the CSS stylesheets (`chs.css`, `stylesheet.css`) and UI image assets required for the frontend[cite: 10].

### Database
*   **`db.sqlite3`:** The default local SQLite database storing application states and potential user queries[cite: 10].

## 🚀 Installation & Setup

Follow these steps to run the numerical analysis application locally.

### 1. Prerequisites
Ensure you have Python 3.x installed on your machine. It is highly recommended to use a virtual environment.

### 2. Clone and Setup Environment
Clone the repository and navigate into the root directory containing `manage.py`[cite: 10].

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
