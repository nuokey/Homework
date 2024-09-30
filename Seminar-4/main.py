import numpy as np
import matplotlib.pyplot as plt

def one():
    fig = plt.figure(figsize = (10,7))
    ax1 = fig.add_subplot(111)

    x_measured = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    y_measured = [0, 10, 21, 32, 39, 48, 60, 70, 81, 92, 96]

    x = [0, 10]
    y = np.interp(x, x_measured, y_measured)

    ax1.scatter(x_measured, y_measured, marker='.')

    ax1.errorbar(x_measured, y_measured, yerr=3.5, xerr = 0.1, color = 'black', linestyle = 'None')

    ax1.plot(x,y, 'black')

    ax1.grid()

    ax1.set_title("График")
    ax1.set_xlabel("Время, с")
    ax1.set_ylabel("Напряжение, град.")

    plt.show()

# one()

def two():
    fig = plt.figure(figsize = (10,7))
    ax1, ax2, ax3 = fig.subplots(1, 3)
    

    pos = 0
    scale = 10
    size = 500
    
    values = np.random.normal(pos, 10, size)
    
    ax1.hist(values, 100)
    

    pos = 0
    scale = 10
    size = 10000
    
    values = np.random.normal(pos, 10, size)
    
    ax2.hist(values, 100)

    pos = 0
    scale = 10
    size = 100000
    
    values = np.random.normal(pos, 10, size)
    
    ax3.hist(values, 100)

    plt.show()

# two()

def three():
    x = np.array([0.0, 1.0, 2.0, 3.0,  4.0,  5.0])
    y = np.array([0.0, 0.8, 0.9, 0.1, -0.8, -1.0])
    z = np.polyfit(x, y, 3) # аппроксимировать функцию y(x) полиномом третьей степени
    print(z)
    # чтобы не приходилось каждый раз строить полином с полученными коэффициентами, также существует функция poly1d
    p = np.poly1d(z)
    print(p)
    # теперь чтобы получить значение полинома с коэффициентами z в точке, например, 5, нам надо вызвать p(5) 
    print(p(5))

three()