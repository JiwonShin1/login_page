
def main():
    userid = input("Enter userID: ")
    userpw = input("Enter userPW: ")


    arr2_lines = []
    with open("user.txt") as userDB:
        lines = userDB.readlines()
    for line in lines:
        arr2_lines.append([line[0:15], line[15:30]])


    access = False
    for user, password in arr2_lines:
        if user.strip() == userid and password.strip() == userpw:
            print('로그인 성공!')
            access =  True
            break
    if access == False:
        print('시스템 권한이 없습니다!')



if __name__ == '__main__':
    main()