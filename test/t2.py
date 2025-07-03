from sklearn.cluster import KMeans

tmp = input().split()
n, d, k = int(tmp[0]), int(tmp[1]), int(tmp[2])

X = []

for i in range(n):
    X.append([float(x) for x in input().split()])

kmeans = KMeans(n_clusters=k, random_state=0)
y_kmeans = kmeans.fit_predict(X)


# 按聚类分组，计算每组均值
import numpy as np
X = np.array(X)
for i in range(k):
    group = X[y_kmeans == i]
    means = group.mean(axis=0)
    print(' '.join(f"{x:.2f}" for x in means))
