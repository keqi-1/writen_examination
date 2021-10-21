# output = []
# for x in input:
#     a = e ^ (x)
#     b = e ^ (-x)
#     output.append((a - b) / (a + b))

import numpy as np
import math
import sys


def Sigmoid(input):
    output = (1 / (1 + (np.exp(-input))))
    return output


def Tanh(input):
    output = (np.exp(input) - np.exp(-input)) / (np.exp(input) + np.exp(-input))
    return output


def ReLU(input):
    output = []
    for x in input:
        output.append(max(0, x))
    return output


def LeakyReLU(input, alpha=0.1):
    output = []
    for x in input:
        output.append(max(0, x) + alpha * min(0, x))
    return output


def Softmax(input):
    s = np.exp(input)
    output = s/s.sum()
    return output


def d_Sigmoid(input):
    output = (1 / (1 + np.exp(-input))) * (1 - 1 / (1 + np.exp(-input)))
    return output


def d_Tanh(input):
    output = []
    t = (np.exp(input) - np.exp(-input)) / (np.exp(input) + np.exp(-input))
    for i in t:
        output.append(1-i*i)
    return output


def d_ReLU(input):

    output = []
    for x in input:
        if x > 0:
            output.append(1)
        if x <= 0:
            output.append(0)
    return output


def d_LeakyReLU(input, alpha=0.1):
    output = []
    for x in input:
        if x > 0:
            output.append(1)
        if x <= 0:
            output.append(alpha)
    return output


if __name__ == "__main__":
    line = sys.stdin.readline().strip()
    lines = line.split()
    lines_list = []
    for i in range(len(lines)):
        lines_list.append(float(lines[i]))
    input = np.array(lines_list)
    print(Sigmoid(input))
    print(Tanh(input))
    print(ReLU(input))
    print(LeakyReLU(input, alpha=0.1))
    print(Softmax(input))
    print(d_Sigmoid(input))
    print(d_Tanh(input))
    print(d_ReLU(input))
    print(d_LeakyReLU(input, alpha=0.1))