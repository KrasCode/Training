import string


def str_to_pos(my_text: str) -> str:
    """
    Создать функцию которая принимает строку и заменяет каждую букву на её позицию в алфавите.
    Если что-то в тексте не является буквой, игнорируйте это и не возвращайте. На выходе получаем строку.
    """
    sim_filter = (sim for sim in my_text.lower() if sim in string.ascii_lowercase)
    dig_for_sim = [str(ord(letter) - 96) for letter in sim_filter]
    print(' '.join(dig_for_sim))


if __name__ == '__main__':
    new_text = "I learn Python with Python Nation!!!"
    str_to_pos(new_text)
