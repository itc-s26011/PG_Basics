numbers = [3, 7, 15, 20, 25]

while True:

    value = input("数字を入力してください('q'で終了)：")

    if value == "q":
        break

    try:
        num = int(value)

    except ValueError:
        print("数字か'q'を入力してください")

    else:
        if num in numbers:
            # a)
            print("正解")

        else:
            # b)
            print("不正解")
