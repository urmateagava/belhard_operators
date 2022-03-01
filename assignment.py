# задумывался как простецкий калькулятор индекса массы тела, в итоге понеслось.
# можно было бы вместо списков прилепить imput, но хотелось именно добавить списки


# создаем списки для дальнейшего расчета индекса массы тела где:
# name - имя
# weight - вес
# height - рост
# counter - все так же счетчик
name = ["king_lich", "lab_ratt", "toxic_witch"]
weight = [57, 85, 65]
height = [1.83, 1.89, 1.61]
counter = 0

# iwb - формула расчета индекса массы тела
while counter <= len(weight[:]):
    iwb = weight[counter] / (height[counter] * 2)
    if iwb <= 16:
        print('У {name} - выраженный дефицит массы тела({iwb})'.format(name=name[counter], iwb=iwb))
    if iwb >= 16 and iwb >= 18:
        if iwb > 18:
            pass
        print('У {name} - Недостаточная масса тела (дефицит)({iwb})'.format(name=name[counter], iwb=iwb))
    if iwb >= 18 and iwb >= 24:
        if iwb > 24:
            pass
        print('У {name} - Нормальная масса тела (дефицит)({iwb})'.format(name=name[counter], iwb=iwb))
    if iwb >= 25 and iwb >= 30:
        if iwb > 30:
            pass
        print('У {name} - Избыточная масса тела (предожирение)({iwb})'.format(name=name[counter], iwb=iwb))
    if iwb >= 30 and iwb >= 35:
        if iwb > 35:
            pass
        print('У {name} - Ожирение I степени({iwb})'.format(name=name[counter], iwb=iwb))
    if iwb >= 35 and iwb >= 40:
        if iwb > 40:
            pass
        print('У {name} - Ожирение II степени({iwb})'.format(name=name[counter], iwb=iwb))
    if iwb >= 40:
        print('У {name} - Ожирение III степени({iwb})'.format(name=name[counter], iwb=iwb))
    counter += 1

    # что бы счетчик не вышел за рамки списка
    if counter >= len(weight[:]):
        break
