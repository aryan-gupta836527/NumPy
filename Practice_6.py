import numpy as np
data = np.array([4.0, np.nan, 8.0, -np.inf, 12.0])
print(np.isnan(data))
print(data[np.isfinite(data)])
mean=data[np.isfinite(data)].mean()
print(mean)
copy=data.copy()
copy[~np.isfinite(copy)]=mean
print(copy)