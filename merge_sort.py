import random
import matplotlib.pyplot as plt

def merge_sort(LIST):
    '''
    Returns sorted list.
    '''
    # Divide list into two parts
    start = []
    end = []
    a = min(LIST)
    b = max(LIST)
    
    while len(LIST)>1:
        start.append(a)
        end.append(b)
        try:
            LIST.remove(a)
            LIST.remove(b)
            a = min(LIST)
            b = max(LIST)
        except ValueError:
            continue
    end.reverse()
    return start + end

def visualize(LIST):
    '''
    Plots unsorted and sorted data.
    '''
    plt.plot(LIST)
    plt.xlabel('Random Data')
    plt.show()
    sorted_data = merge_sort(LIST)
    plt.plot(sorted_data)
    plt.xlabel('Merge Sorted Data')
    plt.show()

if __name__ == '__main__':
    # Basic Test
    LIST = [0,5,2,4,3,9,1,7,6,8]
    print ('Unordered list {}'.format(LIST))
    print ('Merge sorted list {}'.format(merge_sort(LIST)))
    # Generate a list of random length between 100 and 1000.
    # and add random numbers to it.
    LIST = [random.randint(0, 1000) for i in range(random.randint(100, 1000))]
    visualize(LIST)
    
    

