# Тестовое задание для Polza Outreach Engine

В этом репозитории содержатся решения для трех частей тестового задания.

## 1. Проверка email-доменов (`email_checker.py`)

Скрипт проверяет список email-адресов на наличие MX-записей.

**Запуск:**
```bash
python email_checker.py emails.txt
```
Где `emails.txt` — файл со списком адресов (по одному на строку).

**Пример вывода:**
```
test@gmail.com: домен валиден
nonexistent.com: домен отсутствует
...
```

## 2. Мини-интеграция с Telegram (`telegram_sender.py`)

Скрипт отправляет текст из указанного файла в Telegram-чат.

**Требования:**
- Токен бота (от @BotFather)
- Chat ID (можно узнать у @userinfobot)

**Запуск:**
```bash
python telegram_sender.py message.txt --token "ВАШ_ТОКЕН" --chat_id "ВАШ_CHAT_ID"
```

## 3. Архитектурная задача (`architecture.md`)

Предложение по архитектуре для обслуживания 1200 outreach-адресов находится в файле `architecture.md`.

