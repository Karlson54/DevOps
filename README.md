# MyBlog - Django Blog Application

A simple blog application built with Django as part of DevOps practical work.

## Features

- Post listing with pagination
- Post detail view with SEO-friendly URLs
- Email post sharing
- Comments system
- Admin panel for content management

## Installation

1. Clone the repository
2. Create virtual environment:
```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
```
3. Install dependencies:
```bash
   pip install -r requirements.txt
```
4. Run migrations:
```bash
   python manage.py migrate
```
5. Create superuser:
```bash
   python manage.py createsuperuser
```
6. Create sample posts (optional):
```bash
   python manage.py create_sample_posts
```
7. Run development server:
```bash
   python manage.py runserver
```

## Usage

- Visit `http://127.0.0.1:8000/` for blog posts
- Visit `http://127.0.0.1:8000/admin/` for admin panel

## Project Structure

- `blog/` - Main blog application
- `myblog/` - Project settings
- `templates/` - HTML templates
- `static/` - CSS and static files