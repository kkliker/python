"""
Не секрет, что "Главный вопрос жизни, вселенной и всего такого" – это 42.
Давай используем эти знания следующим образом – тебе необходимо напечатать "Hello, world" 42 раза.

Да, целых 42 раза!
"""

text = "Hello"
textmain = "worldHello"
print("Hello, " , end ="")
i = 0
while i < 41:
    i = i +1 

    print(textmain + ", "  ,end = "")
    if(i== 41):
        print("world", end="")