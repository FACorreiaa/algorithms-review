# O(log(N)) time | O(log(N)) space
# def searchForRange(array, target):
#     finalRange = [-1, 1]
#     alteredBinarySearch(array, target, 0, len(array) - 1, finalRange)
#     alteredBinarySearch(array, target, 0, len(array) - 1, finalRange)
#     return finalRange


# def alteredBinarySearch(array, target, left, right, finalRange, goLeft):
#     if left > right:
#         return
#     mid = (left + right) // 2
#     if array[mid] < target:
#         alteredBinarySearch(array, target, mid + 1, right, finalRange, goLeft)
#     elif array[mid] > target:
#         alteredBinarySearch(array, target, left, mid - 1, finalRange, goLeft)
#     else:
#         if goLeft:
#             if mid == 0 or array[mid - 1] != target:
#                 finalRange[0] = mid
#             else:
#                 alteredBinarySearch(array, target, left,
#                                     mid - 1, finalRange, goLeft)
#         else:
#             if mid == len(array) - 1 or array[mid + 1] != target:
#                 finalRange[1] = mid
#             else:
#                 alteredBinarySearch(array, target, mid + 1,
#                                     right, finalRange, goLeft)


def searchForRange(array, target):
    finalRange = [-1, 1]
    alteredBinarySearch(array, target, 0, len(array) - 1, finalRange)
    alteredBinarySearch(array, target, 0, len(array) - 1, finalRange)
    return finalRange

# O(log(N)) time | O(log(1) space)


def alteredBinarySearch(array, target, left, right, finalRange, goLeft):
    while left <= right:
        mid = (left + right) // 2
        if array[mid] < target:
            left = mid + 1
            # alteredBinarySearch(array, target, mid + 1,
            #                   right, finalRange, goLeft)
        elif array[mid] > target:
            right = mid - 1
            # alteredBinarySearch(array, target, left,
            #                    mid - 1, finalRange, goLeft)
        else:
            if goLeft:
                if mid == 0 or array[mid - 1] != target:
                    finalRange[0] = mid
                    return
                else:
                    right = mid - 1
                    # alteredBinarySearch(array, target, left,
                    #                     mid - 1, finalRange, goLeft)
            else:
                if mid == len(array) - 1 or array[mid + 1] != target:
                    finalRange[1] = mid
                    return
                else:
                    # alteredBinarySearch(array, target, mid + 1,
                    #                     right, finalRange, goLeft)
                    left = mid + 1
