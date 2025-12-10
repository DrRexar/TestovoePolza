import requests
import argparse
import sys

def send_telegram_message(token, chat_id, message):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": message
    }
    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при отправке сообщения: {e}")
        if response is not None:
             print(f"Ответ сервера: {response.text}")
        return None

def main():
    parser = argparse.ArgumentParser(description='Отправка текста из файла в Telegram.')
    parser.add_argument('file_path', help='Путь к файлу с текстом сообщения')
    parser.add_argument('--token', required=True, help='Токен Telegram-бота')
    parser.add_argument('--chat_id', required=True, help='ID чата (можно узнать у @userinfobot)')

    args = parser.parse_args()

    try:
        with open(args.file_path, 'r', encoding='utf-8') as f:
            message_text = f.read()
    except FileNotFoundError:
        print(f"Файл {args.file_path} не найден.")
        sys.exit(1)

    if not message_text.strip():
        print("Файл пуст.")
        sys.exit(1)

    print("Отправка сообщения...")
    result = send_telegram_message(args.token, args.chat_id, message_text)
    
    if result and result.get('ok'):
        print("Сообщение успешно отправлено!")
    else:
        print("Не удалось отправить сообщение.")

if __name__ == "__main__":
    main()
