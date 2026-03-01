import numpy as np
import matplotlib.pyplot as plt
import random

def poisson(lambda_):
    X = 0
    S = 1
    q = np.exp(-lambda_)
    while S > q:
        U = random.random()
        S *= U
        X += 1
    return X

def gaussian(mu, sigma):
    U1 = random.random()
    U2 = random.random()
    Z0 = np.sqrt(-2 * np.log(U1)) * np.cos(2 * np.pi * U2)
    Z1 = np.sqrt(-2 * np.log(U1)) * np.sin(2 * np.pi * U2)
    return mu + sigma * Z0, mu + sigma * Z1

def generate_poisson(lambda_, n):
    data = [poisson(lambda_) for _ in range(n)]
    plt.hist(data, bins=range(min(data), max(data) + 1), alpha=0.75, color='blue', edgecolor='black')
    plt.title(f'Histogram rozkładu Poissona λ={lambda_}')
    plt.xlabel('Wartości')
    plt.ylabel('Częstość')
    plt.grid(True)
    plt.show()


def generate_gaussian(mu, sigma, n):
    data = [gaussian(mu, sigma)[0] for _ in range(n)]
    plt.hist(data, bins=30, alpha=0.75, color='green', edgecolor='black')
    plt.title(f'Histogram rozkładu Normalnego μ={mu}, σ={sigma}')
    plt.xlabel('Wartości')
    plt.ylabel('Częstość')
    plt.grid(True)
    plt.show()


def main():
    seed = input("Czy chcesz ustawić seed? (tak/nie): ").lower()
    if seed == "tak":
        seed_value = int(input("Podaj wartość seedu: "))
        random.seed(seed_value)
        np.random.seed(seed_value)


    n = int(input("Podaj liczbę próbek: "))


    lambda_ = float(input("Podaj wartość λ dla rozkładu Poissona: "))
    generate_poisson(lambda_, n)

    mu = float(input("Podaj wartość średnią μ dla rozkładu Normalnego: "))
    sigma = float(input("Podaj wartość odchylenia standardowego σ dla rozkładu Normalnego: "))
    generate_gaussian(mu, sigma, n)


if __name__ == "__main__":
    main()