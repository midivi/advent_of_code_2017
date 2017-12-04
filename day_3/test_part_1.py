"""
layer 0: 1
layer 1: 3 * 4 - 4 -> 2 * 4 = 8.
layer 2: 5 * 4 - 4 -> 4 * 4 = 16.
layer 3: 7 * 4 - 4 -> 6 * 4 = 24.
layer 4: 9 * 4 = 4 -> 8 * 4 = 32.


"""
import pytest


class Layer:
    def __init__(self, layer_number: int, inner_layer) -> None:
        self.edge_length = 1 + layer_number * 2
        self.layer_number = layer_number

        self.minimum = inner_layer.maximum + 1 if inner_layer else 1
        self.maximum = self.minimum + (layer_number * 2) * 4 - 1 if inner_layer else 1

        self.bottom_right = self.maximum if inner_layer else 1
        self.bottom_left = self.bottom_right - self.edge_length + 1 if inner_layer else 1
        self.top_left = self.bottom_left - self.edge_length + 1 if inner_layer else 1
        self.top_right = self.top_left - self.edge_length + 1 if inner_layer else 1

    def in_my_layer(self, number: int) -> bool:
        return self.minimum <= number <= self.maximum

    def resolve_to_centre_of_edge(self, number: int) -> int:
        if self.bottom_right >= number >= self.bottom_left:
            return self.distance_to_centre_of_edge(number, self.bottom_right, self.bottom_left)
        elif self.bottom_left >= number >= self.top_left:
            return self.distance_to_centre_of_edge(number, self.bottom_left, self.top_left)
        elif self.top_left >= number >= self.top_right:
            return self.distance_to_centre_of_edge(number, self.top_left, self.top_right)
        else:
            return self.distance_to_centre_of_edge(number, self.top_right - 1, self.top_right - self.edge_length + 2)

    @staticmethod
    def distance_to_centre_of_edge(number: int, corner1: int, corner2: int) -> int:
        middle = int((corner1 + corner2) / 2)
        return abs(number - middle)

    def resolve_to_centre_of_square(self, number: int) -> int:
        return self.resolve_to_centre_of_edge(number) + self.layer_number


def solve(number):
    inner_layer = Layer(0, None)
    layer_number = 1
    while True:
        current_layer = Layer(layer_number, inner_layer)
        if current_layer.in_my_layer(number):
            return(current_layer.resolve_to_centre_of_square(number))
        inner_layer = current_layer
        layer_number = layer_number + 1


@pytest.mark.parametrize('number, expected', [
    (10, 3),
    (11, 2),
    (12, 3),
    (13, 4),
    (1024, 31)
])
def test_solve(number, expected):
    assert solve(number) == expected


if __name__ == '__main__':
    number = 361527
    print(solve(number))


@pytest.mark.parametrize('number, corner1, corner2, expected', [
    (15, 13, 17, 0),
    (16, 13, 17, 1),
    (17, 13, 17, 2),
    (14, 13, 17, 1),
    (13, 13, 17, 2),
])
def test_resolve_to_centre_of_edge(number, corner1, corner2, expected):
    assert Layer.distance_to_centre_of_edge(number, corner1, corner2) == expected


def test_layer0():
    test = Layer(0, None)

    assert test.minimum == 1
    assert test.maximum == 1
    assert test.bottom_right == 1
    assert test.bottom_left == 1
    assert test.top_left == 1
    assert test.top_right == 1


def test_layer1():
    layer0 = Layer(0, None)
    test = Layer(1, layer0)

    assert test.minimum == 2
    assert test.maximum == 9
    assert test.bottom_right == 9
    assert test.bottom_left == 7
    assert test.top_left == 5
    assert test.top_right == 3


@pytest.mark.parametrize('number, expected', [
    (2, 0),
    (3, 1),
    (4, 0),
    (5, 1),
    (6, 0),
    (7, 1),
    (8, 0),
    (9, 1)
])
def test_layer1_resolve_to_middle_of_edge(number, expected):
    layer0 = Layer(0, None)
    test = Layer(1, layer0)
    assert test.resolve_to_centre_of_edge(number) == expected


def test_layer2():
    layer0 = Layer(0, None)
    layer1 = Layer(1, layer0)
    layer2 = Layer(2, layer1)

    assert layer2.minimum == 10
    assert layer2.maximum == 25
    assert layer2.bottom_right == 25
    assert layer2.bottom_left == 21
    assert layer2.top_left == 17
    assert layer2.top_right == 13


@pytest.mark.parametrize('number, expected', [
    (10, 1),
    (11, 0),
    (12, 1),
    (13, 2),
    (14, 1),
    (15, 0),
    (16, 1),
    (17, 2),
    (18, 1),
    (19, 0),
])
def test_layer2_resolve_to_centre_of_edge(number, expected):
    layer0 = Layer(0, None)
    layer1 = Layer(1, layer0)
    layer2 = Layer(2, layer1)

    assert layer2.resolve_to_centre_of_edge(number) == expected


@pytest.mark.parametrize('number, expected', [
    (10, 3),
    (11, 2),
    (12, 3),
    (13, 4),
    (14, 3),
    (15, 2),
    (16, 3),
    (17, 4),
    (18, 3),
    (19, 2),
])
def test_distance_to_centre_of_square(number, expected):
    layer0 = Layer(0, None)
    layer1 = Layer(1, layer0)
    layer2 = Layer(2, layer1)

    assert layer2.resolve_to_middle_of_square(number) == expected

