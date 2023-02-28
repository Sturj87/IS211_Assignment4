import random
import time

# Saar T. CUNYSPS SPRING 2023
# IS211 A#4

def random_list(length):
    r_list = []
    for i in range(length):
        r_list.append(random.randint(1, 1000))
    return r_list


def insertion_sort(my_list):

    for i in range(1, len(my_list)):
        current = my_list[i]
        j = i - 1
        while j >= 0 and my_list[j] > current:
            my_list[j + 1] = my_list[j]
            j -= 1
        my_list[j + 1] = current

def shell_sort(my_list):

    for i in range(len(my_list)):
        for j in range(len(my_list) - i - 1):
            if my_list[j] > my_list[j + 1]:
                my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]

def python_sort(my_list):

    for i in range(len(my_list)):
        min_index = i
        for j in range(i + 1, len(my_list)):
            if my_list[j] < my_list[min_index]:
                min_index = j
        my_list[i], my_list[min_index] = my_list[min_index], my_list[i]


def main():

    list_lengths = [500, 1000, 10000]

    for length in list_lengths:
        print(f"Testing sort algorithms on a list of {length} integers")
        r_list = random_list(length)

        start = time.time()
        sorted_list = sorted(r_list)
        end = time.time()
        python_sort_time = end - start
        print(f"Python's built-in sort took {python_sort_time:.6f} seconds")

        start = time.time()
        shell_sort(r_list.copy())
        end = time.time()
        shell_sort_time = end - start
        print(f"Shell sort took {shell_sort_time:.6f} seconds")

        start = time.time()
        python_sort(r_list.copy())
        end = time.time()
        python_sort_time = end - start
        print(f"Python sort took {python_sort_time:.6f} seconds")

        start = time.time()
        insertion_sort(r_list.copy())
        end = time.time()
        insertion_sort_time = end - start
        print(f"Insertion sort took {insertion_sort_time:.6f} seconds")

if __name__ == "__main__":
    main()
