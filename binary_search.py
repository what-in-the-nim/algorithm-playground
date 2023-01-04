def bin_search(sorted_array: list[int], pointer: list[int], target: int):
    length = len(sorted_array)
    if length == 1:
        return pointer[0]

    midpoint = length // 2
    if sorted_array[midpoint] > target:
        return bin_search(sorted_array[:midpoint], pointer[:midpoint], target)
    else:
        return bin_search(sorted_array[midpoint:], pointer[midpoint:], target)

if __name__ == '__main__':
    array = [2,5,6,7,8,9,10,16,17,18,19]
    print(bin_search(array, list(range(len(array))), 19))