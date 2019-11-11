import numpy as np
import matplotlib as mpl
import csv

# 日本語のフォントを設定
mpl.rcParams['font.family'] = 'sans-serif'
mpl.rcParams['font.sans-serif'] = ['Noto Sans CJK JP']
mpl.rcParams['font.size'] = 18
# 図を大きくする
mpl.rcParams['figure.figsize'] = 10, 6
import matplotlib.pyplot as plt

np.random.seed(0)

N = 1000

X = np.random.multivariate_normal([2.5, 0.5], [[0.6, 0], [0, 0.01]], N).reshape(N, 2)
X = np.append(X, np.ones((N, 1)), axis=1)


W = np.array([
    [0.3, 0.8],
    [3, 0.3],
    [0.2, 0.1]
])

Y = X @ W + np.random.normal(0, 0.5, (N, 2))

fig, ax = plt.subplots(1, 2, figsize=(18, 7))

sc = None
for i, a in enumerate(ax):
    sc = a.scatter(X[:, 0], X[:, 1], c=Y[:, i], s=20, vmin=0, vmax=4)
    plt.colorbar(sc, ax=a)
    a.set_xlim(0, 5)
    a.set_ylim(0, 1)
    a.set_xlabel("1日当たり勉強時間 [h]")
    a.set_ylabel("授業出席率")

ax[0].set_title("成績 [基本情報技術概論]")
ax[1].set_title("成績 [計算論]")
plt.show()

with open('data.csv', mode='w') as f:
    writer = csv.writer(f)
    for i in range(N):
        writer.writerow([ X[i][0], X[i][1], Y[i][0], Y[i][1] ])
