import random
import numpy
N = 1000
class hw(object):
    def __init__(self):
        self.data = {}
    def sign(self, a):
        return 1 if a > 0 else -1
    def gen_data(self):
        self.data['x'] = [[1, random.uniform(-1, 1), random.uniform(-1, 1)] for i in range(N)]
        # gen y with sign(x1^2 + x2^2 - 0.6)
        self.data['y'] = [self.sign(pow(self.data['x'][i][1], 2) + pow(self.data['x'][i][2], 2) - 0.6) for i in range(N)]
        # simulate flipping
        self.data['y'] = [self.data['y'][i] if random.randint(1, 10) > 1 else (-1)*self.data['y'][i] for i in range(N)]
if __name__ == '__main__':
    hw13_inst = hw()
    error_rate = 0
    for i in range(1000):
        hw13_inst.gen_data()
        matX = numpy.array([hw13_inst.data['x'][j] for j in range(len(hw13_inst.data['x']))])
        matXplus = numpy.linalg.pinv(matX)
        w = numpy.dot(matXplus, hw13_inst.data['y'])
        error = sum(1 for j in range(len(hw13_inst.data['x'])) if hw13_inst.sign(numpy.dot(w, hw13_inst.data['x'][j])) != hw13_inst.data['y'][j])
        error_rate = error_rate + error/float(len(hw13_inst.data['x']))
    print error_rate/float(1000)
