# DevOps Lab 7: Docker + PostgreSQL Web Application

Простий веб-застосунок на Flask з PostgreSQL, повністю контейнеризований через Docker та Docker Compose.

## 🚀 Функціонал

- ✅ Веб-сервер на Flask
- ✅ PostgreSQL база даних
- ✅ Docker контейнеризація
- ✅ Docker Compose оркестрація
- ✅ Persistent volumes для даних
- ✅ Health checks
- ✅ Автоматична ініціалізація БД
- ✅ REST API для роботи з нотатками

## 📋 Вимоги

- Docker 20.10+
- Docker Compose 2.0+

## 🛠️ Встановлення та запуск

### 1. Клонування репозиторію
```bash
git clone <repository-url>
cd lab7
```

### 2. Налаштування змінних оточення
```bash
cp .env.example .env
# Відредагуйте .env файл за потреби
```

### 3. Запуск через Docker Compose
```bash
# Побудувати та запустити контейнери
docker-compose up -d

# Переглянути логи
docker-compose logs -f

# Перевірити статус
docker-compose ps
```

### 4. Ініціалізація бази даних (опціонально)

База даних автоматично ініціалізується при першому запуску. Але якщо потрібно повторно виконати ініціалізацію:
```bash
./init_db.sh
```

## 📡 API Endpoints

### Домашня сторінка
```
GET http://localhost:5000/
```

### Health Check
```bash
curl http://localhost:5000/health
```

### Отримати всі нотатки
```bash
curl http://localhost:5000/notes
```

### Додати нову нотатку
```bash
curl -X POST http://localhost:5000/notes \
  -H "Content-Type: application/json" \
  -d '{"title": "My Note", "content": "Note content here"}'
```

## 🗄️ Структура бази даних

### Таблиця `notes`

| Колонка | Тип | Опис |
|---------|-----|------|
| id | SERIAL | Primary key |
| title | VARCHAR(255) | Заголовок нотатки |
| content | TEXT | Вміст нотатки |
| created_at | TIMESTAMP | Час створення |
| updated_at | TIMESTAMP | Час останнього оновлення |

## 🐳 Docker команди

### Запуск контейнерів
```bash
docker-compose up -d
```

### Зупинка контейнерів
```bash
docker-compose down
```

### Зупинка з видаленням volumes
```bash
docker-compose down -v
```

### Перебудова образів
```bash
docker-compose up -d --build
```

### Перегляд логів
```bash
docker-compose logs -f app
docker-compose logs -f db
```

### Доступ до PostgreSQL CLI
```bash
docker-compose exec db psql -U devops_user -d devops_db
```

### Доступ до контейнера застосунку
```bash
docker-compose exec app /bin/bash
```

## 📂 Структура проєкту
```
lab7/
├── app/
│   ├── __init__.py          # Python package init
│   └── main.py              # Flask application
├── sql/
│   └── init.sql             # Database initialization
├── .env                     # Environment variables (не в git)
├── .env.example             # Environment template
├── .gitignore               # Git ignore rules
├── docker-compose.yml       # Docker Compose configuration
├── Dockerfile               # Docker image definition
├── init_db.sh              # Database initialization script
├── requirements.txt         # Python dependencies
└── README.md               # Documentation
```

## 🔧 Налаштування

### Зміна портів

Відредагуйте `.env` файл:
```env
APP_PORT=8080
POSTGRES_PORT=5433
```

### Зміна credentials

Відредагуйте `.env` файл:
```env
POSTGRES_USER=myuser
POSTGRES_PASSWORD=mysecurepassword
POSTGRES_DB=mydb
```

## 🧪 Тестування

### Перевірка підключення до БД
```bash
docker-compose exec db pg_isready -U devops_user -d devops_db
```

### Перевірка таблиць
```bash
docker-compose exec db psql -U devops_user -d devops_db -c "\dt"
```

### Перевірка даних
```bash
docker-compose exec db psql -U devops_user -d devops_db -c "SELECT * FROM notes;"
```

## 🐛 Troubleshooting

### Проблеми з підключенням до БД

1. Перевірте, чи запущені контейнери:
```bash
docker-compose ps
```

2. Перевірте логи БД:
```bash
docker-compose logs db
```

3. Перевірте health check:
```bash
curl http://localhost:5000/health
```

### Контейнери не запускаються
```bash
# Очистити все та перезапустити
docker-compose down -v
docker-compose up -d --build
```

### База даних не ініціалізується
```bash
# Вручну виконати ініціалізацію
./init_db.sh
```

## 📝 Автор

DevOps Lab 7 Assignment

## 📄 Ліцензія

MIT