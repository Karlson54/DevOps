from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from blog.models import Post
from django.utils import timezone


class Command(BaseCommand):
    help = 'Creates sample blog posts in Ukrainian'

    def handle(self, *args, **kwargs):
        # Отримуємо або створюємо користувача
        user, created = User.objects.get_or_create(
            username='admin',
            defaults={
                'email': 'admin@example.com',
                'is_staff': True,
                'is_superuser': True
            }
        )
        
        if created:
            user.set_password('admin123')
            user.save()
            self.stdout.write(self.style.SUCCESS('Created admin user (password: admin123)'))

        # Створюємо пости
        posts_data = [
            {
                'title': 'Про мене',
                'slug': 'pro-mene',
                'body': '''Вітаю! Мене звати [Ваше ім'я], і це мій особистий блог про веб-розробку.
                
Я студент, який вивчає Django та Python. У цьому блозі я ділюся своїм досвідом навчання, 
цікавими знахідками та проектами, над якими працюю.

Основні напрямки, якими я цікавлюся:
- Веб-розробка з Django
- Python програмування
- DevOps практики
- Базі даних та ORM

Сподіваюся, що мій досвід буде корисним для інших студентів!''',
                'status': Post.Status.PUBLISHED
            },
            {
                'title': 'Як досягти успіху в онлайн-навчанні',
                'slug': 'uspikh-v-onlayn-navchanni',
                'body': '''Онлайн-навчання стає все більш популярним, але воно має свої виклики.

**Основні поради для успішного онлайн-навчання:**

1. **Створіть чіткий розклад** - Визначте години для навчання і дотримуйтесь їх
2. **Організуйте робоче місце** - Зручне, тихе місце без відволікаючих факторів
3. **Робіть регулярні перерви** - Кожні 45-50 хвилин робіть 10-хвилинну перерву
4. **Беріть активну участь** - Ставте питання, беріть участь в обговореннях
5. **Не бійтеся просити допомоги** - Викладачі та однокурсники завжди готові допомогти

Головне - залишатися мотивованим і зосередженим на своїх цілях!''',
                'status': Post.Status.PUBLISHED
            },
            {
                'title': 'Перші кроки у Django',
                'slug': 'pershi-kroky-u-django',
                'body': '''Django - це потужний Python фреймворк для веб-розробки.

**Мій досвід вивчення Django:**

**Встановлення та налаштування**
Почав з встановлення Django через pip і створення першого проекту.

**Робота з моделями**
Навчився створювати моделі для роботи з базою даних, використовувати міграції.

**Представлення та шаблони**
Освоїв створення views і templates для відображення даних користувачам.

**Адміністративна панель**
Django має чудову вбудовану адмін-панель для управління контентом.

Django робить веб-розробку простою, структурованою та приємною!''',
                'status': Post.Status.PUBLISHED
            },
            {
                'title': 'Робота з формами в Django',
                'slug': 'robota-z-formamy-v-django',
                'body': '''Форми - важлива частина будь-якого веб-застосунку.

**Типи форм у Django:**

1. **Form** - для створення стандартних форм
2. **ModelForm** - для форм на основі моделей

**Валідація даних**
Django автоматично валідує дані форми і показує помилки користувачу.

**CSRF захист**
Всі форми захищені від CSRF атак за допомогою спеціальних токенів.

Форми Django спрощують обробку введення користувача!''',
                'status': Post.Status.PUBLISHED
            },
            {
                'title': 'Система коментарів для блогу',
                'slug': 'systema-komentariv',
                'body': '''Додавання коментарів робить блог інтерактивним.

**Що потрібно для системи коментарів:**

- Модель Comment з полями для імені, email та тексту
- Форма для введення коментаря
- Представлення для обробки коментарів
- Шаблони для відображення

**Модерація коментарів**
Важливо мати можливість активувати/деактивувати коментарі через адмін-панель.

Коментарі роблять блог живим і цікавим!''',
                'status': Post.Status.PUBLISHED
            },
            {
                'title': 'Майбутня стаття про тестування (чернетка)',
                'slug': 'maybutnya-stattya-testuvannya',
                'body': '''Ця стаття ще в розробці. Скоро тут буде інформація про тестування Django застосунків...

Плануються теми:
- Unit тести
- Integration тести
- Test fixtures
- Coverage аналіз''',
                'status': Post.Status.DRAFT
            }
        ]

        for post_data in posts_data:
            post, created = Post.objects.get_or_create(
                slug=post_data['slug'],
                defaults={
                    'title': post_data['title'],
                    'author': user,
                    'body': post_data['body'],
                    'status': post_data['status'],
                    'publish': timezone.now()
                }
            )
            if created:
                self.stdout.write(
                    self.style.SUCCESS(f'✓ Created post: {post.title}')
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f'○ Post already exists: {post.title}')
                )
        
        self.stdout.write(self.style.SUCCESS('\n=== Setup Complete ==='))
        self.stdout.write('Run: python manage.py runserver')
        self.stdout.write('Admin: http://127.0.0.1:8000/admin/')
        self.stdout.write('Login: admin / admin123')