from user import UserManager

def main():
    manager = UserManager()

    # 사용자 추가
    manager.add_user("siwoo", "siwoo@example.com")
    manager.add_user("yuna", "yuna@example.com")

    # 사용자 목록 출력
    for user in manager.list_users():
        print(f"{user['username']} - {user['email']}")

if __name__ == "__main__":
    main()
