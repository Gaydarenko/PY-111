"""
Автор: Гайдаренко Евгений Григорьевич

Задача:
Дан каталог книг.
Реализуйте библиотеку для хранения данных книг и поиску по каталогу.
Каталог должен поддерживать возможность добавления и удаления книг, редактирования информации о книге,
а также обладать персистентностью (т.е. сохранять библиотеку в внешнем файле и подгружать обратно).
Также необходимо оформить точку входа, поддерживать поиск по различным параметрам
и обеспечить интерфейс взаимодействия пользователя с библиотекой.
"""

# Перед отправлением на проверку преподавателю необходимо пройтись по тегу "проверить"

import tkinter as tk
import tkinter.messagebox as mb
import json


def create_window():
    """
    Функция создаёт головное окно с полями ввода данных и кнопкой поиска в каталоге по введенным данным.
    :return: None
    """
    # Создание головного окна по центру экрана.
    window = tk.Tk()
    window.title('Каталог библиотеки им.Гайдаренко Е.Г.')
    w = window.winfo_screenwidth()      # Переменная создана для удобства чтения кода
    h = window.winfo_screenheight()     # Переменная создана для удобства чтения кода
    window.geometry(f'{size_x}x{size_y}+{w // 2 - size_x // 2}+{h // 2 - size_y // 2}')
    window.resizable(False, False)      # Запрет изменения размера окна

    # Отрисовка текста в окне
    label_title = tk.Label(window, text='Название книги:')
    label_title.place(x=10, y=10)
    label_author = tk.Label(window, text='Автор:')
    label_author.place(x=10, y=40)
    label_genre = tk.Label(window, text='Жанр:')
    label_genre.place(x=10, y=70)

    # Размещение полей ввода данных напротив отрисованного ранее текста
    entry_title = tk.Entry(window, width=45)
    entry_title.place(x=120, y=10)
    entry_author = tk.Entry(window, width=45)
    entry_author.place(x=120, y=40)
    entry_genre = tk.Entry(window, width=45)
    entry_genre.place(x=120, y=70)

    # Альтернативный вариант отрисовки текста в окне и размещения полей ввода данных
    # tk.Label(text='Название книги:').grid(row=0, column=0)
    # tk.Label(text='Автор:').grid(row=1, column=0)
    # tk.Label(text='Жанр:').grid(row=2, column=0)
    #
    # entry_title = tk.Entry(width=25)
    # entry_title.grid(row=0, column=1, columnspan=2)
    # entry_author = tk.Entry(width=25)
    # entry_author.grid(row=1, column=1, columnspan=2)
    # entry_genre = tk.Entry(width=25)
    # entry_genre.grid(row=2, column=1, columnspan=2)

    # Создание кнопок поиска и добавления книги, а также привязка к ним функций
    button_search = tk.Button(window, text='Поиск')
    button_search.bind('<Button-1>', lambda x: search_window(entry_title.get(), entry_author.get(), entry_genre.get()))
    button_search.place(x=size_x // 3, y=110)
    button_add = tk.Button(window, text='Добавить')
    button_add.bind('<Button-1>', lambda x: add_book(entry_title.get(), entry_author.get(), entry_genre.get()))
    button_add.place(x=2 * size_x // 3, y=110)

    window.mainloop()


def search(title: str, author: str, genre: str):
    """
    Функция выполняет поиск в каталоге по переданным данным.
    :param title: Строка с названием книги
    :param author: Строка с фамилией (возможно с инициалами) автора книги
    :param genre: Строка с годом выпуска книги
    :return roster: Список книг (с данными), удовлетворяющих параметрам поиска
    """

    roster = []

    with open('catalog.lib', 'r', encoding='utf-8') as file:
        lines = file.readlines()

    for line in lines:
        line = json.loads(line)     # Нужно не забыть проверить на необходимость!!!
        line = list(map(lambda x: x.capitalize(), line))
        target = list(map(lambda x: x.capitalize(), [title, author, genre]))
        if title == '':
            target[0] = line[0]
        if author == '':
            target[1] = line[1]
        if genre == '':
            target[2] = line[2]

        if line == target:
            roster.append(line)
    if not roster:
        return None
    return roster


def search_window(title, author, genre):
    """
    Функция создаёт окно, которое появляется ровно над головным, тем самым скрывая его.
    :param title: Строка с названием книги
    :param author: Строка с фамилией (возможно с инициалами) автора книги
    :param genre: Строка с годом выпуска книги
    :return: None
    """

    def insert(book):
        """
        Функция вставляет данные в поля окна результатов поиска
        :param book: Список данных книги
        :return: None
        """
        result_book_number.configure(state="normal")
        result_book_number.delete(0, tk.END)
        result_book_number.insert(0, f'{num+1} из {len_res}')
        result_book_number.configure(state="disabled")
        result_title.configure(state="normal")
        result_title.delete(0, tk.END)
        result_title.insert(0, book[0])
        result_title.configure(state="disabled")
        result_author.configure(state="normal")
        result_author.delete(0, tk.END)
        result_author.insert(0, book[1])
        result_author.configure(state="disabled")
        result_genre.configure(state="normal")
        result_genre.delete(0, tk.END)
        result_genre.insert(0, book[2])
        result_genre.configure(state="disabled")

    def scroll_right():
        global num
        if num + 1 < len(results):
            num += 1
            insert(results[num])

    def scroll_left():
        global num
        if num - 1 >= 0:
            num -= 1
            insert(results[num])

    global num
    num = 0

    if [title, author, genre] == ['', '', '']:
        return None

    results = search(title, author, genre)
    if not results:
        return mb.showinfo('Упс!!!', 'Такой книги нет в базе')
    len_res = len(results)

    # Создание нового окна поверх всех окон
    window = tk.Tk()
    window.title(f'Найдено книг по заданным параметрам:   {len_res}')
    w = window.winfo_screenwidth()
    h = window.winfo_screenheight()
    window.geometry(f'{size_x}x{size_y + 50}+{w // 2 - size_x // 2}+{h // 2 - size_y // 2}')
    # window.grab_set()
    window.focus_set()

    # Создание кнопок редактирования, удаления и переключения результатов
    button_edit = tk.Button(window, text='Изменить')
    button_edit.bind('<Button-1>', lambda x: edit_window(results[num][0], results[num][1], results[num][2]))
    button_edit.place(x=100, y=150)
    button_del = tk.Button(window, text='Удалить')
    button_del.bind('<Button-1>', lambda x: del_book(results[num][0], results[num][1], results[num][2]))
    button_del.place(x=200, y=150)
    button_scroll_r = tk.Button(window, text='>>')
    button_scroll_r.bind('<Button-1>', lambda x: scroll_right())
    button_scroll_r.place(x=300, y=150)
    button_scroll_l = tk.Button(window, text='<<')
    button_scroll_l.bind('<Button-1>', lambda x: scroll_left())
    button_scroll_l.place(x=10, y=150)

    # Отрисовка текста в окне
    label_book_number = tk.Label(window, text=f'Номер книги:')
    label_book_number.place(x=10, y=10)
    label_title = tk.Label(window, text='Название книги:')
    label_title.place(x=10, y=40)
    label_author = tk.Label(window, text='Автор:')
    label_author.place(x=10, y=70)
    label_genre = tk.Label(window, text='Жанр:')
    label_genre.place(x=10, y=100)

    # Размещение полей для ответов
    result_book_number = tk.Entry(window, width=45)
    result_book_number.place(x=110, y=10)
    result_book_number.insert(0, f'{num+1} из {len_res}')
    result_book_number.configure(state="disabled")
    result_title = tk.Entry(window, width=45)
    result_title.place(x=110, y=40)
    result_title.insert(0, results[num][0])
    result_title.configure(state="disabled")
    result_author = tk.Entry(window, width=45)
    result_author.place(x=110, y=70)
    result_author.insert(0, results[num][1])
    result_author.configure(state="disabled")
    result_genre = tk.Entry(window, width=45)
    result_genre.place(x=110, y=100)
    result_genre.insert(0, results[num][2])
    result_genre.configure(state="disabled")

    window.mainloop()


def edit_window(title, author, genre):

    # Создание нового окна поверх всех окон
    window = tk.Tk()
    window.title(f'Редактирование книги {title}')
    w = window.winfo_screenwidth()
    h = window.winfo_screenheight()
    window.geometry(f'{size_x+30}x{size_y + 150}+{w // 2 - size_x // 2}+{h // 2 - size_y // 2}')
    window.focus_set()

    # Отрисовка текста в окне
    label_text = tk.Label(window, text='Если поле будет не заполнено, то данные этой графы будут отсутствовать')
    label_text.place(x=10, y=10)
    label_title = tk.Label(window, text='Название книги:')
    label_title.place(x=10, y=40)
    label_title_old = tk.Label(window, text=f'Сейчас:      {title}')
    label_title_old.place(x=30, y=60)
    label_title_old = tk.Label(window, text='Новое:')
    label_title_old.place(x=30, y=80)
    label_author = tk.Label(window, text='Автор:')
    label_author.place(x=10, y=110)
    label_author_old = tk.Label(window, text=f'Сейчас:      {author}')
    label_author_old.place(x=30, y=130)
    label_author_old = tk.Label(window, text='Новое:')
    label_author_old.place(x=30, y=150)
    label_genre = tk.Label(window, text='Жанр:')
    label_genre.place(x=10, y=180)
    label_genre_old = tk.Label(window, text=f'Сейчас:      {genre}')
    label_genre_old.place(x=30, y=200)
    label_genre_old = tk.Label(window, text='Новое:')
    label_genre_old.place(x=30, y=220)

    # Размещение полей ввода данных напротив отрисованного ранее текста
    entry_title_new = tk.Entry(window, width=45)
    entry_title_new.place(x=90, y=80)
    entry_author_new = tk.Entry(window, width=45)
    entry_author_new.place(x=90, y=150)
    entry_genre_new = tk.Entry(window, width=45)
    entry_genre_new.place(x=90, y=220)

    # Создание кнопок редактирования, удаления и переключения результатов
    button_edit = tk.Button(window, text='Применить изменения')
    button_edit.bind('<Button-1>', lambda x: edit_book(title, author, genre, entry_title_new.get(),
                                                       entry_author_new.get(), entry_genre_new.get()))
    button_edit.place(x=150, y=260)


def add_book(title, author, genre):
    """
    Добавление новой книги в каталог.
    Достаточно указать только наименование (например, утеряна обложка и неизвестен автор)
    :param title: Строка с названием книги
    :param author: Строка с фамилией (возможно с инициалами) автора книги
    :param genre: Строка с годом выпуска книги
    :return None
    """
    target = list(map(lambda x: x.capitalize(), [title, author, genre]))
    if len(title):
        with open('catalog.lib', 'r', encoding='utf-8') as file:
            for line in file.readlines():
                line = json.loads(line)
                line = list(map(lambda x: x.capitalize(), line))
                if line == target:
                    return mb.showinfo('Упс!!!', 'Такая книга уже существует')
        with open('catalog.lib', 'a', encoding='utf-8') as file:
            json.dump(target, file, ensure_ascii=False)
            file.write(f'\n')
        mb.showinfo(f"Книга добавлена в базу.", f"Название книги: {target[0]}\nАвтор: {target[1]}\nЖанр: {target[2]}")


def del_book(title, author, genre):
    """
    Функция производит удаление книги путем выгрузки в память содержимого файла и перезаписи этого файла.
    Также производится подсчет количества удаленных книг.
    :param title: Строка с названием книги
    :param author: Строка с фамилией (возможно с инициалами) автора книги
    :param genre: Строка с годом выпуска книги
    :return: count: Количество удаленных книг
    """
    count = 0
    if len(title):
        with open('catalog.lib', 'r', encoding='utf-8') as file:
            lines = file.readlines()

        file = open('catalog.lib', 'w')     # очиска файла
        file.close                          # очиска файла

        with open('catalog.lib', 'a', encoding='utf-8') as file:
            for line in lines:
                line = json.loads(line)
                if line != [title, author, genre]:
                    json.dump(line, file, ensure_ascii=False)
                    file.write(f'\n')
                else:
                    count += 1
        mb.showinfo('Готово!', 'Книга удалена.')
    return count


def edit_book(title, author, genre, new_title, new_author, new_genre):
    """
    Функция производит редактирование инфоормации о книге.
    :param title: Строка с неисправленным названием книги
    :param author: Строка с неисправленной фамилией (возможно с инициалами) автора книги
    :param genre: Строка с неисправленным годом выпуска книги
    :param new_title: Строка с исправленным названием книги
    :param new_author: Строка с исправленной фамилией (возможно с инициалами) автора книги
    :param new_genre: Строка с исправленным годом выпуска книги
    :return:
    """
    if len(new_title):
        with open('catalog.lib', 'r', encoding='utf-8') as file:
            lines = file.readlines()

        file = open('catalog.lib', 'w')     # очиска файла
        file.close                          # очиска файла

        target = list(map(lambda x: x.capitalize(), [new_title, new_author, new_genre]))
        with open('catalog.lib', 'a', encoding='utf-8') as file:
            for line in lines:
                line = json.loads(line)     # Нужно не забыть проверить на необходимость!!!
                if line == [title, author, genre]:
                    json.dump(target, file, ensure_ascii=False)
                    file.write(f'\n')
                else:
                    json.dump(line, file, ensure_ascii=False)
                    file.write(f'\n')
        mb.showinfo('Готово!', 'Изменения данных о книге успешно применены.')
    else:
        mb.showinfo('Внимание', 'Необходимо указать название книги!')

# size_x = 650
# size_y = 300
#
# create_window()


if __name__ == '__main__':
    a = [["Унесенные ветром", "Евген у.К.", "наука"],
         ["Физика", "Евген", "наука"],
         ["Алгебра", "Евген", "наука"],
         ["Химия", "Евген", "наука"],
         ["Ботаника", "Елена", "наука"],
         ["Физ-ра", "Евген", "спорт"],
         ["1", "2", "3"]]

    # Проверка функции добавления книг
    # for i in a:
    #     title = i[0]
    #     author = i[1]
    #     genre = i[2]
    #     add_book(title, author, genre)

    # Проверка функции удаления книг
    # del_book("Химия", "Евген", "наука")

    size_x = 400
    size_y = 150
    create_window()
