# main.py

from benchmark import run_benchmarks
from plots import plot_all


def main():

    print("Запуск benchmark...")

    run_benchmarks()

    print("Построение графиков...")

    plot_all()

    print("Готово!")


if __name__ == "__main__":
    main()
