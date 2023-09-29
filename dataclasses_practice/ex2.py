from dataclasses import dataclass, field, InitVar


class Vector3D:
    def __init__(self, x, y, z, calc_len: bool = True):
        self.x = x
        self.y = y
        self.z = z
        self.length = (x * x + y * y + z * z) ** 0.5 if calc_len else 0


@dataclass(order=True)
class V3D:
    x: int
    y: int
    z: int
    calc_len: InitVar[bool] = True
    length: float = field(repr=False, compare=False, default=0)

    def __post_init__(self, calc_len):
        if calc_len:
            self.length = (self.x * self.x + self.y * self.y + self.z * self.z) ** 0.5


if __name__ == '__main__':
    v1 = V3D(1, 2, 2, False)
    v2 = V3D(1, 2, 4)
    print(v1 < v2)