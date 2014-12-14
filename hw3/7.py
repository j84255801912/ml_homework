import math
eta = 0.01

class hw(object):
    def E(self, k):
        u, v = k
        exp = math.exp
        return exp(u) + exp(2*v) + exp(u*v) + pow(u, 2) - 2*u*v + 2*pow(v, 2) - 3*u - 2*v
    def gradient(self, k):
        u, v = k
        exp = math.exp
        return [exp(u) + v*exp(u*v) + 2*u - 2*v - 3, 2*exp(2*v) + u*exp(u*v) - 2*u + 4*v -2]
    def u_and_v(self, t):
        if t is 0:
            return [0, 0]
        else:
            k = self.u_and_v(t - 1)
            grad = self.gradient(k)
            return [k[0] - eta*grad[0], k[1] - eta*grad[1]]
if __name__ == '__main__':
    myhw = hw()
    print myhw.E(myhw.u_and_v(5))
