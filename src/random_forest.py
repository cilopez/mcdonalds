import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y ,test_size=0.35, random_state = 1996)
model = RandomForestRegressor(min_samples_leaf=3,max_depth=4,criterion='mae')
model.fit(X_train,np.ravel(y_train))