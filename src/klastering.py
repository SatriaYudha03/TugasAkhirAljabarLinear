#UAS ALJABAR LINEAR
#NAMA: Made Satria Yudha Negara
#NIM: 2305551058
#KELAS: Aljabar Linear C

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

#Baca dataset
data = pd.read_csv('Default_Fin.csv')

#Pilih kolom yang digunakan untuk klastering
selected_features = ['Bank Balance','Annual Salary']

#Preprocesing
X = data[selected_features]

print(X.head())

# Visualisasi data sebelum klastering
plt.scatter(X['Bank Balance'], X['Annual Salary'])
plt.xlabel('Bank Balance')
plt.ylabel('Annual Salary')
plt.title('Scatter Plot Based on Bank Balance and Annual Salary')
plt.show()

# Plot hasil Elbow method
plt.plot(cluster_range, inertias, 'bo-')
plt.title('Elbow Method')
plt.xlabel('Jumlah Cluster')
plt.ylabel('Inertia')
plt.show()

#Metode Elbow digunakan untuk menentukan jumlah cluster yang optimal dengan mencari titik "siku" pada grafik.
#Titik ini adalah tempat di mana penurunan inertia mulai melambat secara signifikan.
#Dari gambar tersebut, terlihat bahwa penurunan inertia mulai melambat setelah 3 cluster.
#Ini menunjukkan bahwa jumlah cluster yang optimal kemungkinan adalah 3.

#Melihat titik tengah dari setiap cluster
kmeans.cluster_centers_
# Tampilkan centroid
print("Centroids:", kmeans.cluster_centers_)

# Visualisasi hasil klastering
plt.scatter(X.values[:, 0], X.values[:, 1], c=y_kmeans, cmap='viridis')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=300, c='red', label='Centroids')
plt.xlabel('Bank Balance')
plt.ylabel('Annual Salary')
plt.title('Clustering Result')
plt.legend()
plt.show()
