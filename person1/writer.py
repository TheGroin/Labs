def save_data(filename, text):
    """Сохраняет данные в файл"""
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(text)

print("dev2: writer done")
print("change from development branch")
