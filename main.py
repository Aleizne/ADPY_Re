from pprint import pprint
import re
import csv
# читаем адресную книгу в формате CSV в список contacts_list

with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)


# pprint(contacts_list)

# Здесь постарался четко следовать предложенной в условии ДЗ логике: 1, 2, 3.

# Выполняем задание №1

def fullname_change(contacts) -> list:
    goodname_list = []
    for value in contacts:
        fullname = ' '.join(value[:3]).split(' ')
        while "" in fullname:
            fullname.remove("")
        while len(fullname) < 3:
            fullname.append("")
        templist = [fullname[0], fullname[1], fullname[2], value[3], value[4]]
        goodname_list.append(templist)
    return goodname_list


# Выполняем задание №2

def contact_adder(contacts, goodname):
    pattern_comp = re.compile(r'(\+7|8)*[\s\(]*(\d{3})[\)\s-]*(\d{3})-*(\d{2})-*(\d{2})[\s\(]*(доб\.)*\s*(\d+)*\)*')
    subst = r'+7(\2)\3-\4-\5 \6\7'
    counter = 0
    for value in contacts:
        goodname[counter].extend([pattern_comp.sub(subst, value[5]), value[6]])
        counter += 1
    return goodname


# Выполняем задание №3 без itertools и третьего вложенного цикла

def twin_corrector(goodlist) -> list:
    res = []
    for indx_a in goodlist:
        last_name = indx_a[0]
        first_name = indx_a[1]
        for indx_b in goodlist:
            name_2 = indx_b[0]
            surname_2 = indx_b[1]
            if last_name == name_2 and first_name == surname_2:
                if indx_a[2] == "":
                    indx_a[2] = indx_b[2]

                if indx_a[3] == "":
                    indx_a[3] = indx_b[3]

                if indx_a[4] == "":
                    indx_a[4] = indx_b[4]

                if indx_a[5] == "":
                    indx_a[5] = indx_b[5]

                if indx_a[6] == "":
                    indx_a[6] = indx_b[6]

    for value in goodlist:
        if value not in res:
            res.append(value)
    return res


if __name__ == '__main__':
    homework_1st = fullname_change(contacts_list)
    # pprint(homework_1st)
    homework_2st = contact_adder(contacts_list, homework_1st)
    # pprint(homework_2st)
    homework_3d = twin_corrector(homework_2st)
    pprint(homework_3d)

    with open("phonebook.csv", "w", encoding="utf-8") as f:
        datawriter = csv.writer(f, delimiter=',')
        # Вместо contacts_list подставьте свой список
        datawriter.writerows(homework_3d)
