# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

moves = 0
tab = [(-1,-1),(-1,0),(-1,1),(0,1),(0,-1),(1,1),(1,0),(1,-1)]
def count(me_x,me_y,destination_x,destination_y):
    d = ((me_x-destination_x)**2 + (me_y-destination_y)**2)**(1/2)
    return d


def check(before_d,new_d):
    if before_d<=new_d:
        return False
    else:
        return True




if __name__ == "__main__":
    my_x = 0
    my_y = 0
    destination_x = 0
    destination_y = 0
    while type(my_x)!=int or type(my_y)!=int or type(destination_y)!= int or type(destination_x)!=int:
        try:
            my_x = int(input("Podaj punkt od ktorego zaczynasz x:"))
            my_y = int(input("Podaj punkt od ktorego zaczynasz y:"))
        except TypeError:
            print("Niewlasciwy typ danych")
        except ValueError:
            print("Niewlasciwy typ danych")
    destination_x = int(input("podaj punkt do ktorego chcesz dojsc x:"))
    destination_y = int(input("podaj punkt do ktorego chcesz dojsc y:"))
    before_d = count(my_x,my_y,destination_x,destination_y)

    while my_x!= destination_x or my_y!= destination_y:
        distances = []
        for i in range(8):
            x = my_x + tab[i][0]
            y = my_y + tab[i][1]
            d = count(x,y,destination_x,destination_y)
            distances.append(d)
        index = distances.index(min(distances))
        my_x = my_x + tab[index][0]
        my_y = my_y + tab[index][1]
        print(my_x,my_y,destination_x,destination_y)
        moves+=1
    print("Zajelo ci to:",moves," krokow")








            # See PyCharm help at https://www.jetbrains.com/help/pycharm/
