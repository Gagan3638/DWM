from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs

x, _ = make_blobs(n_samples=100, centers=3, random_state=42)