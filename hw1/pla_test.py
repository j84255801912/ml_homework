import random
class pla:
    def __init__(self):
        self.data = []
        self.test = []
    def read_file_15(self):
        fp = open("hw1_15_train.dat")
        while 1:
            line = fp.readline()
            line = line.replace('\n', '')
            if line == "":
                break;
            exploded = line.replace('\t', ' ').split(' ')
            self.data.append({
                                'x' : [1, float(exploded[0]), float(exploded[1]), float(exploded[2]), float(exploded[3])],
                                'y' : int(exploded[4])
                             })
    def read_file_18(self):
        fp = open("hw1_18_train.dat")
        while 1:
            line = fp.readline()
            line = line.replace('\n', '')
            if line == "":
                break;
            exploded = line.replace('\t', ' ').split(' ')
            self.data.append({ 
                                'x' : [1, float(exploded[0]), float(exploded[1]), float(exploded[2]), float(exploded[3])],
                                'y' : int(exploded[4])
                             })
        # read test
        fp = open("hw1_18_test.dat")
        while 1:
            line = fp.readline()
            line = line.replace('\n', '')
            if line == "":
                break;
            exploded = line.replace('\t', ' ').split(' ')
            self.test.append({ 
                                'x' : [1, float(exploded[0]), float(exploded[1]), float(exploded[2]), float(exploded[3])],
                                'y' : int(exploded[4])
                             })
    def pla_15(self):
        self.read_file_15()
        N = len(self.data)

        i = 0
        update_times = 0
        k = 0
        w = [0, 0, 0, 0, 0]

        while 1:
            # inner product
            inner_product = sum(p*q for p, q in zip(self.data[i]['x'], w))
            sign = 1 if inner_product > 0 else -1

            # if the sign != yn
            if sign != self.data[i]['y']:
                for j in range(5):
                    w[j] = w[j]+self.data[i]['y']*self.data[i]['x'][j]
                update_times = update_times+1
                k = 0
            else:
                k = k+1
            if k == N:
                break
            i = (i+1)%N
        print update_times

    def pla_16(self):
        self.read_file_15()
        N = len(self.data)
        all_times = 0
        for d in range(2000):
            random.shuffle(self.data)
            i = 0
            k = 0
            w = [random.random(), random.random(), random.random(), random.random(), random.random()]
            update_times = 0
            while 1:
                # inner product
                inner_product = sum(p*q for p, q in zip(self.data[i]['x'], w))
                sign = 1 if inner_product > 0 else -1

                # if the sign != yn
                if sign != self.data[i]['y']:
                    for j in range(5):
                        w[j] = w[j]+self.data[i]['y']*self.data[i]['x'][j]
                    update_times = update_times+1
                    k = 0
                else:
                    k = k+1
                if k == N:
                    break
                i = (i+1)%N
            all_times = all_times + update_times
        print all_times/float(2000)
    def pla_17(self):
        self.read_file_15()
        N = len(self.data)
        all_times = 0
        miu = 0.5
        for d in range(2000):
            random.shuffle(self.data)
            k = 0
            i = 0
            w = [random.random(), random.random(), random.random(), random.random(), random.random()]
            update_times = 0
            while 1:
                # inner product
                inner_product = sum(p*q for p, q in zip(self.data[i]['x'], w))
                sign = 1 if inner_product > 0 else -1

                # if the sign != yn
                if sign != self.data[i]['y']:
                    for j in range(5):
                        w[j] = w[j]+miu*self.data[i]['y']*self.data[i]['x'][j]
                    update_times = update_times+1
                    k = 0
                else:
                    k = k+1
                if k == N:
                    break
                i = (i+1)%N
            all_times = all_times + update_times
        print all_times/float(2000)
    def pla_18(self):
        self.read_file_18()
        N = len(self.data)
        iteration = 2000
        avg_error_rate = 0
        for d in range(iteration):
            random.shuffle(self.data)
            i = 0
            k = 0
            head_w = [0, 0, 0, 0, 0]
            w = [0, 0, 0, 0, 0]
            update_times = 0
            while update_times < 50:
                # inner product
                inner_product = sum(p*q for p, q in zip(self.data[i]['x'], w))
                sign = 1 if inner_product > 0 else -1

                # if the sign != yn
                if sign != self.data[i]['y']:
                    for j in range(5):
                        w[j] = w[j] + self.data[i]['y']*self.data[i]['x'][j]
                    update_times = update_times+1
                    # cyclic testing for mistakes made by w & head_w
                    x = (i+1)%N
                    w_mistake = 0
                    head_w_mistake = 0
                    while x != i:
                        sign = 1 if sum(p*q for p, q in zip(self.data[x]['x'], w)) > 0 else -1
                        if sign != self.data[x]['y']:
                            w_mistake += 1
                        sign = 1 if sum(p*q for p, q in zip(self.data[x]['x'], head_w)) > 0 else -1
                        if sign != self.data[x]['y']:
                            head_w_mistake += 1
                        x = (x+1)%N
                    # if w make less mistakes, use w as head_w
                    if w_mistake < head_w_mistake:
                        head_w = [w[j] for j in range(5)]
                i = (i+1)%N
            # count the error rate
            error_times = 0
            for z in range(len(self.test)):
                sign = 1 if sum(p*q for p, q in zip(self.test[z]['x'], head_w)) > 0 else -1
                if sign != self.test[z]['y']:
                    error_times += 1
            avg_error_rate += error_times/float(len(self.test))
        #    print error_times/float(len(self.test))
        print avg_error_rate/float(iteration)
    def pla_19(self):
        self.read_file_18()
        N = len(self.data)
        iteration = 2000
        avg_error_rate = 0
        for d in range(iteration):
            random.shuffle(self.data)
            i = 0
            k = 0
            head_w = [0, 0, 0, 0, 0]
            w = [0, 0, 0, 0, 0]
            update_times = 0
            while 1:
                # inner product
                inner_product = sum(p*q for p, q in zip(self.data[i]['x'], w))
                sign = 1 if inner_product > 0 else -1

                # if the sign != yn
                if sign != self.data[i]['y']:
                    for j in range(5):
                        w[j] = w[j] + self.data[i]['y']*self.data[i]['x'][j]
                    update_times = update_times+1
                    # cyclic testing for mistakes made by w & head_w
                    x = i + 1
                    w_mistake = 0
                    head_w_mistake = 0
                    while x != i:
                        sign = 1 if sum(p*q for p, q in zip(self.data[x]['x'], w)) > 0 else -1
                        if sign != self.data[x]['y']:
                            w_mistake += 1
                        sign = 1 if sum(p*q for p, q in zip(self.data[x]['x'], head_w)) > 0 else -1
                        if sign != self.data[x]['y']:
                            head_w_mistake += 1
                        x = (x+1)%N
                    # if w make less mistakes, use w as head_w
                    if w_mistake < head_w_mistake:
                        head_w = [w[j] for j in range(5)]
                if update_times == 50:
                    break
                i = (i+1)%N
            # count the error rate
            error_times = 0
            for z in range(len(self.test)):
                sign = 1 if sum(p*q for p, q in zip(self.test[z]['x'], w)) > 0 else -1
                if sign != self.test[z]['y']:
                    error_times += 1
            avg_error_rate += error_times/float(len(self.test))
        #    print error_times/float(len(self.test))
        print avg_error_rate/float(iteration)
    def pla_20(self):
        self.read_file_18()
        N = len(self.data)
        iteration = 2000
        avg_error_rate = 0
        for d in range(iteration):
            random.shuffle(self.data)
            i = 0
            k = 0
            head_w = [0, 0, 0, 0, 0]
            w = [0, 0, 0, 0, 0]
            update_times = 0
            while 1:
                # inner product
                inner_product = sum(p*q for p, q in zip(self.data[i]['x'], w))
                sign = 1 if inner_product > 0 else -1

                # if the sign != yn
                if sign != self.data[i]['y']:
                    for j in range(5):
                        w[j] = w[j] + self.data[i]['y']*self.data[i]['x'][j]
                    update_times = update_times+1
                    # cyclic testing for mistakes made by w & head_w
                    x = i + 1
                    w_mistake = 0
                    head_w_mistake = 0
                    while x != i:
                        sign = 1 if sum(p*q for p, q in zip(self.data[x]['x'], w)) > 0 else -1
                        if sign != self.data[x]['y']:
                            w_mistake += 1
                        sign = 1 if sum(p*q for p, q in zip(self.data[x]['x'], head_w)) > 0 else -1
                        if sign != self.data[x]['y']:
                            head_w_mistake += 1
                        x = (x+1)%N
                    # if w make less mistakes, use w as head_w
                    if w_mistake < head_w_mistake:
                        head_w = [w[j] for j in range(5)]
                if update_times == 100:
                    break
                i = (i+1)%N
            # count the error rate
            error_times = 0
            for z in range(len(self.test)):
                sign = 1 if sum(p*q for p, q in zip(self.test[z]['x'], head_w)) > 0 else -1
                if sign != self.test[z]['y']:
                    error_times += 1
            avg_error_rate += error_times/float(len(self.test))
        #    print error_times/float(len(self.test))
        print avg_error_rate/float(iteration)
