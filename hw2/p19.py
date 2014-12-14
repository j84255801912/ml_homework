import random
class p19(object):
    def __init__(self):
        self.data = []
        self.test = []
    def read_file(self):
        fp = open("hw2_train.dat")
        while 1:
            line = fp.readline()
            line = line[1:].replace('\n', '')
            if line == "":
                break;
            exploded = line.replace('\t', ' ').split(' ')
            self.data.append({
                                'x' : [float(exploded[0]), float(exploded[1]), float(exploded[2]), float(exploded[3]), float(exploded[4]), float(exploded[5]), float(exploded[6]), float(exploded[7]), float(exploded[8])],
                                'y' : int(exploded[9])
                             })
        fp = open("hw2_test.dat")
        while 1:
            line = fp.readline()
            line = line[1:].replace('\n', '')
            if line == "":
                break;
            exploded = line.replace('\t', ' ').split(' ')
            self.test.append({
                                'x' : [float(exploded[0]), float(exploded[1]), float(exploded[2]), float(exploded[3]), float(exploded[4]), float(exploded[5]), float(exploded[6]), float(exploded[7]), float(exploded[8])],
                                'y' : int(exploded[9])
                             })
if __name__ == "__main__":
    temp = p19()
    temp.read_file()
    avg_error_rate = 0
    the_real_ein = 100
    for z in range(9):
        #x = [random.uniform(-1, 1) for i in range(20)]
        x = [temp.data[i]['x'][z] for i in range(len(temp.data))]
        y = [temp.data[i]['y'] for i in range(len(temp.data))]
        x, y = zip(*sorted(zip(x, y)))
        """
        y = [1 if x[i] > 0 else -1 for i in range(20)]
        for i in range(20):
            if random.uniform(0, 10) < 2:
                y[i] = y[i] * (-1)
        """
        best_error = len(temp.data)
        best_s = -1
        best_theta = 0
        for s in {-1, 1}:
            for theta in range(len(x)+1):
                error = 0
                for j in range(len(x)):
                    if j >= theta:
                        if y[j] != s:
                            error += 1
                    else:
                        if y[j] != (-1)*s:
                            error += 1
                if error < best_error:
                    best_error = error
                    if theta == 0:
                        best_theta = -100
                    elif theta == len(x):
                        best_theta = 100
                    else:
                        best_theta = (x[theta-1]+x[theta])/float(2)
                    best_s = s
        if best_error/float(len(temp.data)) < the_real_ein:
            the_real_ein = best_error/float(len(temp.data))
    #    avg_error_out_rate += 0.5+0.3*best_s*(abs(best_theta)-1)
    print the_real_ein
