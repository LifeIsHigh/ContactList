# # # # # Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных.
# # # # # Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных


from os import path

file_base = "base.txt"
last_id = 0
all_data = []


if not path.exists(file_base):
    with open(file_base, "w", encoding="utf-8") as _:
        pass


def read_records():
    global last_id, all_data

    with open(file_base, encoding="utf-8") as f:
        all_data = [i.strip() for i in f]
        if all_data:
            last_id = int(all_data[-1].split()[0])
            return all_data
    return []


def show_all():
    if all_data:
        print(*all_data, sep="\n")
    else:
        print("Empty data")


def AddRecords():
    global last_id, all_data

    with open(file_base, "a", encoding="utf-8") as f:
        last_id = last_id + 1
        f.write(str(last_id) + ' ')
        all_data.append(f.write(input('Введите новую строку: \n') + '\n'))
    return []


def SearchRecords():
    global last_id, all_data
    DelID = 0
    with open(file_base, "r", encoding="utf-8") as f:
        Data = (input("Enter your first or last name to search for a contact: "))
        for i in f:
            if i.split()[1] == Data:
                print(i, end="")
            elif i.split()[2] == Data:
                print(i, end="")
    return []


def DeleteRecord():
    global last_id, all_data
    
    with open(file_base, "r", encoding="utf-8") as f:
        print(*all_data, sep="\n")
        BuferData = all_data
        DelID = int(input("Enter ID of the contact you want to delete: "))
        with open(file_base, "w", encoding="utf-8") as ff:
            for i in BuferData:
                if int(i.split()[0]) != DelID:
                    ff.writelines(i + '\n')
    return []  


def ChangeRecords():
    global last_id, all_data

    with open(file_base, "r", encoding="utf-8") as f:
        print(*all_data, sep="\n")
        BuferData = all_data
        DelID = int(input("Enter ID of the contact you want to change: "))
        with open(file_base, "w", encoding="utf-8") as ff:
            for i in BuferData:
                if int(i.split()[0]) == DelID:
                    ff.writelines(str(DelID) + ' ' + str(input('Enter new contact change: ')) + '\n')
                else:
                    ff.writelines(i + '\n')
    return []


def main_menu():
    play = True
    while play:
        read_records()
        answer = input("Phone book:\n"
                       "1. Show all records\n"
                       "2. Add a record\n"
                       "3. Search a record\n"
                       "4. Change\n"
                       "5. Delete\n"
                       "6. Exp/Imp\n"
                       "7. Exit\n")
        match answer:
            case "1":
                show_all()
            case "2":
                AddRecords()
            case "3":
                SearchRecords()
            case "4":
                ChangeRecords()
            case "5":
                DeleteRecord()
            case "6":
                pass
            case "7":
                play = False
            case _:
                def m_menu():
                    Func = True
                    while Func:
                        read_records()
                        answer = input("Phone book:\n"
                                       "1. Change\n"
                                       "2. Delete\n"
                                       "3. Exit to main\n")
                        match answer:
                            case "1":
                                ChangeRecords()
                                # ChangeRecords()
                            case "2":
                                SearchRecords()
                                # DeleteRecord()
                            case "3":
                                Func = False
                            case _:
                                print("Try again!\n")


                m_menu()

main_menu()