print("dev3: init utils")
def read_data(filename):
    """Считывает данные из файла"""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        return "Файл не найден"


print("utils: старт чтения файла")
