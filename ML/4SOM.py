#A.Self organizing maps(SOM)

from minisom import MiniSom
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

X = load_iris().data
X = StandardScaler().fit_transform(X)

som = MiniSom(7, 7, 4, sigma=1, learning_rate=0.5)

som.random_weights_init(X)
som.train_random(X, 1000)

plt.pcolor(som.distance_map().T, cmap='bone_r')
plt.colorbar()

for x in X:
    w = som.winner(x)
    plt.plot(w[0]+0.5, w[1]+0.5, 'o', mfc='none')

plt.title("Self Organizing Map")
plt.show()

print("Training Completed")




#B.K-Means Clustering

from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

X = load_iris().data

X = StandardScaler().fit_transform(X)

kmeans = KMeans(n_clusters=3, random_state=42)
clusters = kmeans.fit_predict(X)

plt.scatter(X[:,0], X[:,1], c=clusters)
plt.title("K-Means Clustering")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.show()

print("Cluster Labels:")
print(clusters)

#C. K-Means vs SOM comparison using Silhouette Score

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from minisom import MiniSom

data = pd.read_csv(r"C:\Users\student\Downloads\StudentsPerformance_with_headers.csv")

X = data[['Weekly study hours',
          'Attendance to classes',
          'Preparation to midterm exams 1',
          'Preparation to midterm exams 2',
          'GRADE']]

X = StandardScaler().fit_transform(X)

kmeans = KMeans(n_clusters=3, random_state=0)
k = kmeans.fit_predict(X)

som = MiniSom(3, 3, X.shape[1], learning_rate=0.5)
som.random_weights_init(X)
som.train_random(X, 500)

s = [som.winner(x)[0] * 3 + som.winner(x)[1] for x in X]

ks = silhouette_score(X, k)
ss = silhouette_score(X, s)

print("K-Means Score:", round(ks, 3))
print("SOM Score:", round(ss, 3))

if ks > ss:
    print("K-Means is better suitable")
else:
    print("SOM is better suitable")

plt.scatter(X[:,0], X[:,1], c=k, label="K-Means")
plt.scatter(X[:,0], X[:,1], c=s, marker="^", label="SOM")

plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.title("K-Means vs SOM")
plt.legend()
plt.show()
