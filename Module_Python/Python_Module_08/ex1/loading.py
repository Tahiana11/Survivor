#!/usr/bin/env python3
import importlib.metadata
import sys


def compare_dependency_managers() -> None:
    print("\nDependency Management Comparison")
    print("=" * 40)

    print("\n[pip]")
    print("- Uses requirements.txt")
    print("- Install: pip install -r requirements.txt")
    print("- Export: pip freeze > requirements.txt")
    print("- Manual virtual environment management")

    print("\n[Poetry]")
    print("- Uses pyproject.toml and poetry.lock")
    print("- Install: poetry install")
    print("- Add package: poetry add <package>")
    print("- Automatic dependency resolution")
    print("- Automatic virtual environment management")


def display_version() -> None:
    modules: dict[str, str] = {
        "pandas": "Data manipulation ready",
        "numpy": "Numerical computation ready",
        "requests": "Network access ready",
        "matplotlib": "Visualization ready"
    }
    missings: list[str] = []
    for module, description in modules.items():
        try:
            version = importlib.metadata.version(module)
            print(f"[OK] {module} ({version}) - {description}")
        except importlib.metadata.PackageNotFoundError:
            missings.append(module)

    if missings:
        print("\n❌ ERROR: Missing dependencies detected!")
        print(f"Missing modules: {', '.join(missings)}")

        print("\nDependency Management Comparison")
        print("=" * 40)

        print("\n[pip]")
        print("- Dependency file : requirements.txt")
        print("- Install packages:")
        print(f"  pip install {' '.join(missings)}")
        print("- Export dependencies:")
        print("  pip freeze > requirements.txt")
        print("- Virtual environment:")
        print("  python -m venv matrix_env")

        print("\n[Poetry]")
        print("- Dependency file : pyproject.toml + poetry.lock")
        print("- Install packages:")
        print(f"  poetry add {' '.join(missings)}")
        print("- Install all project dependencies:")
        print("  poetry install")
        print("- Virtual environment managed automatically")

        print("\nProgram cannot continue until all dependencies"
              " are installed.")
        sys.exit(1)


def analysis_data() -> None:
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt

    print("\nAnalyzing Matrix data...")
    packages = np.array(["numpy", "matplotlib", "pandas"])
    project = np.array([
        "Project_1", "Project_2", "Project_3", "Project_4", "Project_5"]
        )
    matrix = np.random.randint(0, 2, size=(5, 3))
    df = pd.DataFrame(matrix, index=project, columns=packages)
    usage = df.sum()

    print(f"Processing {df.shape[0]} data points...")
    print("Generating visualization...")
    colors = ["black", "red", "blue"]
    plt.bar(usage.index, usage.values, color=colors)
    plt.title("Package Popularity", color="green")
    plt.xlabel("Packages")
    plt.ylabel("Number of projects")

    plt.savefig("matrix_analysis.png")
    plt.close()
    print("\nAnalysis complete!")
    print("Results saved to: matrix_analysis.png")


def main() -> None:
    print("LOADING STATUS: loading programs...")

    print("\nChecking depedencies:")
    display_version()
    analysis_data()
    compare_dependency_managers()


if __name__ == "__main__":
    main()
