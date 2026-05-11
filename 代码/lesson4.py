import json
class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone


def add_contact(contacts):
    name = input("输入你的名字:")
    phone = input("输入你的电话号码:")
    contacts.append({"name": name, "phone": phone})
    print(f"已添加{name}")


def show_all(contacts):
    if not contacts:
        print("没有联系人")
        return
    for i,c in enumerate(contacts):
        print(f"{i+1}. {c['name']} - {c['phone']}")

def search(contacts):
    keyword = input("输入要搜索的名字:")
    found = []
    for c in contacts:
        if keyword in c["name"]:
            found.append(c)
    if found:
        for c in found:
            print(f"{c['name']} - {c['phone']}")
    else:
        print("没有找到匹配的联系人")

def save(contacts):
    with open("contacts.json","w",encoding="utf-8") as f:
        json.dump(contacts,f,ensure_ascii=False)
    print("已保存联系人到contacts.json")


contacts = []

while True:
    print("1. 添加联系人")
    print("2. 显示所有联系人")
    print("3. 搜索联系人")
    print("4. 保存联系人")
    print("5. 退出")
    choice = input("请选择操作:")
    if choice == "1":
        add_contact(contacts)
    elif choice == "2":
        show_all(contacts)
    elif choice == "3":
        search(contacts)
    elif choice == "4":
        save(contacts)
    elif choice == "5":
        print("退出程序")
        break
    else:
        print("无效的选择，请重新输入")


