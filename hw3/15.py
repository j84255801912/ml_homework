import random
import numpy
N = 1000
class hw(object):
    def __init__(self):
        self.data = {}
        self.test = {}
    def sign(self, a):
        return 1 if a > 0 else -1
    def gen_data(self):
#        self.data['x'] = [[1, random.uniform(-1, 1), random.uniform(-1, 1)] for i in range(N)]
        self.data['x'] = []
        for i in range(N):
            a = random.uniform(-1, 1)
            b = random.uniform(-1, 1)
            self.data['x'].append([1, a, b, a*b, pow(a, 2), pow(b, 2)])
        # gen y with sign(x1^2 + x2^2 - 0.6)
        self.data['y'] = [self.sign(pow(self.data['x'][i][1], 2) + pow(self.data['x'][i][2], 2) - 0.6) for i in range(N)]
        # simulate flipping
        self.data['y'] = [self.data['y'][i] if random.randint(1, 10) > 1 else (-1)*self.data['y'][i] for i in range(N)]
    def gen_test(self):
        self.test['x'] = []
        for i in range(N):
            a = random.uniform(-1, 1)
            b = random.uniform(-1, 1)
            self.test['x'].append([1, a, b, a*b, pow(a, 2), pow(b, 2)])
        # gen y with sign(x1^2 + x2^2 - 0.6)
        self.test['y'] = [self.sign(pow(self.test['x'][i][1], 2) + pow(self.test['x'][i][2], 2) - 0.6) for i in range(N)]
        # simulate flipping
        self.test['y'] = [self.test['y'][i] if random.randint(1, 10) > 1 else (-1)*self.test['y'][i] for i in range(N)]
if __name__ == '__main__':
    hw15_inst = hw()
    error_rate = 0
    w_all = [0, 0, 0, 0, 0, 0]
    for i in range(1000):
        hw15_inst.gen_data()
        hw15_inst.gen_test()
        matX = numpy.array([hw15_inst.data['x'][j] for j in range(len(hw15_inst.data['x']))])
        matXplus = numpy.linalg.pinv(matX)
        # get w
        w = numpy.dot(matXplus, hw15_inst.data['y'])
        # testing by test data
        error = sum(1 for j in range(len(hw15_inst.test['x'])) if hw15_inst.sign(numpy.dot(w, hw15_inst.test['x'][j])) != hw15_inst.test['y'][j])
        error_rate = error_rate + error/float(len(hw15_inst.test['x']))
    print error_rate/float(1000)
