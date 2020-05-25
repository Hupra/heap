from my_sorting_object import X


#   Time complexity
#   O(n) amortized -> one would think its O(n*log(n))
#
#   Space complexity
#   O(n)

def siftdown(a, i, n):
    top = i
    left = 2 * i + 1  # i = 5 l = 11
    right = 2 * i + 2  # i = 5 r = 12

    # check if left is out of range
    if left < n and a[left] > a[top]:
        top = left

    if right < n and a[right] > a[top]:
        top = right

    if i != top:
        # swap values
        a[i], a[top] = a[top], a[i]

        # we call siftdown again to make sure our change
        # didnt ruin something further down the tree, we do
        # this recursivly all the way to the root of the tree (the top)
        siftdown(a, top, n)


def heap_sort(a):
    n = len(a)

    # -- heapify --
    # starts our maxheap
    # we go backwards because we wanna,
    # start at the bottom of the tree.
    # loop from n to/including 0 -> 5,4,3,2,1,0
    for i in reversed(range(n // 2)):
        siftdown(a, i, n)

    # extract the numbers
    # we loop backwards because we put the largest number at the end
    # and then dont look at them again
    for i in reversed(range(n)):
        # swap the numbers because we want the largest number last
        # and then because of our loop we dont look at it again
        a[i], a[0] = a[0], a[i]

        # we want the next largest value at the top so we have to run heapify again
        # we use "i" as the third value because we dont wanna look at values after that
        # because that part is already sorted
        siftdown(a, 0, i)


if __name__ == "__main__":

    a = [X(3, "a"), X(3, "b"), X(1, "a"), X(9, "a"), X(4, "a"), X(9, "b"), X(3, "c"), X(5, "c"), X(6, "a"), X(7, "a")]
    print(a)
    heap_sort(a)
    print(a)

    print("----")

    a = [X(3, "a"), X(3, "b"), X(3, "c")]
    print(a)
    heap_sort(a)
    print(a)

    #
    #
    #
    #    (a)        {c}        (c)        {b}        (b)
    #    / \   ->   / \   ->   / \   ->   / \   ->   / \   ->   / \
    #  (b) (c)    (b) {a}    (b)        {c}
    #   start      swaps      pops       swaps      pops        DONE
    #             [0][-1]     [-1]      [0][-2]     [-2]
    #
    #  [a,b,c]    [c,b,c]    [c,b,a]    [b,c,a]    [b,c,a]     [b,c,a]
    #
    #
