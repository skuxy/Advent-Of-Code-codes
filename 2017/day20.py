#! /usr/bin/pypy3

import re


GENERAL_REGEX = '[pva]=<(.+),(.+),(.+)>'


class particle:
    def __init__(self, name, position, velocity, acceleration):
        self.name = name
        self.position = position
        self.velocity = velocity
        self.acceleration = acceleration

    def __repr__(self):
        return "{}, {}, {}, {}, {}".format(
            self.name,
            self.distance_to_0(),
            self.position,
            self.velocity,
            self.acceleration)

    def distance_to_0(self):
        x, y, z = self.position
        return abs(x) + abs(y) + abs(z)

    def update(self):
        x_velocity, y_velocity, z_velocity = self.velocity
        x_acceleration, y_acceleration, z_acceleration = self.acceleration
        x_position, y_position, z_position = self.position

        x_velocity += x_acceleration
        y_velocity += y_acceleration
        z_velocity += z_acceleration

        x_position += x_velocity
        y_position += y_velocity
        z_position += z_velocity

        self.velocity = (
            x_velocity,
            y_velocity,
            z_velocity
        )

        self.position = (
            x_position,
            y_position,
            z_position
        )


def remove_duplicates(particles):
    position_occured = {}
    for particle_object in particles:
        if particle_object.position not in position_occured:
            position_occured[particle_object.position] = 1
        else:
            position_occured[particle_object.position] += 1

    occured_once = []
    for position in position_occured:
        if position_occured[position] == 1:
            occured_once.append(position)

    return list(filter(lambda x: x.position in occured_once, particles))


if __name__ == "__main__":
    with open('input20.txt') as stdin:
        particles = []
        particle_index = 0

        for line in stdin.readlines():
            position_data, velocity_data, acceleration_data = line.strip().split(', ')
            position = re.search(GENERAL_REGEX, position_data).group(1, 2, 3)
            velocity = re.search(GENERAL_REGEX, velocity_data).group(1, 2, 3)
            acceleration = re.search(GENERAL_REGEX, acceleration_data).group(1, 2, 3)

            position = [int(x) for x in position]
            velocity = [int(x) for x in velocity]
            acceleration = [int(x) for x in acceleration]

            particles.append(particle(particle_index, position, velocity, acceleration))
            particle_index += 1

    for _ in range(100):
        [particle_object.update() for particle_object in particles]
        particles = remove_duplicates(particles)
        print(len(particles))
    # part 1
    # particles = sorted(particles, key=lambda x: x.distance_to_0())
    # print(particles[0])
    # part 2
    print(len(particles))
