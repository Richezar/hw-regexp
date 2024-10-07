import re
import csv
with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

def group_name(contacts):
    full_name = " ".join(contacts[:3]).split()
    full_name += [''] * (3 - len(full_name))
    return full_name + contacts[3:]

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
      result = [contacts[0], contacts[1], contacts[2], contacts[3], contacts[4],
                re.sub(pattern, substitution, contacts[5]),
                contacts[6]]
      return result

normal_contacts = [group_name(i) for i in [create_contact(contact) for contact in contacts_list]]
result = del_duplicate(normal_contacts)

with open("phonebook.csv", "w", encoding="utf-8") as f:
    datawriter = csv.writer(f, delimiter=',', lineterminator="\r")
    datawriter.writerows(result)