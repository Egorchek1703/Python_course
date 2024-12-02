### Конспект по уроку

В python цикл "for ... in ..." имеет следующий синтаксис:
```
for имя_переменной in range(начальная_граница, конец, шаг):
    тело_цикла
#---------------------
for i in range(0, 10):
    print(i)
```  
*Важное замечание: цикл не включает последнюю указанную границу, т.е. раюотает по условию **i < 10**,  поэтому, если необходимо вывести последнее значение, то можно использовать запись "10 + 1"*  

Шаг цикла, передается третим параметром и может быть изменён:
```
for i in range (0, 100 + 1, 20):
    print(i) # 0 20 40 60 80 100
```  

Помимо цикла "for ... in ..." существует также цикл while с подобным синтаксисом:
```
while условие:
    тело_цикла
```  
```
x = 0
while x <= 100:
    print(x)
    x = x + 0.5
```  

*** Циклы можно прерывать с помощью ключевого слова break. Чаще всего данный функционал используется в сочетании с условными конструкциями. Если отработало условие, то прервать цикл ***