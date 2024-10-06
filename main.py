import re
import csv
with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

def group_name(contacts):
    result_list = contacts
    for idx, text in enumerate(contacts):
        if idx == 0:
            continue
        fio = text[0].split()
        if len(text[0].split()) == 2:
            result_list[idx][0] = fio[0]
            result_list[idx][1] = fio[1]
        elif len(text[0].split()) == 3:
            result_list[idx][0] = fio[0]
            result_list[idx][1] = fio[1]
            result_list[idx][2] = fio[2]
        elif len(text[1].split()) == 2:
            io = text[1].split()
            result_list[idx][1] = io[0]
            result_list[idx][2] = io[1]
    return result_list

def del_duplicate(contacts):
    for contact in contacts:
        lastname = contact[0]
        firstname = contact[1]
        surname = contact[2]
        for ncontact in contacts:
            nlastname = ncontact[0]
            nfirstname = ncontact[1]
            nsurname = ncontact[2]
            if lastname == nlastname and firstname == nfirstname and surname == nsurname:
                if contact[3] == '':
                    contact[3] = ncontact[3]
                if contact[4] == '':
                    contact[4] = ncontact[4]
                if contact[5] == '':
                    contact[5] = ncontact[5]
                if contact[6] == '':
                    contact[6] = ncontact[6]
            elif lastname == nlastname and firstname == nfirstname:
                if contact[2] == '':
                    contact[2] = ncontact[2]
                if contact[3] == '':
                    contact[3] = ncontact[3]
                if contact[4] == '':
                    contact[4] = ncontact[4]
                if contact[5] == '':
                    contact[5] = ncontact[5]
                if contact[6] == '':
                    contact[6] = ncontact[6]
    result_list = []
    for i in contacts:
        if i not in result_list:
            result_list.append(i)
    return result_list

def create_contact(contacts):
  pattern = r'(\+7|8)*[\s\(]*(\d{3})[\)\s-]*(\d{3})[-]*(\d{2})[-]*(\d{2})[\s\(]*(доб\.)*[\s]*(\d+)*[\)]*'
  substitution = r'+7(\2)\3-\4-\5 \6\7'
  new_list = []
  for item in contacts:
      full_name = ' '.join(item[:3]).split(' ')
      result = [full_name[0], full_name[1], full_name[2], item[3], item[4],
                re.sub(pattern, substitution, item[5]),
                item[6]]
      new_list.append(result)
  return new_list

result = del_duplicate(group_name(create_contact(contacts_list)))

with open("phonebook.csv", "w", encoding="utf-8") as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(result)