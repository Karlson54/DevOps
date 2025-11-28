# Інструкції для запуску проекту

## Початкове налаштування

1. **Клонування репозиторію**
```bash
   git clone <your-repo-url>
   cd myblog
```

2. **Створення віртуального середовища**
```bash
   python -m venv venv
   
   # Windows
   venv\Scripts\activate
   
   # Linux/Mac
   source venv/bin/activate
```

3. **Встановлення залежностей**
```bash
   pip install -r requirements.txt
```

4. **Міграції бази даних**
```bash
   python manage.py makemigrations
   python manage.py migrate
```

5. **Створення тестових даних**
```bash
   python manage.py create_sample_posts
```
   Це створить адміністратора з логіном `admin` і паролем `admin123`

6. **Запуск сервера**
```bash
   python manage.py runserver
```

7. **Відкрити в браузері**
   - Головна: http://127.0.0.1:8000/
   - Адмін-панель: http://127.0.0.1:8000/admin/
   - RSS Feed: http://127.0.0.1:8000/feed/
   - Sitemap: http://127.0.0.1:8000/sitemap.xml

## Структура проекту
```
myblog/
├── blog/                  # Додаток блогу
│   ├── migrations/        # Міграції БД
│   ├── management/        # Команди управління
│   ├── templatetags/      # Власні шаблонні теги
│   ├── admin.py          # Налаштування адмін-панелі
│   ├── feeds.py          # RSS стрічка
│   ├── forms.py          # Форми
│   ├── models.py         # Моделі даних
│   ├── sitemaps.py       # Карта сайту
│   ├── urls.py           # URL маршрути додатку
│   └── views.py          # Представлення
├── myblog/               # Налаштування проекту
│   ├── settings.py       # Конфігурація Django
│   └── urls.py           # Головні URL маршрути
├── templates/            # HTML шаблони
│   └── blog/
│       ├── base.html     # Базовий шаблон
│       └── post/         # Шаблони постів
├── static/               # Статичні файли
│   └── css/
│       └── blog.css      # Стилі
├── manage.py             # Головний скрипт Django
└── requirements.txt      # Залежності Python
```

## Функціонал

### Реалізовано у Практичній роботі №6:
- ✅ Список постів з пагінацією (3 пости на сторінку)
- ✅ Детальний перегляд посту
- ✅ SEO-дружні URL з датою та slug
- ✅ Система коментарів
- ✅ Відправка посту email'ом
- ✅ Адмін-панель для управління контентом
- ✅ Розділення постів на статуси (Draft/Published)

### Реалізовано у Практичній роботі №7:
- ✅ Тегування постів (django-taggit)
- ✅ Фільтрація постів за тегами
- ✅ Схожі пости на основі тегів
- ✅ Власні шаблонні теги:
  - `total_posts` - загальна кількість постів
  - `show_latest_posts` - останні пости
  - `get_most_commented_posts` - найбільш коментовані пости
  - `markdown` фільтр - підтримка Markdown синтаксису
- ✅ RSS стрічка новин
- ✅ Карта сайту (sitemap.xml)
- ✅ Підтримка Markdown для форматування постів
- ✅ Готовність до міграції на PostgreSQL

### Можливості адмін-панелі:
- Управління постами (створення, редагування, видалення)
- Управління тегами
- Модерація коментарів
- Фільтрація та пошук
- Автоматичне заповнення slug

## Корисні команди
```bash
# Створити нового суперкористувача
python manage.py createsuperuser

# Перевірити код на помилки
python manage.py check

# Запустити тести
python manage.py test

# Створити міграції
python manage.py makemigrations

# Застосувати міграції
python manage.py migrate

# Відкрити Django shell
python manage.py shell

# Збір статичних файлів
python manage.py collectstatic
```

## Email функціонал

У режимі розробки email відправляються в консоль.
Для production налаштуйте SMTP в `settings.py`:
```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'your_email@gmail.com'
EMAIL_HOST_PASSWORD = 'your_app_password'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
```

## Робота з тегами

### Додавання тегів до постів через адмін-панель:
1. Відкрийте http://127.0.0.1:8000/admin/
2. Перейдіть до розділу "Posts"
3. Виберіть пост для редагування
4. У полі "Tags" введіть теги через кому: `django, python, tutorial`
5. Збережіть пост

### Перегляд постів за тегом:
- URL формат: `http://127.0.0.1:8000/tag/<tag-slug>/`
- Приклад: `http://127.0.0.1:8000/tag/django/`

## Markdown синтаксис

Пости підтримують Markdown форматування:

```markdown
# Заголовок 1
## Заголовок 2
### Заголовок 3

**Жирний текст**
*Курсив*

- Список
- Елементів

1. Нумерований
2. Список

[Посилання](https://example.com)
```

## Міграція на PostgreSQL (опціонально)

Для використання PostgreSQL замість SQLite:

1. **Встановіть PostgreSQL**
   - Завантажте з https://www.postgresql.org/download/

2. **Створіть базу даних**
```sql
   CREATE USER blog WITH PASSWORD 'your_password';
   CREATE DATABASE blog OWNER blog ENCODING 'UTF8';
```

3. **Оновіть settings.py**
```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': 'blog',
           'USER': 'blog',
           'PASSWORD': 'your_password',
           'HOST': 'localhost',
           'PORT': '5432',
       }
   }
```

4. **Експортуйте дані з SQLite**
```bash
   python manage.py dumpdata --indent=2 --output=mysite_data.json
```

5. **Застосуйте міграції**
```bash
   python manage.py migrate
```

6. **Імпортуйте дані**
```bash
   python manage.py loaddata mysite_data.json
```

## Troubleshooting

### Проблема: "No module named 'django'"
**Рішення**: Переконайтеся, що віртуальне середовище активоване

### Проблема: "No module named 'taggit'"
**Рішення**: 
```bash
pip install django-taggit
```

### Проблема: Статичні файли не завантажуються
**Рішення**: 
```bash
python manage.py collectstatic
```

### Проблема: Помилки міграцій
**Рішення**: 
```bash
python manage.py migrate --run-syncdb
```

### Проблема: Теги не відображаються
**Рішення**: Переконайтеся, що:
1. django-taggit встановлено
2. Міграції застосовано
3. У шаблоні використано `{% load blog_tags %}`