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

## Структура проекту
```
myblog/
├── blog/                  # Додаток блогу
│   ├── migrations/        # Міграції БД
│   ├── management/        # Команди управління
│   ├── templates/         # Не використовується (використовуємо глобальні)
│   ├── admin.py          # Налаштування адмін-панелі
│   ├── forms.py          # Форми
│   ├── models.py         # Моделі даних
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

### Реалізовано:
- ✅ Список постів з пагінацією (3 пости на сторінку)
- ✅ Детальний перегляд посту
- ✅ SEO-дружні URL з датою та slug
- ✅ Система коментарів
- ✅ Відправка посту email'ом
- ✅ Адмін-панель для управління контентом
- ✅ Розділення постів на статуси (Draft/Published)

### Можливості адмін-панелі:
- Управління постами (створення, редагування, видалення)
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

## Troubleshooting

### Проблема: "No module named 'django'"
**Рішення**: Переконайтеся, що віртуальне середовище активоване

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