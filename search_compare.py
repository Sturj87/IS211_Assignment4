import time
import random

# Saar T. CUNYSPS SPRING 2023
# IS211 A#4
def random_list(n):
    return random.sample(range(n), n)


def sequential_search(a_list, item):
    start = time.time()
    found = False
    for i in range(len(a_list)):
        if a_list[i] == item:
            found = True
            break
    end = time.time()
    return found, (end - start)


def ordered_sequential_search(a_list, item):
    start = time.time()
    a_list.sort()
    found = False
    for i in range(len(a_list)):
        if a_list[i] == item:
            found = True
            break
        elif a_list[i] > item:
            break
    end = time.time()
    return found, (end - start)

def binary_search_iterative(a_list, item):
    start = time.time()
    first = 0
    last = len(a_list) - 1
    found = False

    while first <= last:
        midpoint = (first + last) // 2

        if a_list[midpoint] == item:
            found = True
            break

        elif a_list[midpoint] > item:
            last = midpoint - 1

        else:
            first = midpoint + 1

    end = time.time()
    return found, (end - start)


def binary_search_recursive(a_list, item):
    start = time.time()
    if len(a_list) == 0:
        end = time.time()
        return False, (end - start)
    else:
        midpoint = len(a_list) // 2
        if a_list[midpoint] == item:
            end = time.time()
            return True, (end - start)
        else:
            if item < a_list[midpoint]:
                found, time_taken = binary_search_recursive(a_list[:midpoint], item)
            else:
                found, time_taken = binary_search_recursive(a_list[midpoint + 1:], item)
            end = time.time()
            return found, time_taken + (end - start)


def main():
    the_size = [500, 1000, 10000]
    search_functions = [sequential_search, ordered_sequential_search, binary_search_iterative, binary_search_recursive]

    for size in the_size:
        for search_function in search_functions:
            total_time = 0
            for i in range(100):
                mylist = random_list(size)
                found, time_taken = search_function(mylist, -1)
                total_time += time_taken
            avg_time = total_time / 100
            print(
                f"{search_function.__name__} took {avg_time:.7f} seconds to run, on average for a list of {size} elements.")
        print()


if __name__ == "__main__":
    main()
