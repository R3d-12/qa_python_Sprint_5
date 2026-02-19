from faker import Faker

faker = Faker()

def generate_registration_data():
    """
    Генерирует случайные данные для регистрации пользователя.
    
    """
    name = faker.first_name()  # Имя
    email = faker.free_email()   # email
    password = faker.password(
        length=8,                # Минимальная длина — 8 символов
        special_chars=True,      # Включает спецсимволы
        digits=True,             # Включает цифры
        upper_case=True,         # Включает заглавные буквы
        lower_case=True          # Включает строчные буквы
    )
    
    return name, email, password