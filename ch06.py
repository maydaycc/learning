# -*- coding=utf-8 -*-
__author__ = 'mayday_cc'

"""
(1) 创建一个名为 Thing 的空类并将它打印出来。接着，创建一个属于该类的对象 example，
同样将它打印出来。看看这两次打印的结果是一样的还是不同的？
(2) 创建一个新的类 Thing2，将 'abc' 赋值给类特性 letters，打印 letters。
(3) 再创建一个新的类， 叫作 Thing3。这次将 'xyz' 赋值给实例（对象）特性 letters，并
试着打印 letters。看看你是不是必须先创建一个对象才可以进行打印操作？
(4) 创建一个名为 Element 的类，它包含实例特性 name、 symbol 和 number。使用 'Hydrogen'、
'H' 和 1 实例化一个对象。
(5) 创建一个字典，包含这些键值对： 'name': 'Hydrogen'、 'symbol': 'H' 和 'number': 1。
然后用这个字典实例化 Element 类的对象 hydrogen。
(6) 为 Element 类定义一个 dump() 方法，用于打印对象的特性（ name、 symbol 和 number）。
使用这个新定义的类创建一个对象 hydrogen 并用 dump() 打印。
(7) 调用 print(hydrogen)，然后修改 Element 的定义，将 dump 方法的名字改为 __str__。
再次创建一个 hydrogen 对象并调用 print(hydrogen)，观察输出结果。
(8) 修改 Element 使得 name、 symbol 和 number 特性都变成私有的。为它们各定义一个 getter
属性来返回各自的值。
(9) 定义三个类 Bear、 Rabbit 和 Octothorpe。对每个类都只定义一个方法 eats()，分别返
回 'berries'（ Bear）、 'clover'（ Rabbit）和 'campers'（ Octothorpe）。为每个类创建
一个对象并输出它们各自吃的食物（调用 eats()）。
(10) 定义三个类 Laser、 Claw 以及 SmartPhone。每个类都仅有一个方法 does()，分别返回
'disintegrate'（ Laser）、 'crush'（ Claw） 以 及 'ring'（ SmartPhone）。 接 着， 定 义
Robot 类，包含上述三个类的实例（对象）各一个。给 Robot 定义 does() 方法用于输
出它各部分的功能。
"""


class Thing:
    pass


class Thing2:
    letters = 'abc'


class Thing3:
    def __init__(self):
        self.letters = 'xyz'


class Element:
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number

    def dump(self):
        print(self.name, self.symbol, self.number)

    def __str__(self):
        return "{0} {1} {2}".format(self.name, self.symbol, self.number)


class ElementPrivate:
    def __init__(self, name, symbol, number):
        self.__name = name
        self.__symbol = symbol
        self.__number = number

    @property
    def name(self):
        return self.__name

    @property
    def symbol(self):
        return self.__symbol

    @property
    def number(self):
        return self.__number

    def __str__(self):
        return "{0} {1} {2}".format(self.name, self.symbol, self.number)


class Bear:
    def eats(self):
        return 'berries'


class Rabbit:
    def eats(self):
        return 'clover'


class Octothorpe:
    def eats(self):
        return 'campers'


class Laser:
    def does(self):
        return 'disintegrate'


class Claw:
    def does(self):
        return 'crush'


class SmartPhone:
    def does(self):
        return 'ring'


class Robot:
    def __init__(self):
        self.laser = Laser()
        self.claw = Claw()
        self.smartphone = SmartPhone()

    def does(self):
        return '''I have many attachments:
        My laser, to %s.
        My claw, to %s.
        My smartphone, to %s.''' % (self.laser.does(),
                                    self.claw.does(),
                                    self.smartphone.does() )


if __name__ == "__main__":
    print(Thing)
    example = Thing()
    print(example)
    print(Thing2.letters)

    # print(Thing3.letters)
    example3 = Thing3()
    print(example3.letters)

    elem = Element('Hydrogen', 'H', 1)
    dic = {'name': 'Hydrogen', 'symbol': 'H', 'number': 1}
    elem2 = Element(**dic)
    print(elem2)
    hydrogen = Element(**dic)
    hydrogen.dump()
    print(hydrogen)
    newelem = ElementPrivate(**dic)
    print(newelem)

    b = Bear()
    r = Rabbit()
    o = Octothorpe()
    print(b.eats())
    print(r.eats())
    print(o.eats())

    robbie = Robot()
    print(robbie.does())
