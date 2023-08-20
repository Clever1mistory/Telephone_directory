import json

filename = 'phonebook.txt'


def load_phonebook() -> list:
    """ Загрузка данных из файла """
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_phonebook(phonebook: list):
    """ Сохранение данных в файл.
     phonebook - список записей справочника
    """
    with open(filename, 'w') as file:
        json.dump(phonebook, file)


def display_entries(phonebook: list, p_size: int = 10):

    """ Постраничный вывод всех абонентов
    phonebook - список записей справочника
    p_size - количество записей на одной странице
    """

    p_number = 1
    all_p = len(phonebook) // p_size + 1
    while True:
        start_i = (p_number - 1) * p_size
        end_i = start_i + p_size
        curr_p = phonebook[start_i:end_i]

        for entries in curr_p:
            print(entries)

        print(f"Страница {p_number} из {all_p}")
        func = input("Нажмите Enter для того, чтобы продолжить, 'n' - на следующую страницу, 'q' - для выхода")
        if func.lower() == 'q':
            break
        elif func.lower() == 'n':
            p_number += 1
            if p_number > all_p:
                p_number = 1
        else:
            p_number += 1
            if p_number > all_p:
                p_number = 1


def add_entry(phonebook: list):

    """ Добавление нового абонента в справочник
    phonebook - список записей справочника """

    entry = {
        "Имя": input("Введите имя:"),
        "Фамилия": input("Введите фамилию:"),
        "Отчество": input("Введите отчество:"),
        "Название организации": input("Введите название организации:"),
        "Тел. рабочий": input("Введите рабочий телефонный номер:"),
        "Тел. личный": input("Введите личный телефонный номер:"),
    }
    phonebook.append(entry)
    save_phonebook(phonebook)
    print("Абонент успешно добавлен")


def edit_entry(phonebook: list):

    """ Редактирование существующей записи абонента в справочнике
    phonebook - список записей справочника """

    surname = input("Введите фамилию изменяемой записи абонента: ")
    found_entries = []

    for index, entry in enumerate(phonebook):
        if entry["Фамилия"] == surname:
            found_entries.append((index, entry))

    if len(found_entries) == 0:
        print("Записи с указанной фамилией не найдены")
    elif len(found_entries) == 1:
        index, entry = found_entries[0]
        print(f"Найдена запись: {entry}")
        print("Введите новые данные для записи:")

        for key in entry:
            entry[key] = input(f"{key}: ")

        phonebook[index] = entry
        save_phonebook(phonebook)
        print("Запись успешно изменена")
    else:
        print("Найдено несколько записей с указанной фамилией, уточните запрос")


def search_entry(phonebook: list):

    """ Поиск по заданным параметрам
    phonebook - список записей справочника """

    param = input("Введите параметры поиска(имя, фамилия, отчество, личный телефонный номер:)").lower()
    found_entries = []
    for entry in phonebook:
        if (
            param in entry["Имя"].lower()
            or param in entry["Фамилия"].lower()
            or param in entry["Отчество"].lower()
            or param in entry["Тел. личный"].lower()
        ):
            found_entries.append(entry)
        if len(found_entries) == 0:
            print("Записи с данными параметрами не найдены. Проверьте правильность ввода")
        else:
            print("Результаты поиска:")

            for entry in found_entries:
                print(entry)


def main():
    """ Главная функция для запуска кода """
    phonebook = load_phonebook()

    while True:
        print("\n=== Телефонный справочник ===\n")
        print("1. Вывод записей")
        print("2. Добавление новой записи")
        print("3. Редактирование записи")
        print("4. Поиск записей")
        print("5. Сохранить и выйти")
        choice = input("Выберите действие (1-5): ")

        if choice == "1":
            display_entries(phonebook)
        elif choice == "2":
            add_entry(phonebook)
        elif choice == "3":
            edit_entry(phonebook)
        elif choice == "4":
            search_entry(phonebook)
        elif choice == "5":
            save_phonebook(phonebook)
            print("Сохранение данных и выход из программы")
            break
        else:
            print("Некорректный выбор. Пожалуйста, повторите.")


if __name__ == "__main__":
    main()