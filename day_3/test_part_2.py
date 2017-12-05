from collections import namedtuple
from typing import Iterable
from itertools import permutations


Point = namedtuple('Point', ['x', 'y'])


Right = Point(x=1, y=0)
Left = Point(x=-1, y=0)
Up = Point(x=0, y=1)
Down = Point(x=0, y=-1)


def get_points_on_edge(start: Point, end: Point, direction: Point) -> Iterable:
    current_point = start
    while not (current_point == end):
        current_point = Point(current_point.x + direction.x, current_point.y + direction.y)
        yield current_point


def get_next_corner(start: Point)-> Point:
    if start.x > 0 and start.y <= 0:
        end = Point(start.x, start.x)
    if start.x > 0 and start.y > 0:
        end = Point(-start.x, start.y)
    if start.x < 0 and start.y > 0:
        end = Point(start.x, -start.y)
    if start.x < 0 and start.y < 0:
        end = Point(-start.x, start.y)
    return end


def generate_points() -> Iterable:
    current_point = Point(0, 0)
    yield current_point
    while True:
        # New layer.
        start_point = Point(current_point.x + 1, current_point.y)
        yield start_point

        top_right_corner = get_next_corner(start_point)
        for right_edge_point in get_points_on_edge(start_point, top_right_corner, Up):
            yield right_edge_point

        top_left_corner = get_next_corner(top_right_corner)
        for top_edge_point in get_points_on_edge(top_right_corner, top_left_corner, Left):
            yield top_edge_point

        bottom_left_corner = get_next_corner(top_left_corner)
        for left_edge_point in get_points_on_edge(top_left_corner, bottom_left_corner, Down):
            yield left_edge_point

        bottom_right_corner = get_next_corner(bottom_left_corner)
        for bottom_edge_point in get_points_on_edge(bottom_left_corner, bottom_right_corner, Right):
            yield bottom_edge_point

        # Set current point to start the next layer.
        current_point = bottom_right_corner


RELATIVE_SURROUNDING_COORDINATES = set(permutations([-1, -1, 0, 0, 1, 1, ], 2))


def get_surrounding_points(point: Point) -> list:
    # Also results itself, but that's ok.
    absolute_surrounding_coordinates = [(point.x + x, point.y + y) for (x, y) in RELATIVE_SURROUNDING_COORDINATES]
    return absolute_surrounding_coordinates


def solve():
    point_dict = {}
    for point in generate_points():
        surrounding_fill_values = [point_dict.get(point_x_y).get('fill_value') for point_x_y in get_surrounding_points(point) if point_dict.get(point_x_y)]
        fill_value = sum(surrounding_fill_values) or 1  # '1' is for the centre.
        if fill_value > 361527:
            return fill_value
        point_dict[(point.x, point.y)] = {'point': point, 'fill_value': fill_value}


if __name__ == "__main__":
    print(solve())


def test_get_points_on_edge_up():
    start = Point(0, 0)
    end = Point(0, 5)
    direction = Up

    result = list(get_points_on_edge(start, end, direction))
    assert result == [Point(0, 1), Point(0, 2), Point(0, 3), Point(0, 4), Point(0, 5)]


def test_get_points_on_edge_down():
    start = Point(-3, 3)
    end = Point(-3, 1)
    direction = Down

    result = list(get_points_on_edge(start, end, direction))
    assert result == [Point(-3, 2), Point(-3, 1)]


def test_get_end_point():
    assert get_next_corner(Point(3, -1)) == Point(3, 3)
    assert get_next_corner(Point(4, 4)) == Point(-4, 4)
    assert get_next_corner(Point(-5, 5)) == Point(-5, -5)
    assert get_next_corner(Point(-3, -3)) == Point(3, -3)


# def test_get_surrounding_points():
#     get_surrounding_points(Point(1, 1))
