# MyBlog - Django Blog Application

A fully-featured blog application built with Django as part of DevOps practical work (Practical Work #6 & #7).

## Features

### Core Features (Practical Work #6)
- ✅ Post listing with pagination (3 posts per page)
- ✅ Post detail view with SEO-friendly URLs (year/month/day/slug)
- ✅ Email post sharing functionality
- ✅ Comments system with moderation
- ✅ Admin panel for content management
- ✅ Post status management (Draft/Published)

### Extended Features (Practical Work #7)
- ✅ **Tagging system** - Classify posts with keywords using django-taggit
- ✅ **Tag filtering** - Filter posts by specific tags
- ✅ **Similar posts** - Recommend related posts based on shared tags
- ✅ **Custom template tags**:
  - `total_posts` - Display total published posts count
  - `show_latest_posts` - Show latest N posts
  - `get_most_commented_posts` - Display most commented posts
  - `markdown` filter - Render Markdown formatted content
- ✅ **RSS feed** - Syndication feed for latest posts
- ✅ **Sitemap** - XML sitemap for SEO optimization
- ✅ **Markdown support** - Write posts using Markdown syntax
- ✅ **PostgreSQL ready** - Prepared for migration from SQLite

## Installation

1. **Clone the repository**
```bash
   git clone <your-repo-url>
   cd myblog
```

2. **Create virtual environment**
```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
   pip install -r requirements.txt
```

4. **Run migrations**
```bash
   python manage.py makemigrations
   python manage.py migrate
```

5. **Create sample data** (optional)
```bash
   python manage.py create_sample_posts
```
   This creates an admin user with login `admin` and password `admin123`

6. **Run development server**
```bash
   python manage.py runserver
```

## Usage

- **Blog**: http://127.0.0.1:8000/
- **Admin Panel**: http://127.0.0.1:8000/admin/
- **RSS Feed**: http://127.0.0.1:8000/feed/
- **Sitemap**: http://127.0.0.1:8000/sitemap.xml
- **Tag Filtering**: http://127.0.0.1:8000/tag/django/

## Working with Tags

### Adding tags via admin panel:
1. Navigate to Posts in admin panel
2. Edit or create a post
3. Add tags separated by commas: `django, python, tutorial`
4. Save the post

### Viewing posts by tag:
- Click on any tag in the post list or detail page
- Or navigate directly: `/tag/<tag-slug>/`

## Markdown Support

Posts support Markdown formatting. Example:

```markdown
# Heading 1
## Heading 2

**Bold text**
*Italic text*

- Bullet list
- Items

[Link](https://example.com)
```

## Project Structure

```
myblog/
├── blog/                     # Blog application
│   ├── templatetags/        # Custom template tags
│   │   ├── __init__.py
│   │   └── blog_tags.py    # total_posts, show_latest_posts, etc.
│   ├── admin.py            # Admin configuration
│   ├── feeds.py            # RSS feed
│   ├── forms.py            # Forms (Email, Comment, Search)
│   ├── models.py           # Models (Post, Comment)
│   ├── sitemaps.py         # Sitemap configuration
│   ├── urls.py             # URL routing
│   └── views.py            # Views
├── templates/              # HTML templates
│   └── blog/
│       ├── base.html       # Base template with sidebar
│       ├── post/
│       │   ├── list.html   # Post list with tags
│       │   ├── detail.html # Post detail with similar posts
│       │   └── ...
└── static/                 # Static files (CSS)
```

## Technologies Used

- **Django 5.2** - Web framework
- **django-taggit 5.0+** - Tagging functionality
- **Markdown 3.5+** - Content formatting
- **PostgreSQL support** - via psycopg2-binary
- **SQLite** - Default development database

## Migration to PostgreSQL

The application is ready for PostgreSQL. See `INSTRUCTIONS.md` for detailed migration steps.

## Development

```bash
# Create superuser
python manage.py createsuperuser

# Run tests
python manage.py test

# Check for issues
python manage.py check

# Collect static files
python manage.py collectstatic
```

## License

Educational project for DevOps course.

## Author

Created as part of practical work #6 and #7 for DevOps course.