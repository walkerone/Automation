'''
装饰器
定义：装饰器本身是函数（装饰其它函数），为其他函数添加附加功能
1 不能修改被装饰函数的源代码
2 不能被装饰函数的调用方式
实现装饰器的知识储备
1 函数即变量
2 嵌套函数
3 高阶函数
    a. 把一个函数当一个实参传个另一个函数（不修改被装饰函数的源代码为其添加功能）
    b. 返回值中包含函数名（不修改函数的调用方式）
高阶函数+嵌套函数===》装饰器
4 函数的嵌套和函数的调用的区别

列表生成式：使代码可以更简洁
在python中一边循环一边计算的机制称作生成器
生成器只有在调用的时候才会生成相应的数据,只记住当前位置数据
生成器只有 __next__方法，循环会一个一个的取生成下一个
生成器中yield的作用，生成器
yield保存函数的中断状态

可以直接作用于for循环的对象统称为可迭代对象，Iterable
一类是集合数据，如 list,tuple,dict,set,str
一类是gernerator,包括生成器和和带yield的generarot function
可以直接作用于for循环的对象称为可迭代对象， Iterable
可以使用isinstance 判断是否是Iterable对象


可以被next()函数调用并不断返回下一个值的对象成为迭代器，Iterator
可以使用isinstance 判断是否是Iterator生成器
把list,dict,str等Iterable等变成Iterarot可以使用 iter函数

pickele可以序列换所有python的文件类型

json dump时，读出时还用json的load
picke的dump对应pickle的load
不要dump多次
写程序只dump一次,只load一次
'''
