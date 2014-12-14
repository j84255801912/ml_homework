import math
import numpy
from math import exp
#from scipy.optimize import newton
#from sympy import *

class hw(object):
    def E(self, k):
        u, v = k
        return 1.5*pow(u, 2) + 4*pow(v, 2) - u*v - 2*u + 3
    def gradient(self, k):
        u, v = k
        return [exp(u) + v*exp(u*v) + 2*u - 2*v - 3, 2*exp(2*v) + u*exp(u*v) - 2*u + 4*v - 2]
    def hes(self, k):
        u, v = k
        return [[exp(u) + pow(v, 2)*exp(u*v) + 2, exp(u*v) + u*v*exp(u*v) - 2], [exp(u*v) + u*v*exp(u*v) - 2, 4*exp(2*v) + pow(u, 2)*exp(u*v) + 4]]
    def adding(self, a, b):
        return [a[0] + b[0], a[1] + b[1]]
if __name__ == '__main__':
    myhw = hw()
    # 0
    uv = [0, 0]
    grad = myhw.gradient(uv)
    hess = myhw.hes(uv)
    matBinv = numpy.linalg.inv(hess)
    delta_uv = -numpy.dot(matBinv, grad)
    # 1
    uv = myhw.adding(uv, delta_uv)

    grad = myhw.gradient(uv)
    hess = myhw.hes(uv)
    matBinv = numpy.linalg.inv(hess)
    delta_uv = -numpy.dot(matBinv, grad)
    # 2
    uv = myhw.adding(uv, delta_uv)

    grad = myhw.gradient(uv)
    hess = myhw.hes(uv)
    matBinv = numpy.linalg.inv(hess)
    delta_uv = -numpy.dot(matBinv, grad)
    # 3
    uv = myhw.adding(uv, delta_uv)

    grad = myhw.gradient(uv)
    hess = myhw.hes(uv)
    matBinv = numpy.linalg.inv(hess)
    delta_uv = -numpy.dot(matBinv, grad)
    #4
    uv = myhw.adding(uv, delta_uv)

    grad = myhw.gradient(uv)
    hess = myhw.hes(uv)
    matBinv = numpy.linalg.inv(hess)
    delta_uv = -numpy.dot(matBinv, grad)
    #5
    uv = myhw.adding(uv, delta_uv)

    print myhw.E(uv)
