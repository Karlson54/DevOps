from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from blog.models import Post
from django.utils import timezone


class Command(BaseCommand):
    help = 'Creates sample blog posts'

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
            user.set_password('admin')
            user.save()
            self.stdout.write(self.style.SUCCESS('Created admin user'))

        # Створюємо пости
        posts_data = [
            {
                'title': 'Про мене',
                'slug': 'about-me',
                'body': '''Вітаю! Мене звати [Ваше ім'я], і це мій особистий блог про веб-розробку.
                
Я студент, який вивчає Django та Python. У цьому блозі я ділюся своїм досвідом навчання, 
цікавими знахідками та проектами, над якими працюю.

Сподіваюся, що мій досвід буде корисним для інших студентів!''',
                'status': Post.Status.PUBLISHED
            },
            {
                'title': 'Як досягти успіху в онлайн-навчанні',
                'slug': 'success-in-online-learning',
                'body': '''Онлайн-навчання стає все більш популярним, але воно має свої виклики.

**Поради для успішного онлайн-навчання:**

1. Створіть розклад і дотримуйтесь його
2. Організуйте зручне робоче місце
3. Робіть регулярні перерви
4. Беріть участь в обговореннях
5. Не бійтеся ставити питання

Головне - залишатися мотивованим і зосередженим!''',
                'status': Post.Status.PUBLISHED
            },
            {
                'title': 'Перші кроки у Django',
                'slug': 'first-steps-in-django',
                'body': '''Django - це потужний Python фреймворк для веб-розробки.

У цій статті я розповім про свій досвід вивчення Django:
- Встановлення та налаштування
- Створення першого проекту
- Робота з моделями
- Створення представлень та шаблонів

Django робить веб-розробку простою та приємною!''',
                'status': Post.Status.PUBLISHED
            },
            {
                'title': 'Майбутній пост (чернетка)',
                'slug': 'future-post-draft',
                'body': 'Цей пост ще в розробці...',
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
                    self.style.SUCCESS(f'Created post: {post.title}')
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f'Post already exists: {post.title}')
                )