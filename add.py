from data import directories, documents


class Secretary:
    def __init__(self, name, password):
        self.name = name
        self.password = password

    def name_people(self, doc_number):
        """команда, которая спросит номер документа и выведет имя человека, которому он принадлежит"""
        owner = 'Вы ввели несуществующий документ'
        for docs in documents:
            if docs["number"] == doc_number:
                owner = docs["name"]
        return owner


    def shelf(self, doc_number):
        """команда, которая спросит номер документа и выведет номер полки, на которой он находится"""
        for shelf_name in directories:
            if doc_number in directories[shelf_name]:
                return f'Номер полки: {shelf_name}'
        return 'Вы ввели несуществующий документ'

    def doc_list(self):
        """команда, которая выведет список всех документов в формате passport '2207 876234' 'Василий Гупкин'"""
        new_doc = []
        for doc_info in documents:
            new_doc.append(f'{doc_info["type"]} "{doc_info["number"]}" "{doc_info["name"]}"')
        return new_doc

    def add_info(self, type_d, doc_number, name, shelf_name):
        """команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип, имя владельца и номер полки, на котором он будет храниться."""

        if shelf_name not in directories:
            return 'Вы ввели неверный номер полки'
        else:
            documents.append({"type": type_d, "number": doc_number, "name": name})
            directories[shelf_name].append(doc_number)
            return 'Документ добавлен.'

    def del_doc(self, number):
        """команда, которая спросит номер документа и удалит его из каталога и из перечня полок"""
        for id, doc_num in enumerate(documents):
            if doc_num['number'] == number:
                documents.pop(id)
                return 'Документ удален'
        if number not in directories.values():
            return 'Такого документа нет'
        for key, values in directories.items():
            if number in values:
                values.remove(number)

    def move_doc(self, doc_num, shelf_name):
        """команда, которая спросит номер документа и целевую полку и переместит его с текущей полки на целевую."""
        if shelf_name not in directories:
            return 'Неверный номер полки'
        for nums in directories.values():
            if doc_num in nums:
                nums.remove(doc_num)
                directories[shelf_name] += [doc_num]
                return f'Документ перенесен в полку № {shelf_name}.'
            else:
                return 'Неверный номер документа'

    def add_shelf(self, shelf_name):
        """команда, которая спросит номер новой полки и добавит ее в перечень"""
        if shelf_name not in directories.keys():
            directories[shelf_name] = []
            return f' полка {shelf_name} создана'
        else:
            return f' полка {shelf_name} уже была создана'

    def main(self):
        user_input = input('Введите команду "p", "s", "l", "a", "d", "as", "m" или "q" ')
        if user_input == 'p':
            doc_number = input("Введите номер документа: ")
            return self.name_people(doc_number)
        elif user_input == 's':
            doc_number = input("Введите номер документа: ")
            return self.shelf(doc_number)
        elif user_input == 'l':
            return self.doc_list()
        elif user_input == 'a':
            doc_number = input("Введите номер документа: ")
            type_d = input('Введите тип документа: ')
            name = input('Введите имя и фамилию человека: ')
            shelf_name = input('Введите номер полки, куда необходимо записать данные: ')
            return self.add_info(type_d, doc_number, name, shelf_name)
        elif user_input == 'd':
            num_ = input('Введите номер документа для удаления ')
            return self.del_doc(num_)
        elif user_input == 'as':
            shelf_name = input("Введите номер новой полки: ")
            return self.add_shelf(shelf_name)
        elif user_input == 'm':
            doc_num = input("Введите номер документа: ")
            shelf_name = input('Введите номер полки, куда необходимо перенести данные: ')
            return self.move_doc(doc_num, shelf_name)
        elif user_input == 'q':
            return user_input
        else:
            return 'Ошибка ввода'

while True:
    secretary = Secretary('Lidia', 'Ivanova')
    result = secretary.main()
    if isinstance(result, list):
        for i in result:
            print(i)
    elif result == 'q':
        print('Работа программы завершена')
        break
    else:
        print(result)
