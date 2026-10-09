import numpy as np
data = np.array([4.0, np.nan, 8.0, -np.inf, 12.0])
print(np.isnan(data))#Mask for NaN entries
print(data[np.isfinite(data)])#Select only finite values
mean=data[np.isfinite(data)].mean()#Find their mean.
print(mean)
copy=data.copy()
copy[~np.isfinite(copy)]=mean#Make a copy where every non-finite value is replaced with that mean.
print(copy)