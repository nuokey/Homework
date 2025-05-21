def capitalize(s):
    if len(s) < 4:
        # Проверяем, все ли символы заглавные для коротких строк
        if s.isupper():
            return s
        else:
            return s
    else:
        # Считаем количество заглавных букв среди первых 4 символов
        uppercase_count = sum(1 for char in s[:4] if char.isupper())
        if uppercase_count >= 3:
            return s.upper()
        else:
            return s

print(capitalize(input()))