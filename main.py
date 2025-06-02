from user import UserManager
from os import system

manager = UserManager()

def menu():
    system("cls")
    print("유저관리 프로그램")
    print("--{ 메뉴를 선택해주세요 }--")
    print("1. 유저정보 등록")
    print("2. 유저정보 출력")
    print("3. 유저정보 초기화")
    print("4. 유저정보 검색")
    print("5. 종료")

def command(x):
    if x == 1:
        system("cls")
        addUser(input("이름: "), input("이메일: "))
        
    elif x == 2:
        system("cls")
        user_print()
        
    elif x == 3:
        system("cls")
        manager.reset_users()
        print("유저 정보가 초기화되었습니다.")
        back_menu()
    
    elif x == 4:
        system("cls")
        name = input("이름을 입력해주세요\n입력: ")
        user = manager.find_user(name)
        if isinstance(user, dict):
            print(f"찾은 유저: {user['username']} - {user['email']}")
        else:
            print(user)
        back_menu()
        
    elif x == 5:
        print("프로그램을 종료합니다.")
        exit()
        
    else:
        print("잘못 입력하셨습니다.")
        back_menu()

def addUser(x, y):
    manager.add_user(x, y)
    print("유저가 추가되었습니다.")
    back_menu()

def user_print():
    users = manager.list_users()
    if users:
        for user in users:
            print(f"{user['username']} - {user['email']}")
    else:
        print("등록된 유저가 없습니다.")
    back_menu()

def back_menu():
    print("\n[Enter]를 누르면 메뉴로 돌아갑니다.")
    input()

def main():
    while True:
        menu()
        try:
            x = int(input("\n입력: "))
            command(x)
        except ValueError:
            print("숫자만 입력해주세요.")
            back_menu()

if __name__ == "__main__":
    main()
