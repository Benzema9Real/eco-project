# 🐦 КормушкиТим — Сайт фото-отчётов

Django-сайт для команды с кормушками. Участники оставляют фото-отчёты, все видят галерею.

## Деплой на Railway

### 1. Загрузи код на GitHub
```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/ВАШ_ЛОГИН/feeders-site.git
git push -u origin main
```

### 2. Задеплой на Railway
1. Зайди на https://railway.app
2. Нажми **New Project → Deploy from GitHub repo**
3. Выбери свой репозиторий
4. Railway автоматически определит Django!

### 3. Добавь PostgreSQL
1. В проекте нажми **New → Database → PostgreSQL**
2. Railway сам добавит `DATABASE_URL` в переменные

### 4. Настрой переменные окружения
В Railway → Settings → Variables добавь:
```
SECRET_KEY=твой-случайный-секретный-ключ-здесь
DEBUG=False
```

Сгенерировать SECRET_KEY:
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

### 5. Создай суперюзера (для админки)
В Railway → Terminal:
```bash
python manage.py createsuperuser
```

Админка доступна на `/admin/`

## Хранение фото

⚠️ На Railway файлы сбрасываются при редеплое!

**Решение:** Добавь Railway Volume:
1. Railway → твой сервис → Volumes
2. Примонтируй к `/app/media`

Или используй Cloudinary — пиши если нужна помощь с настройкой.

## Локальный запуск
```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```
