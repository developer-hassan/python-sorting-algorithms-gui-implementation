# Importing random module
import random


class Generator:
    '''
    Generates the random array for user in given range
    '''

    def create_random_array(array_size, lower_bound, upper_bound):
        '''
        create array from the user inputted values
        '''

        # Initializing the random array
        random_array = []

        for i in range(array_size):
            # Populating array with random integer in given range
            random_array.append(random.randint(lower_bound, upper_bound))

        # returning the populated array
        return random_array
