#! -*- coding:utf-8 -*-
data = {
    "北京": {
        "昌平": {
            "沙河": {"oldboy", "test"},
            "天通苑": {"链家地产", "我爱我家"}
        },
        "朝阳": {
            "望京": {"奔驰", "陌陌"},
            "国贸": {"CICC", "HP"},
            "东直门": {"Advent", "飞信"},
        },
        "海淀": {},
    },
    '山东': {
        "德州": {},
        "青岛": {},
        "济南": {},
    },
    "广东": {
        "东莞": {},
        "常熟": {},
        "佛山": {},
    },
}
flag_exit = False
while not flag_exit:
    for i in data:
        print(i)
    choice = input("选择第一层中的的哪一个")
    if choice in data:
        print(data[choice])
        choice2 = input("选择第二层中的的哪一个")
        while not flag_exit:
            if choice2 in data[choice]:
                print(data[choice][choice2])
                c3 = data[choice][choice2]
                choice3 = input("选择第三层中的的哪一个")
                while not flag_exit:
                    if choice3 in c3:
                        print(c3[choice3])
                        break
                    elif choice3 == 'b':
                        break
                    elif choice3 == 'q':
                        flag_exit = True
            elif choice2 == "b":
                break
            elif choice2=='q':
                flag_exit=True

    elif choice == "b":
        break
    elif choice == "q":
        break
