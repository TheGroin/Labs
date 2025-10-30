from utils import read_data
from writer import save_data

if __name__ == "__main__":
    data = read_data("input.txt")
    save_data("output.txt", data.upper())
    print("Данные успешно обработаны.")

print("main: обработка завершена")
