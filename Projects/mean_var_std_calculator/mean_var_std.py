import numpy as np

def calculate(list):
    '''
    use Numpy to output the mean, variance, standard deviation, max, min, and sum of the rows, columns, and elements in a 3 x 3 matrix.
    input: a list containing 9 digits
    return:  a dictionary containing the mean, variance, standard deviation, max, min, and sum along both axes and for the flattened matrix as a list
    '''
    # Check if the list has size 9
    if (len(list) != 9):
        raise ValueError("List must contain nine numbers.")

    # create a matrix from the list and make it 3 x 3
    matrix = np.reshape(np.array(list), (3,3)) 

    # create a dictionary to hold the results
    calculations = {}

    # Compute the stats
    # Each stat is a list of the results on axis=0, axis=1, and flattened matrix
    calculations['mean'] = [matrix.mean(axis=0).tolist(), # axis=0
                            matrix.mean(axis=1).tolist(), # axis=1
                            matrix.mean()]                # flattened
    calculations['variance'] = [matrix.var(axis=0).tolist(),
                                matrix.var(axis=1).tolist(), 
                                matrix.var()]
    calculations['standard deviation'] = [matrix.std(axis=0).tolist(),
                                          matrix.std(axis=1).tolist(), 
                                          matrix.std()]
    calculations['max'] = [matrix.max(axis=0).tolist(),
                           matrix.max(axis=1).tolist(), 
                           matrix.max()]
    calculations['min'] = [matrix.min(axis=0).tolist(),
                           matrix.min(axis=1).tolist(), 
                           matrix.min()]
    calculations['sum'] = [matrix.sum(axis=0).tolist(),
                           matrix.sum(axis=1).tolist(), 
                           matrix.sum()]
    return calculations
     
