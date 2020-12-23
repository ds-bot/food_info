class FoodInfo:
    '''
    Класс для удобного хранения калорийности продуктов.
    '''

    def __init__(self, proteins, fats, carbohydrates):
        self.proteins = proteins
        self.fats = fats
        self.carbohydrates = carbohydrates

    def get_proteins(self):
        return self.proteins

    def get_fats(self):
        return self.fats

    def get_carbohydrates(self):
        return self.carbohydrates

    def get_kcalories(self):
        self.kcalories = 4 * self.proteins + 9 * self.fats + 4 * self.carbohydrates
        return self.kcalories

    def __add__(self, other):
        p = self.proteins + other.proteins
        f = self.fats + other.fats
        c = self.carbohydrates + other.carbohydrates
        return FoodInfo(p, f, c)

    def __eq__(self, other):
        if self.kcalories == other.kcalories:
          return True
        else:
          return False

    def __ne__(self, other):
        if self.kcalories != other.kcalories:
          return True
        else:
          return False

    def __it__(self, other):
        if self.kcalories < other.kcalories:
          return True
        else:
          return False

    def __gt__(self, other):
        if self.kcalories > other.kcalories:
          return True
        else:
          return False

    def __le__(self, other):
        if self.kcalories <= other.kcalories:
          return True
        else:
          return False

    def __qe__(self, other):
        if self.kcalories >= other.kcalories:
          return True
        else:
          return False

food1 = FoodInfo(25,50,75)
food2 = FoodInfo(75,50,25)
food3 = food1 + food2
print(food1.get_proteins(), food1.get_fats(),
food1.get_carbohydrates(), food1.get_kcalories())
print(food2.get_proteins(), food2.get_fats(),
food2.get_carbohydrates(), food2.get_kcalories())
print(food3.get_proteins(), food3.get_fats(),
food3.get_carbohydrates(), food3.get_kcalories())

result = food1==food2
result1 = food3!=food1
result2 = food3>food1
result3 = food2<food3
result4 = food1>=food2
result5 = food2<=food1

print(result,result1,result2,result3,result4,result5)
