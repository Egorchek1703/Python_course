### Конспект по уроку

В python, как и в JS, существуют классы для работы с ООП. Чтобы объявить класс нам необходимо использовать ключевое слово class, указать название класса, круглые скобки и двоеточие в конце данной строки (синтаксис похож на объявление функции)  
```
class Heroes():
    методы_класса
```  
  
Внутри класса, его методы объявляются как обычные функции, т.е. следующим образом:  
```
class Heroes():
    def attack():
        print("I've just attacked you!")
```  

В классах python существует обязательный метод \_\_init\_\_(self, ...). Данный метод является конструктором instance-ев данного класса, а именно, объектов (не словарей). Поля каждого instance-а класса - это параметры, передаваемые в данный метод, т.е., если мы хотим иметь шаблон для генерации с набором свойств (name, lvl, race, power), то нам необходим следующий метод \_\_init\_\_(self):  
```
class Heroes():
    def __init__(self, name, lvl, race, power):
        self.name = name
        self.lvl = lvl
        self.race = race
        self.power = power
```  
Когда мы указываем self.название_поля - мы задаем поле, которое будет содержать в себе передаваемый в данный метод параметр. Ключевое слово self - аналог слова this в JavaScript. Данное слово также указывает на тот объект, в контексте которого вызывается тот или иной метод класса.  
  
*Название класса пишется с большой буквы и не содержит символа "_". Для разделения слов используется PaskalCase*
Первым параметром в данный метод передается сам формирующийся instance данного класса (т.е. пустой объект, выделенный в области памяти) и далее, с помощью описания его полей, данный объект приобретает те или иные свойства.  
  
Помимо динамических свойтсв (т.е. тех которые мы передаем в конструктор при вызове класса), мы также можем назначать статические свойства данному объекту.
```
class Heroes():
    def __init__(self, name, lvl, race, power):
        self.name = name
        self.lvl = lvl
        self.race = race
        self.power = power
        self.health = 100
```  

Чтобы создать объект на основании класса необходимо в соответствующую переменную вложить вызов данного класса и передать при вызове необходимые параметры.  
Для классов также можно задавать методы, которые будут доступны в том числе и для объектов, созданных на основании этого класса:
```
class Heroes():
    def __init__(self, name, lvl, race, power):
        self.name = name
        self.lvl = lvl
        self.race = race
        self.power = power
        self.health = 100

    def show_hero_desc(self):
        description = self.name + " is a " + self.race + " and has:\n\tlevel: " + str(self.lvl) + "\n\tpower: " + str(self.power) 
        print(description)

first_hero = Heroes('Aracul', 1, 'witch', 125)
first_hero.show_hero_desc()
"""
Aracul is a witch and has:
        level: 1
        power: 125
"""
```  

**Заметим, что изменение свойств объекта возможно двумя способами: переназначением вручную в коде и использованием встроенных методов класса (наподобие set-еров в JavaScript). Способ через изменение свойств объекта с использрованием методов класса является более предпочтительным**  

```
class Heroes():
    
    ...

    def set_new_health(self, new_health):
        self.health = new_health
    
    ...

first_hero["health"] = 33      # Менее предпочтительный способ
first_hero.set_new_health(35)  # Более предпочтительный способ
```  
**Также стоит отметить, что на основании классов создаются именно объекты, а не словари, поэтому обращение к их свойствам реализовано только через точку ".". Обратиться к полям объекта через \["название_свойства"\] мы не сможем**  

```
dictionary["name"] # - обращение к полю словаря
object.name        # - обращение к полю объекта
```
*Ввиду того, что объявление классов - это всегда объемное удовольствие, стоит выносить данный процесс в модули*  
  
Классы в python как и в JavaScript могут наследоваться. Для примера объявим класс "Orcs" с родительским классом "Heroes". Для этого необходимо передать родительский класс в качестве параметра в дочерний класс. И внутри дочернего метода \_\_init\_\_ вызвать функцию super(), которая возвращает все свойства и методы родительского класса. Соответственно, данные свойства и методы сохраняться и для дочернего класса. В вызов метода super() нужно передать необходимые для родительского метода параметры.
```
class Orcs (Heroes):
    def __init__(self, name, lvl, race, power, armor_lvl):
        super().__init__(name, lvl, race, power)
        self.armor_lvl = armor_lvl
```  
*Пусть в нашей игре, орки имеют эксклюзивное свойство - наличие брони, поэтому добавим им уровень брони в свойства объекта с помощью синтаксиса выше*  
  
Теперь созданный на основе класса Orcs персонаж, будет иметь доступ и к методам класса Heroes и к методам класса Orcs, но при этом будет иметь дополнительное свойство "armor", актуальное только для класса Orcs:  
```
first_orc = Orcs("Orgun", 1, "Orc-warrior", 140, 5)
first_orc.show_hero_desc()
print( first_orc.armor )

first_orc = Orcs("Orgun", 1, "Orc-warrior", 140, 5)
first_orc.show_hero_desc()        # Orgun is a Orc-warrior and has: level: 1 power: 140
print( str(first_orc.armor_lvl) ) # 5
```  
  
Если мы хотим расширить функционал метода родительского класса, внутри дочернего, то нам необходимо просто пересоздать функцию с таким же названием и расширить её. Т.е. если мы хотим с помощью show_hero_desc() для орков выводить еще и уровень брони (armor_lvl), то нам необходимо:
```
class Orcs (Heroes):
    def __init__(self, name, lvl, race, power, armor_lvl):
        super().__init__(name, lvl, race, power)
        self.armor_lvl = armor_lvl
    
    def show_hero_desc(self):
        description = self.name + " is a " + self.race + " and has:\n\tlevel: " + str(self.lvl) + "\n\tpower: " + str(self.power) + "\n\tarmor_level: " + str(self.armor_lvl)
        print(description)

first_orc.show_hero_desc()
"""
Orgun is a Orc-warrior and has:
        level: 1
        power: 140
        armor_level: 5
"""
```
  
Если мы хотим задать поля которые нельзя изменить вручную из кода, т.е. не используя методы объекта, то его название стоит начать с двух нижних подчеркиваний "__"
```
class Orcs (Heroes):
    def __init__(self, name, lvl, race, power, armor_lvl):
        super().__init__(name, lvl, race, power)
        self.__armor_lvl = armor_lvl
    
    def show_hero_desc(self):
        description = self.name + " is a " + self.race + " and has:\n\tlevel: " + str(self.lvl) + "\n\tpower: " + str(self.power) + "\n\tarmor_level: " + str(self.__armor_lvl)
        print(description)

first_orc.__armor_lvl = 0    # Выдаст ошибку
first_orc.show_hero_desc()
```