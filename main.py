import matplotlib.pyplot as plt
import numpy as np

def generate_data():
    """Generates x values and their squared values"""
    x = np.linspace(-10, 10, 100)
    y = x ** 2
    return x, y

def generate_data2():
    """Generates x values and their squared values"""
    x = np.linspace(-10, 10, 100)
    y = x ** 3
    return x, y

def generate_data3():
    """Generates x values and their squared values"""
    x = np.linspace(-10, 10, 100)
    y = np.sin(x)
    return x, y
def plot_data(x, y):
    """Plots y = x^2"""
    plt.figure(figsize=(8, 5))
    plt.plot(x, y, label="y = x²", color='purple')
    plt.title("Plot of y = x²")
    plt.xlabel("x")
    plt.ylabel("y")

    plt.grid(True)
    plt.legend()
    # Save the figure
    plt.savefig("plot.png")
    plt.show()

def plot_data2(x, y):
    """Plots y = x^3"""
    plt.figure(figsize=(8, 5))
    plt.plot(x, y, label="y = x³", color='purple')
    plt.title("Plot of y = x²")
    plt.xlabel("x")
    plt.ylabel("y")

    plt.grid(True)
    plt.legend()
    # Save the figure
    plt.savefig("plot.png")
    plt.show()

def plot_data3(x, y):
    """Plots y = Sin"""
    plt.figure(figsize=(8, 5))
    plt.plot(x, y, label="y = x³", color='purple')
    plt.title("Plot of y = x²")
    plt.xlabel("x")
    plt.ylabel("y")

    plt.grid(True)
    plt.legend()
    # Save the figure
    plt.savefig("plot.png")
    plt.show()

def main():
    print("Generating and plotting y = x²...")
    x, y = generate_data()
    x2, y3 = generate_data2()
    x3, y4 = generate_data2()
    plot_data(x, y)
    plot_data2(x2, y3)
    plot_data3(x3, y4)


if __name__ == "__main__":
    main()
