def menu():
    while True:
        print(60 * '-')
        print('|1.입력|2.목록|3.검색|4.삭제|5.수정|0.프로그램종료|')
        print(60 * '-')
        menu = input('메뉴선택>')
        if not menu.isnumeric():
            print('숫자로 입력하세요.')
            continue
        else:
            menu = int(menu)
            if menu == 0:
                print('프로그램을 종료합니다.')
                break
            elif menu == 1:
                pass
            elif menu == 2:
                pass
            elif menu == 3:
                pass
            elif menu == 4:
                pass

if __name__ == '__main__':
    menu()