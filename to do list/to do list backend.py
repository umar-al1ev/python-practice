import json
try:
    with open("data.json", "r", encoding="utf-8") as f:
        data = json.load(f)
except:
    data =[]

def add_data():
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def add_task():
    task = input('gorevleri giriniz:')
    new_task = {'id': len(data) + 1,
                'task': task, }
    data.append(new_task)
    print('GOREVINIZ EKLENDI')
    add_data()

def remove_task():
    for item in data:
        print(f"{item['id']}. {item['task'].capitalize()}")

    number_task = int(input('Silmek istediğiniz görev sayısını giriniz: '))

    for item in data:
        if item['id'] == number_task:
            data.remove(item)
            print('ISTEDIGINIZ GOREV SILINDI')
            break
    else:
        print('BOYLE BIR RAKAMLI GOREV YOKTUR')
        return

    for i, item in enumerate(data, start=1):
        item["id"] = i

    add_data()
def show_data():
    for item in data:
        print(f'{item["id"]}. {item["task"].capitalize()}')

def del_data():
    data.clear()
    add_data()


while True:
    print(f'1: GOREV EKLEMEK\n2: GOREV SILMEK\n3:TUM GOREVLER\n4:TUM GOREVLERI SILMEK\n5: CIKIS YAPMAK')
    sayi = int(input('SAYI GIR :'))
    if sayi == 1:
        add_task()
    elif sayi == 2:
        remove_task()
    elif sayi == 3:
        show_data()
    elif sayi == 4:
        del_data()
    elif sayi == 5:
        break







