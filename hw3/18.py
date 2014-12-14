import math

eta = 0.001
T = 2000
class hw(object):
    def __init__(self):
        self.data = []
        self.test = []
    def get_data(self):
        for line in open("hw3_train.dat"):
            line = line.replace('\n', '')
            if line == "":
                break
            exploded = line.replace('\t', ' ').split(' ')
            self.data.append({
                               'x': [float(exploded[i]) if i != 0 else 1 for i in range(len(exploded) - 1)],
                               'y': float(exploded[len(exploded) - 1])
                             })
    def get_test(self):
        for line in open("hw3_test.dat"):
            line = line.replace('\n', '')
            if line == "":
                break;
            exploded = line.replace('\t', ' ').split(' ')
            self.test.append({
                               'x': [float(exploded[i]) if i != 0 else 1 for i in range(len(exploded) - 1)],
                               'y': int(exploded[len(exploded) - 1])
                             })
    def sign(self, a):
        return 1 if a > 0 else -1
    def sigmoid(self, x):
        return 1 / (1 + math.exp((-1)*x))
    def dot(self, a, b):
        if len(a) != len(b):
            raise Exception("dot error")
        return sum([a[i]*b[i] for i in range(len(a))])
    def compute_gradient(self, w, N):
        dim = len(myhw.data[0]['x'])
        w_all = [0]*dim
        for i in range(N):
            eta_result = self.sigmoid((-1)*self.data[i]['y']*self.dot(w, self.data[i]['x']))
            for j in range(len(self.data[0]['x'])):
                w_all[j] += eta_result*(-1)*self.data[i]['y']*self.data[i]['x'][j]
        w_all = [w_all[i] / float(N) for i in range(dim)]
        return w_all
if __name__ == "__main__":
    myhw = hw()
    myhw.get_data()
#    print myhw.data
    myhw.get_test()
    dim = len(myhw.data[0]['x'])
    N = len(myhw.data)
    w = [0]*dim
    for t in range(T):
        the_gradient = myhw.compute_gradient(w, N)
        w = [w[i] - eta*the_gradient[i] for i in range(dim)]
    # test
    testN = len(myhw.test)
    error = sum([1 if myhw.sign(myhw.dot(w, myhw.test[i]['x'])) != myhw.test[i]['y'] else 0 for i in range(testN)])
    print error/float(testN)
