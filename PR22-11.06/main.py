from analysis.numpy_tasks import run_numpy_tasks
from analysis.pandas_tasks import run_pandas_tasks
from analysis.visualization import create_graphs


def main():
    print("Проект запущен")

    run_numpy_tasks()
    run_pandas_tasks()
    create_graphs()


if __name__ == "__main__":
    main()