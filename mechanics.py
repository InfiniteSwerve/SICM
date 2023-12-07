from typing import Callable
import numpy as np


class Local:
    def __init__(self):
        pass

    @property
    def coordinates(self):
        return

    @property
    def velocity(self):
        return


def L_free_particle(mass: float) -> Callable[[Local], float]:
    def v(local: Local):
        v = local.velocity
        return mass / 2 * np.dot(v, v)

    return v
