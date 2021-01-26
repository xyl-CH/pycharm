from python_pratice.homework_oop.animal import Animals

"""
比如创建一个类（Animal）【动物类】，类里有属性（名称，颜色，年龄，性别），
类方法（会叫，会跑）
创建子类【猫】，继承【动物类】，
重写父类的__init__方法，继承父类的属性，
添加一个新的属性，毛发 = 短毛，
添加一个新的方法， 会捉老鼠，
重写父类的【会叫】的方法，改成【喵喵叫】
"""


class Cat(Animals):

    def __init__(self, nimal_name, animal_colour, animal_age, animal_sex, animal_hail):
        self.animal_hail = animal_hail
        super().__init__(nimal_name, animal_colour, animal_age, animal_sex)
        print(f"动物名字：{self.animal_name}\n动物颜色：{self.animal_colour}\n"
              f"动物年龄: {self.animal_age}\n动物性别: {self.animal_sex}\n"
              f"动物毛发: {self.animal_hail}")

    def call(self, animal_call):
        self.animal_call = animal_call
        print(f"what dose the {self.animal_name} say ? {self.animal_call}")

    def skill(self):
        print(f"我是可爱的{self.animal_name},会捉老鼠。喵~")


if __name__ == '__main__':
    cat = Cat('cat','yellow',2,'male','short hail')
    cat.call('喵喵喵喵喵喵喵喵喵喵喵喵')
    cat.run()
    cat.skill()
