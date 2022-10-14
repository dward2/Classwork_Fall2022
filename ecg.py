import matplotlib.pyplot as plt


def add_plot(x):
    a = x + 5
    time = [0, 1, 2, 3]
    y = [0, 1, 4, 9]
    plt.plot(time, y)
    plt.show()
    return a


if __name__ == "__main__":
    print(add_plot(4))
