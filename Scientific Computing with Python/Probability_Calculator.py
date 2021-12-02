import random
import copy

class Hat:

    def __init__(self, **balls):

        self.contents = []
        for ball in balls:
            for x in range(balls[ball]):
                self.contents.append(ball)

    def draw(self, times):
        remove_list = []
        if times <= len(self.contents):
            for remove in range(times):
                choice = random.randrange(len(self.contents))
                remove_list.append(self.contents[choice])
                self.contents.pop(choice)
            return remove_list

        else:
            return self.contents


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):

    sucess = 0
    for x in range(num_experiments):
        object = copy.deepcopy(hat)
        draw = object.draw(num_balls_drawn)

        for v, test in enumerate(expected_balls):
            if expected_balls[test] <= draw.count(test):
                if v == len(expected_balls)-1:
                    sucess += 1
            else:
                break
    return sucess/num_experiments


if __name__ == '__main__':
    hat = Hat(blue=3, red=2, green=6)
    probability = experiment(hat=hat, expected_balls={"blue": 2, "green": 1}, num_balls_drawn=4,
                                             num_experiments=1000)
    print(probability)
