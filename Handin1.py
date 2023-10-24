import matplotlib.pyplot as plt
import numpy as np

# Task 2

def pressure(z: float) -> float:
    """Returns the pressure in the atmosphere at height z.

    Args:
        z (float): Height in the atmosphere.

    Returns:
        float: Pressure at height z.
    """
    return 101.3 * 10 ** 3 * np.exp(-z/(1737))

def task2():
    z_list = np.linspace(0, 20_000, 1000)
    p_list = pressure(z_list)

    print(0.0289644 / (8.3144 * 273.15) * 9.82)
    
    plt.plot(z_list, p_list)
    plt.show()


if __name__ == "__main__":
    task2()
    
