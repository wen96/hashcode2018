class Ride:
    def __init__(self, line):
        numbers = line.split(' ')
        self.init_pos = int(numbers[0]), int(numbers[1])
        self.last_pos = int(numbers[2]), int(numbers[3])
        self.start = int(numbers[4])
        self.finish = int(numbers[5])


class Car:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.step = 0

    def goto(self, x, y):
        self.step += self.distance_to(x, y)
        self.x = x
        self.y = y

    def distance_to(self, x, y):
        return abs(self.x - x) + abs(self.y - y)

    def distance_ride(self, ride):
        dist1 = self.distance_to(ride.init_pos[0], ride.init_pos[1])
        x, y = ride.init_pos[0], ride.init_pos[1]
        dist2 = abs(x - ride.last_pos[0]) + abs(y - ride.last_pos[1])
        return dist1 + dist2


class Simulator:
    def __init__(self, vehicles_num, rides_num, bonus, steps, rides):
        self.vehicles_num = int(vehicles_num)
        self.rides_num = int(rides_num)
        self.bonus = int(bonus)
        self.steps = int(steps)
        self.rides = rides

    def solve(self):
        car_rides = []
        gotten_rides = {}
        cars = []
        for vehicle_i in xrange(self.vehicles_num):
            car_rides.append([])
            car = Car()
            cars.append(car)
            for i, ride in enumerate(self.rides):
                if not gotten_rides.get(i):
                    distance = car.distance_ride(ride)
                    if car.step + distance <= ride.start:
                        car.goto(ride.init_pos[0], ride.init_pos[1])
                        car.goto(ride.last_pos[0], ride.last_pos[1])
                        car_rides[vehicle_i].append(i)
                        gotten_rides[i] = True
        print 'Half way'
        for vehicle_i, car in enumerate(cars):
            for j, ride in enumerate(self.rides):
                if not gotten_rides.get(j):
                    distance = car.distance_ride(ride)
                    if car.step + distance <= ride.finish:
                        car.goto(ride.init_pos[0], ride.init_pos[1])
                        car.goto(ride.last_pos[0], ride.last_pos[1])
                        car_rides[vehicle_i].append(j)
                        gotten_rides[j] = True

        print len(self.rides) - len(gotten_rides)
        return car_rides


class Solution:
    def __init__(self, cars):
        self.cars = cars

    def write_files(self, filename):
        with open('{}_solution.out'.format(filename), 'w+') as file:
            for car_ride in self.cars:
                if car_ride:
                    line = '{} {}\n'.format(len(car_ride), ' '.join([str(ride) for ride in car_ride]))
                    file.write(line)
                else:
                    file.write('0\n')


def read_file(filename):
    with open(filename) as file:
        lines = [x for x in file]
        num_rows, num_colum, vehicles_num, rides_num, bonus, steps = lines[0].split(' ')
        rides = [Ride(line) for line in lines[1:]]
        simulation = Simulator(
            vehicles_num=vehicles_num, rides_num=rides_num, bonus=bonus, steps=steps, rides=rides
        )
        sol = Solution(simulation.solve())
        sol.write_files(filename)


if __name__ == '__main__':
    print 'a'
    read_file('a_example.in')
    print 'b'
    read_file('b_should_be_easy.in')
    print 'c'
    read_file('c_no_hurry.in')
    print 'd'
    read_file('d_metropolis.in')
    print 'e'
    read_file('e_high_bonus.in')
