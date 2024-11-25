#программа бросок монеты:
#бросков 100, возможно взять while или бесконечный цикл с BREAK на 100
#броски должны быть с результатом ОРЕЛ или РЕШКА
#считать каждое выпадение в 2 переменные

import random

throw_count = 0
heads_count = 0
tails_count = 0

while throw_count != 100:
    throw_count += 1
    print("\nБросок номер:" + str(throw_count))  
    throw_result = random.randint(1,2)
    if throw_result == 1:
        heads_count += 1
        print("ОРЕЛ ВЫПАЛ!")
    else:  
        tails_count += 1
        print("РЕШКААА")
      

throw_count = str(throw_count)
heads_count = str(heads_count)
tails_count = str(tails_count)

print ("\n\nвсего бросков сделано: " + throw_count)
print ("ОРЛОВ выпало: " + heads_count)
print ("РЕШЕК выпало: " + tails_count+"\n\n")

input ("Нажмите Enter, чтобы выйти")
