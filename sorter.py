class Sorter:
    '''
    Class to perform different sorting algorithms
    '''
    @staticmethod
    def insertion_sort(array: list) -> list:
        '''
        Static method to sort the array using insertion sort
        '''
        # Create copy of array
        array_copy = array[:]
        # For i from 1 to n - 1
        for i in range(1, len(array)):
            j = i
            # Insert ith element at appropriate position in the left portion
            while j > 0 and array_copy[j] < array_copy[j - 1]:
                Sorter.__swap(array_copy, j, j - 1)
                j -= 1
        # Return this sorted copy of the array
        return array_copy

    @staticmethod
    def heap_sort(array: list) -> list:
        '''
        Static method to sort the array using heap sort
        '''
        array_copy = array[:]  # Create a copy of the array
        last_index = len(array_copy) - 1  # Last index
        # Build heap till last index
        Sorter.__build_heap(array_copy, last_index)
        # While the last index hasn't reached the first element
        while last_index > 0:
            # Perform heapify operation till the last index
            Sorter.__heapify(array_copy, 0, last_index)
            # Now the first element contains the maximum element, swap it with last index
            Sorter.__swap(array_copy, 0, last_index)
            # Reduce the last index by 1
            last_index -= 1
        # Return the sorted copy of the array
        return array_copy

    @staticmethod
    def counting_sort(array):
        '''
        Static method to sort the array using counting sort
        '''
        array_copy = array[:]

        # Get the minimum and maximum element
        minimum = min(array_copy)
        maximum = max(array_copy)

        # The size of frequency array will be the difference + 1
        size = (maximum - minimum) + 1

        # Frequency array of specified size, filled with 0
        frequency_array = [0 for i in range(size+1)]

        # For each element in array, increment it's corresponding index frequency
        # by 1. We are subtracting min element from array element. It will make the
        # minimum element map to 0 either if it's positive or negative. It will
        # also make better use of space if the array is only positive because size
        # will be (max - min) + 1 rather than max + 1

        for i in range(len(array_copy)):
            frequency_array[array_copy[i] - minimum] += 1

        sortedIndex = 0             # Index to place sorted value on in the array

        # For each frequency in the frequency array
        for i in range(len(frequency_array)):

            # While the frequency is greater than 0
            occurences = frequency_array[i]
            while (occurences > 0):
                # Add the element + min at sorted index (to map frequency array
                # index back to element, as we subtracted it earlier to convert
                # element into frequency array index). Increment sorted index and
                # decrement the frequency
                array_copy[sortedIndex] = i + minimum
                sortedIndex += 1
                occurences -= 1

        return array_copy

    @staticmethod
    def quick_sort(array: list) -> list:
        '''
        Static method to sort the array using quick sort
        '''
        array_copy = array[:]   # Create a copy of the array

        # Call the helper recursive function from 0 to (size - 1)
        Sorter.__helper_quick_sort(array_copy, 0, len(array_copy)-1)

        return array_copy

    @staticmethod
    def __helper_quick_sort(array, start, end):
        '''
        Private Static method to help the quicksort method in implemention with proper parameters
        '''
        # Applying Recursive case
        if start < end:

            # Calls the helper function to Select and place pivot on appropriate position
            pivot_index = Sorter.__select_and_place_pivot_on_its_place(
                array, start, end)

            # Recursively repeating the quicksort algorithm for left and right sub arrays
            Sorter.__helper_quick_sort(array, start, pivot_index - 1)
            Sorter.__helper_quick_sort(array, pivot_index + 1, end)

    @staticmethod
    def __select_and_place_pivot_on_its_place(array: list, start: int, end: int) -> None:
        '''
        Helper function that selects a pivot and places it on it's appropriate position
        '''
        pivot = array[end]  # Select the last element as pivot
        i = start - 1       # Pointer at previous index of pivot's position

        # Start j from start to second last element
        for j in range(start, end):
            # If jth element is less than pivot
            if array[j] < pivot:
                # Increment the i's previous position and swap ith and jth element
                i += 1
                Sorter.__swap(array, i, j)

        # Swap the pivot with it's new position and return this position
        Sorter.__swap(array, i + 1, end)
        return i + 1

    @staticmethod
    def __build_heap(array: list, size: int):
        '''
        Perform heapify operation from 2nd last level upto root
        '''
        middle = int(len(array) / 2)
        while middle >= 0:
            Sorter.__heapify(array, middle, size)
            middle -= 1

    @staticmethod
    def __heapify(array: list, index: int, size: int) -> None:
        '''
        Performs heapify operation on the max heap to restore heap property
        '''
        max_child = Sorter.__left_child_index(index)
        right_child = Sorter.__right_child_index(index)
        if max_child > size:
            return
        elif right_child <= size:
            if array[right_child] > array[max_child]:
                max_child = right_child

        if array[index] < array[max_child]:
            Sorter.__swap(array, index, max_child)
        Sorter.__heapify(array, max_child, size)

    @staticmethod
    def __left_child_index(index: int) -> int:
        '''
        Private helper static method to get the left child of node
        '''
        return index * 2 + 1

    @staticmethod
    def __right_child_index(index: int) -> int:
        '''
        Private helper static method to get the right child of node
        '''
        return Sorter.__left_child_index(index) + 1

    @staticmethod
    def __swap(array: list, x: int, y: int):
        '''
        Private helper static method to swap elements at x and y of array
        '''
        temp = array[x]
        array[x] = array[y]
        array[y] = temp
