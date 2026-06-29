# Система управления движением денежных средств

Веб-приложение для управления движением денежных средств (ДДС).

## Возможности

* Создание записей о движении денежных средств
* Просмотр списка всех записей
* Редактирование записей
* Удаление записей
* Фильтрация записей по:

  * периоду дат;
  * статусу;
  * типу операции;
  * категории;
  * подкатегории.
* Управление справочниками:

  * статусы;
  * типы операций;
  * категории;
  * подкатегории.
* Проверка логических зависимостей:

  * категория относится к определенному типу операции;
  * подкатегория относится к определенной категории.

---

## Используемые технологии

* Python 3.13
* Django 6
* Django ORM
* SQLite
* HTML
* Bootstrap 5
* JavaScript
* Ruff

---

## Структура проекта

```text
cash-flow/
│
├── cashflow/          # Основное приложение
├── config/            # Настройки Django
├── manage.py
├── pyproject.toml
├── uv.lock
├── README.md
└── .env
```

---

## Установка и запуск

Клонировать репозиторий:

```bash
git clone https://github.com/aurusxd/cash-flow
cd cash-flow
```

Установить зависимости:

```bash
uv sync
```

Создать файл `.env` в корне проекта:

```bash
cp .env.example .env
```

Заполнить `SECRET_KEY` в `.env` любым непустым значением:

```env
SECRET_KEY=django-insecure-local-dev-key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```

Применить миграции:

```bash
uv run python manage.py migrate
```

Создать базовые справочники для чистой установки:

```bash
uv run python manage.py seed_cashflow
```

Команда добавит:

* статусы: `Бизнес`, `Личное`, `Налог`;
* типы операций: `Пополнение`, `Списание`;
* категории и подкатегории:
  * `Пополнение` -> `Доходы` -> `Продажи`, `Возвраты`;
  * `Списание` -> `Инфраструктура` -> `VPS`, `Proxy`;
  * `Списание` -> `Маркетинг` -> `Farpost`, `Avito`.

Команду можно запускать повторно: она не создает дубли.

## Создание администратора

```bash
uv run python manage.py createsuperuser
```

Запустить проект:

```bash
uv run python manage.py runserver
```

После запуска приложение будет доступно по адресу:

```
http://127.0.0.1:8000/
```

Административная панель:

```
http://127.0.0.1:8000/admin/
```

---

## Реализованные функции

* CRUD для записей ДДС
* CRUD для справочников
* Фильтрация записей
* Валидация данных
* Логические зависимости между сущностями
* Команда заполнения базовых справочников
* Docker Compose для запуска одной командой

---
## Запуск через Docker Compose

Docker Compose позволяет поднять проект одной командой: контейнер сам применит
миграции, создаст базовые справочники и запустит сервер.

```bash
docker compose up --build
```

Если Docker Compose выводит предупреждения про переменные из `.env`, замените
`SECRET_KEY` в `.env` на простой dev-ключ без символа `$`, например:

```env
SECRET_KEY=django-insecure-local-dev-key
```

После запуска приложение будет доступно по адресу:

```text
http://127.0.0.1:8000/
```

Что выполняется внутри контейнера при старте:

```bash
uv run python manage.py migrate
uv run python manage.py seed_cashflow
uv run python manage.py runserver 0.0.0.0:8000
```

SQLite-база хранится в Docker volume `sqlite-data`, поэтому данные сохраняются
между перезапусками контейнера.

Создать администратора при Docker-запуске:

```bash
docker compose run --rm web uv run python manage.py createsuperuser
```

Остановить контейнеры:

```bash
docker compose down
```

Удалить контейнеры вместе с SQLite volume:

```bash
docker compose down -v
```


---

## Основные сущности

* Record — запись движения денежных средств
* Status — статус записи
* OperationType — тип операции
* Category — категория операции
* Subcategory — подкатегория операции

Связи:

```
OperationType
      │
      ▼
 Category
      │
      ▼
Subcategory

Record
 ├── Status
 ├── OperationType
 ├── Category
 └── Subcategory
```

---


