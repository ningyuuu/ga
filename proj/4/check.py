import numpy as np

ans = [5.88480150e+00, 5.84317602e+00, 4.16254748e-02, 2.33288076e-11, 7.96860815e-11]

print("total calories:", np.dot(ans, [21, 16, 371, 346, 884]))
print("total protein:", np.dot(ans, [.85, 1.62, 12.78, 8.39, 0]))
print("total fat:", np.dot(ans, [.33, .2, 1.58, 1.39, 100]))
print("total carbohydrate:", np.dot(ans, [4.64, 2.37, 74.69, 80.7, 0]))
print("total sodium:", np.dot(ans, [9, 8, 7, 508.2, 0]))
print("total weight perc of greens:", (ans[1] + ans[2])/np.sum(ans))
