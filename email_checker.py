import sys
import dns.resolver
import argparse

def check_email_domain(email):
    try:
        domain = email.split('@')[1]
    except IndexError:
        return f"{email}: Некорректный формат email"

    domain_exists = False
    try:
        # Проверка, существует ли домен (запись A)
        try:
            dns.resolver.resolve(domain, 'A')
            domain_exists = True
        except (dns.resolver.NXDOMAIN, dns.resolver.NoAnswer, dns.resolver.LifetimeTimeout):
            domain_exists = False
        
        # Проверка записей MX
        mx_records = dns.resolver.resolve(domain, 'MX')
        if mx_records:
            return f"{email}: домен валиден"
        else:
            return f"{email}: MX-записи отсутствуют или некорректны"

    except dns.resolver.NXDOMAIN:
        return f"{email}: домен отсутствует"
    except (dns.resolver.NoAnswer, dns.resolver.LifetimeTimeout):
        # Если запись A существует, но нет записей MX, или тайм-аут
        if domain_exists:
             return f"{email}: MX-записи отсутствуют или некорректны"
        return f"{email}: домен отсутствует (или тайм-аут)"
    except Exception as e:
        return f"{email}: Ошибка проверки ({str(e)})"

def main():
    parser = argparse.ArgumentParser(description='Проверка MX-записей для списка email-адресов.')
    parser.add_argument('input_file', help='Путь к файлу со списком email-адресов (один на строку)')
    args = parser.parse_args()

    try:
        with open(args.input_file, 'r', encoding='utf-8') as f:
            emails = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"Файл {args.input_file} не найден.")
        return

    print(f"Проверка {len(emails)} адресов...\n")
    for email in emails:
        result = check_email_domain(email)
        print(result)

if __name__ == "__main__":
    main()
