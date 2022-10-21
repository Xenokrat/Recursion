def is_palindrome_recr(text: str):
    """Проверка является ли текст палиндромом. Без учета регистра букв, с учетом пробелов"""
    if len(text) == 1:
        return True
    if text[0].lower() != text[-1].lower():
        return False

    return is_palindrome_recr(text[1:-1])
