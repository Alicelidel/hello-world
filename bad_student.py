import random

def fill_absent(n):
    absent = [] #массив с отметками о посещении
    k = 0 #количество когда его не было
    seq = [True, False]
    for i in range(n):
        was = random.choice(seq)
        absent.append(was)
        if was == False: k+=1
    print('Студент прогуливал в течение %s дней' % str(k))
    #print(absent)
    return absent,k


def find_avg(absent,k):
    prev_day = absent[0]
    y = 0
    length = []
    for day in absent:
        if (day == False):
            if day == prev_day:
                y += 1
        if day == True:
            if day != prev_day:
                if y != 0: length.append(y)
                #print(y)
                y = 0
        prev_day = day
    #print(length)
    avg = k // len(length)
    maxi = max(length)
    return avg, maxi


def main():
    n = int(input('Сколько дней считаем? '))
    absent, k = fill_absent(n)
    avg, maxi = find_avg(absent, k)
    print('В среднем прогул длился %s и самый длинный прогул был %s' % (avg, maxi))

if __name__ == "__main__":
    main()