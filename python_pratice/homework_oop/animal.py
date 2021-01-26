"""
比如创建一个类（Animal）【动物类】，类里有属性（名称，颜色，年龄，性别），
类方法（会叫，会跑）
创建子类【猫】，继承【动物类】，
重写父类的__init__方法，继承父类的属性，
添加一个新的属性，毛发 = 短毛，
添加一个新的方法， 会捉老鼠，
重写父类的【会叫】的方法，改成【喵喵叫】
"""


# 定义Animal类,驼峰命名法
class Animals:
    # 定义类属性
    # animal_name = "fox"
    # animal_colour = "white"
    # animal_age = 0
    # animal_sex = "male"

    # def __init__(self):
    #     self.animal_name = 'fox'
    #     self.animal_colour = 'yellow'
    #     self.animal_age = 2
    #     self.animal_sex = 'male'
    #
    def __init__(self, animal_name, animal_colour, animal_age, animal_sex):
        self.animal_name = animal_name
        self.animal_colour = animal_colour
        self.animal_age = animal_age
        self.animal_sex = animal_sex

        # print(animal_name, animal_colour, animal_age, animal_sex)

    # 神奇动物怎么叫
    def call(self):
        print(f"what dose the {self.animal_name} say ?Ring-ding-ding-ding,Ringdingdingdingding")

    # 神奇动物怎么跑
    def run(self):
        print(f"How does the {self.animal_name} run ? Chasing mice, Wa-pa-pa-pa-pa-pa-pow")

    # 动物信息卡
    def IdCard(self):
        print(f"动物名字：{self.animal_name}\n动物颜色：{self.animal_colour}\n"
              f"动物年龄: {self.animal_age}\n动物性别: {self.animal_sex}")


if __name__ == '__main__':
    animal = Animals('fox', 'yellow', 2, 'male')
    animal.call()
    animal.run()
    animal.IdCard()
    # animal = Animals()
    # animal.IdCard()
    # animal.call()
    # animal.run()
