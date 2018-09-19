# Author:zhang
# -*- coding:utf-8 -*-
# product_list = [
#     ('iphone', 5800),
#     ('Mac Pro', 9800),
#     ('Bike', 800),
#     ('Watch', 10600),
#     ('Coffice', 31),
#     ('Alex Python', 81)
#
# ]
file=r'H:\walker\review_code\day2\product_list'
file1=r'H:\walker\review_code\day2\shpping_car'
aa=open(file,'r')
product_list=aa.read()


shopping_list = []  # 购买的商品空列表


salary = input("please input your salary")
if salary.isdigit():  # 如果是数字
    salary = int((salary))
    while True:
        for index, iterm in enumerate(product_list):  # enmurate
            print(index, iterm)
        user_choice = input("what you buy number:")
        if user_choice.isdigit():
            user_choice = int(user_choice)
            if user_choice < len(product_list) and user_choice > -1:
                p_item = product_list[user_choice]
                if p_item[1]<salary:
                    shopping_list.append(p_item)
                    salary-=p_item[1]
                    print("add %s to your shopping cart,your current balance is \033[31;1m%s\033[0m " % (p_item,salary))
                    bb=open(file,'w+')
                    bb.write()
                else:
                    print("\033[41;1m 你的余额只剩 %s 还买个个毛线'\033[0m" % salary)
            else:
                print('此商品不 存在')
        elif user_choice == 'q':
            print('-----shopping_list------')
            for p in shopping_list:
                print(p)
                print('your current salary is %s ' % salary)
            exit()


        else:
            print('此商品不存在')



else:
    print('请输入数字')

aa.close()