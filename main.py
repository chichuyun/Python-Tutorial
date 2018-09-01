# -*- coding: utf-8 -*-      # 设置文本编码格式为utf-8
"""
Created on Thu Apr 20 20:10:01 2017

@author: Rupert in USTC  :)  Aha!!

#  python安装建议用python3版本的Anaconda安装管理python,编辑器推荐用eclipse+PyDev或者spyder 
#  这里是基于python3的一个小总结(主要是说明python中关键字的用法,这里除过global和nonlocal这两个关键字的说明,也不建议使用)
#  python是严格缩进的,4个空格(不要用Tab键,除非设置Tab为4个空格),同缩进就是同一级语句
#  python执行效率有点慢(这里推荐julia语言(提醒：百度的时候一定要打全julia language进行搜索,要不然搜索结果不一定是你想要的))
#  python是利用pip或者conda管理packages的,类似ubuntu中的apt-get命令(pip和conda官方源都比较慢,建议换为科大或者清华镜像中的源(pip是pypi源))
#  pip往往会因为兼容问题出错,这就需要到(www.lfd.uci.edu/~gohlke/pythonlibs/)中下载对应版本的whl包(已经编译好)进行安装(linux下很少出现编译错误)

常用的数据处理模块有：numpy(基本数值),scipy(数值统计),sympy(符号计算),pandas(数据处理),statsmodel(统计模型),sklearn(机器学习),tensorflow(深度学习)
常用的数据可视化库有：matplotlib(一般绘图,2D,3D),boken(基于mpl,操作较为简便),seaborn(基于mpl的统计图),yt(可视化数据),mayavi(3D) 
其他常用的库：csv(读取文件数据),urllib(内建的爬虫库),requests(第三方爬虫库),beautifulsoup4(解析html文档),re(正则表达式),time,datetime,PyQt5(编写界面程序)
            numba(其中的jit可以加快函数内循环多次执行的遍历效率),rpy2(调用r语言),moviepy(简单动画),vapory(调用pov-ray),deap(优化算法库)......

#  能力有限,难免出错,限于篇幅,还有很多细节没有说明
"""

import numpy as np    # 导入numpy模块并命名为np
from numba import jit   # 从一个模块中导入子模块或者函数和类
from sympy import *  # 导入这个模块下所有的子模块或者函数和类

""" python中常用的数据结构为元组tuple(),列表list[],字典dict{}......处理数据常用numpy下的array类型和pandas下的DataFream类型 """
""" python中字符串用单引号和双引号是等价的,区别在于如果要输出单引号,那就得用双引号定义字符串 """
z = [2,1,'a',[1,2],2,3.5,5]   # 定义一个list,list中的元素可以是任何数据类型(本例中z会经常被调用)
del z[3]  # del语句用于删除变量(这里删除了z的第4个元素"[1,2]")
f = lambda x: 2*np.sqrt(x)  # 定义一个简单函数(类似matlab中的@定义方法)

""" python中一共有两种循环方式,for循环和while循环 """
""" python中的try...except...else...finally语句类似于matlab中的try...catch...end """
for m in z:  # m依次遍历z中的元素,遍历完终止循环(或者遇到break)
    try:  # 尝试运行下列语句,如果报错执行except(可以指定错误)(本例中,当m读取到'a'的时候就会报错,因为字符无法和数字进行比较)
        if m > 4:  # 条件语句(其中不等于是!=,和c/c++中的比较算符都一样(python就是用c语言编写的))
            if m > 100:
                raise ValueError("m can't bigger than 100 ")  # 抛出异常   # 这里的ValueError是内建的类,还有KeyError等等,其他的需要自己定义
            break  # 终止循环
        elif m < 1.5:  # 条件语句if else的缩写
            print("result(m**2):", m**2)  # 在python3中print是函数,python2.7中是语句       # python中乘方是**而不是^
            assert m > 0  # 断点测试,不满足会抛出AssertionError错误
        else: # 最后一个else
            print("result(f(m)):", f(m))  
    except: # 可缺省(但是不能只有try而没有后续操作)
        pass  # 空语句,方便编写程序
    else:  # 如果try中的语句执行不报错,则会执行else下的语句(可缺省)
        continue  #　直接进行下次循环,
    finally:  # 无论try下语句报不报错,都会执行finally下的语句(可缺省)(常用于无论有没有出错的情况下关闭数据文档)
        print("test finally", m)
else:
    print("No break!")  # 如果for中没有因为break中断,则会执行else语句
m=0 if(z[0]>1) else 5 # 这里类似C/C++中的?:表达式，但只有赋值功能,若条件满足m等于0,否则就为5
while isinstance(z[m],int):  # while循环语句,当满足时进行循环      # isinstance函数可以判断某个值是否为所给数据类型,例如这里就是判断z的某个元素是不是整数类型(int)
    if z[m]==1 is True:  # 这里加True有点多此一举,仅是作为一个bool类型的例子
        print("test while", True)  # 真为True,假为False
    else:
        print("test while", False) 
    m=m+1

def test_yield(n=None):   # 定义复杂函数,函数中还可以定义函数     # 函数中可以定义默认值,直接等号实现(若另外赋值,该值会被覆盖)
    if n is None:  # None是Nonetype类型(当然也可以直接设初值为n=5而不是n=None)
        n = 5
    if n is not (5 and (7 or 8)):  # 这里仅是举个例子,在这里会导致输出比较奇怪
        n = 5     # and,or,not 是python中的 和,或,非 
    for m in range(n):   #　定义循环,m遍历完z中的所有的值后,终止循环             # range是生成0到n-1的一个生成器函数       # 注意python中list索引指标是从0开始的
        yield m   #　这个是定义生成器,每次定义调用这个函数都会返回下一个值(节省内存)
        
x = test_yield(6)  # 定义了一个具体的生成器
for m in x:   # 依次输出list中的元素值
    print("test yield:%2.1f,%2.3f"%(m, m**2))  # print也可以用类似于c/c++或fortran中的输出格式控制进行输出(注意前后都是%号,中间也没有逗号)

def ss(a, x=[]):  # 通过默认变量定义静态变量(多运行几遍ss(1)看效果)
    x.append(a)   # 用默认变量的时候要注意这里
    return a, x

import csv  # csv模块可以读写表格数据(xls,csv,txt文档)   # 这里往往需要设置读写的编码格式(ascii,utf-8...),不然会出问题
with open("example.csv", "w") as cf1:  # 写入文件(python2.7中和这个不同,不需要with...as...),如果是读取文档则把"w"改为"r"
    csvreader = csv.writer(cf1)  # 写入文档,如果是读取文档则为csv.reader(cf1)
    """ 其他语句 """   # 处理数据的语句
    cf1.close()  # 执行完之后释放内存

"""  前后有两个下划线的函数为python中class的内建函数,有__init__,__call__,__str__,__dir__等等  
            还有很多其他的类用法,class的继承问题等等,这里不做讨论
"""
class TestClass(object):  # 定义类,继承于object,也可以没有object,但是官方建议加
    """ 这是一个测试用类 """
    def __init__(self, x, y, zn):  # 这个内建函数用于初始化类(self不可缺省,self为实例方法)(类方法和静态方法的第一个参数为cls)
        self.x, self.y, self.zn = x, y, zn  # 逗号隔开为python中的一种数据结构元组,可以同时被赋值,以下函数中要用self.变量名进行计算处理                                         
    def area(self):  # 这里定义一个面积函数作为例子
        return self.x*self.y  # return用于返回值,不同于yield(多返回值函数可以用元组进行操作)
    @jit  # 这是一个函数修饰符(jit是numba下的一个函数),内建的还有@classmethod,@staticmethod等,也可以是自己定义的一个函数 
    def sum(self):  # 这里定义一个求和函数(对0,1...zn的一个求和)    # 加了@jit之后在这里的summ(self)函数就变为了jit(summ(self)),可以比较方便的进行函数嵌套        
        zm = 0                                                 # 这里解释@修饰符并不是很准确,但是按照嵌套理解并不会有什么大的问题,@还可以修饰类
        for m in range(self.zn):
            zm = zm + m 
        return zm
    def sumeven(self):   # 这里定义一个求和函数(对0,2...zn的一个求和,小于zn的所有偶数求和)(%号作用于数字就是取余)
        zx = [x for x in range(self.zn) if x%2==0]  # 可以直接把for和if语句写进list中,产生一个满足条件的list(这里也可以没有条件语句)
        return np.sum(zx)                               # 这样的执行效率较高,较为简单的循环语句建议直接写到list当中  
    @classmethod  # 类方法的修饰符
    def test_classmethod(cls):  # 只是一个类方法(cls指向类自己)(self指向实例本身)
        print("test classmethod")   # self和cls也可以是其他名称,不过这些都约定成俗了
    
Area = TestClass(5, 7, 10)  # 实例化一个类   　 # 另外python中是区分大小写的
print("Area is：", Area.area(), "\nSum(zn) = " , Area.sum())  # 输出这个例子
print(TestClass.__doc__)  # 这个可以输出class或者def下的"""中的内容,一些函数,类,模块不会使用的时候就可以利用这个方法查看说明

if __name__=="__main__":  # 如果这个.py文件不是被import调用的,而是自己运行的,就会执行if下的语句
    TestClass.test_classmethod()  # 类方法是实例和类都可以调用的
    print("Area.sumeven:", Area.sumeven())
else:  # 如果是被import调用的,就会执行else下的语句
    print("import successfully")
