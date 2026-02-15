import random
import string

def generate_unique_email(domain="yandex.ru"):
    first_name = "test"
    last_name = "user"
    cohort_number = "7"
    random_digits = ''.join(random.choices(string.digits, k=3))

    local_part = f"{first_name}_{last_name}_{cohort_number}_{random_digits}"
    return f"{local_part}@{domain}"


def generate_password(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))