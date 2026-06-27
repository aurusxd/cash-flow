# Cash Flow Management System

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

## Установка

Клонировать репозиторий:

```bash
git clone https://github.com/aurusxd/cash-flow
cd cash-flow
```

Установить зависимости:

```bash
uv sync
```

---

## Настройка окружения

Создать файл `.env` в корне проекта:

```env
SECRET_KEY=your_secret_key
DEBUG=True
```

---

## Применение миграций

```bash
uv run python manage.py makemigrations
uv run python manage.py migrate
```

---

## Создание администратора

```bash
uv run python manage.py createsuperuser
```

---

## Запуск проекта

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

## Реализованные функции

* CRUD для записей ДДС
* CRUD для справочников
* Фильтрация записей
* Валидация данных
* Логические зависимости между сущностями
* Работа с Django ORM

---
