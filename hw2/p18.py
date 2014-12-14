import random
class p18(object):
    if __name__ == "__main__":
    #    avg_error_rate = 0
        avg_error_out_rate = 0
        for z in range(5000):
            x = [random.uniform(-1, 1) for i in range(20)]
            x = sorted(x)
            y = [1 if x[i] > 0 else -1 for i in range(20)]
            for i in range(20):
                if random.uniform(0, 10) < 2:
                    y[i] = y[i] * (-1)
            best_error = 20
            best_s = -1
            best_theta = 0
            for s in {-1, 1}:
                for theta in range(21):
                    error = 0
                    for j in range(20):
                        if s == 1:
                            if j >= theta:
                                if y[j] != 1:
                                    error += 1
                            else:
                                if y[j] != -1:
                                    error += 1
                        else:
                            if j >= theta:
                                if y[j] != -1:
                                    error += 1
                            else:
                                if y[j] != 1:
                                    error += 1
                    if error < best_error:
                        best_error = error
                        if theta == 0:
                            best_theta = -1
                        elif theta == 20:
                            best_theta = 1
                        else:
                            best_theta = (x[theta-1]+x[theta])/float(2)
                        best_s = s
        #    avg_error_rate += best_error/float(len(x))
            avg_error_out_rate += 0.5+0.3*best_s*(abs(best_theta)-1)
        #print avg_error_rate/float(5000)
        print avg_error_out_rate/float(5000)
