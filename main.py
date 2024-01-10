import matplotlib.pyplot as plt
import numpy as np


def xor_verification(x1, x2):
    if x1 >= 0.5 and x2 >= 0.5:
        return False
    elif x1 < 0.5 and x2 < 0.5:
        return False
    elif x1 >= 0.5 and x2 < 0.5:
        return True
    elif x1 < 0.5 and x2 >= 0.5:
        return True


def result_verification(result):
    if result >= 0.5:
        return True
    else:
        return False


if __name__ == "__main__":

    w1_1_1 = 3.4243
    w1_2_1 = 3.4299
    b1_1 = -5.3119

    w1_1_2 = 4.4863
    w1_2_2 = 4.4830
    b1_2 = -1.7982

    w2_1 = -7.1722
    w2_2 = 6.7997
    b2 = -3.0611

    INTERVAL = 100

    x1_val = np.linspace(0, 1, INTERVAL)
    x2_val = np.linspace(0, 1, INTERVAL)

    x1_val = list(map(lambda x: x + 1/(INTERVAL*2), x1_val))
    x2_val = list(map(lambda x: x + 1/(INTERVAL*2), x2_val))

    correct_x1_list = []
    correct_x2_list = []
    wrong_x1_list = []
    wrong_x2_list = []
    correct_count = 0
    wrong_count = 0
    for x1 in x1_val:
        for x2 in x2_val:
            f1_1_input = x1*w1_1_1 + x2*w1_2_1 + b1_1
            f2_1_input = x1*w1_1_2 + x2*w1_2_2 + b1_2

            f1_1 = 1/(1 + np.exp(-1*f1_1_input))
            f2_1 = 1/(1 + np.exp(-1*f2_1_input))

            f_xor_input = f1_1*w2_1 + f2_1*w2_2 + b2
            f_xor = 1/(1 + np.exp(-1*f_xor_input))
            if xor_verification(x1, x2) == result_verification(f_xor):
                correct_x1_list.append(x1)
                correct_x2_list.append(x2)
                correct_count += 1
            else:
                wrong_x1_list.append(x1)
                wrong_x2_list.append(x2)
                wrong_count += 1

    plt.xlim([0, 1])      # X축의 범위: [xmin, xmax]
    plt.ylim([0, 1])     # Y축의 범위: [ymin, ymax]

    plt.plot(correct_x1_list, correct_x2_list, 'gs', wrong_x1_list, wrong_x2_list, 'rs')
    plt.xticks(np.arange(0, 1.1, 0.1))
    plt.yticks(np.arange(0, 1.1, 0.1))
    plt.text(0, -0.1, "Number of correct values:" + str(correct_count))
    plt.text(0.5, -0.1, "Number of wrong values:" + str(wrong_count))
    plt.show()


