import numpy as np

def my_own_error_function(y_pred=np.array([1,32,3]), y_obs=np.array([12,34,56])):
    
    return (y_pred - y_obs)