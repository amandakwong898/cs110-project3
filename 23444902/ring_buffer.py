"""
ring_buffer.py

Models a ring buffer.
"""

import stdarray
import stdio
import sys


def create(capacity):
    """
    Create and return a ring buffer, with the given maximum capacity and
    with all elements initialized to None. A ring buffer is represented as
    a list of four elements: the buffer (buff) itself as a list; number of
    elements (size) currently in buff; the index (first) of the least
    recently inserted item; and the index (last) one beyond the most recently
    inserted item.
    """

    buffer = stdarray.create1D(capacity, None)
    rb = [buffer, 0, 0, 0]
    return rb


def capacity(rb):

    """
    Return the capacity of the ring buffer.
    """

    return len(rb[0])


def size(rb):

    """
    Return the number of items currently in the buffer rb.
    """
    return rb[1]


def is_empty(rb):

    """
    Return True if the buffer rb is empty (ie, its size is 0), and False
    otherwise.
    """

    if (rb[1] == 0):
        return True
    else:
        return False


def is_full(rb):

    """
    Return True if the buffer rb is full (ie, its size equals its capacity),
    and False otherwise.
    """

    if (capacity(rb) == size(rb)):
        return True
    else:
        return False


def enqueue(rb, x):

    """
    Store x at buff[last] in the given ring buffer. If last + 1 equals
    capacity, set last to 0; otherwise, increment it by 1. Increment size
    by 1. Add item x to the end of the buffer rb.
    """

    if(is_full(rb)):
        sys.exit("Error: cannot enqueue a full buffer.")

    rb[0][rb[3]] = x
    if (rb[3] + 1 == capacity(rb)):
        rb[3] = 0
    else:
        rb[3] += 1
    rb[1] += 1


def dequeue(rb):

    """
    Assign the item buff[first] in the given ring buffer to some
    variable v. If first + 1 equals capacity, set first to 0;
    otherwise, incrememnt it by 1. Decrement size by 1. Return v.
    Delete and return item from the front of the buffer rb.
    """

    if(is_empty(rb)):
        sys.exit("Error: cannot dequeue an empty buffer.")
    v = rb[0][rb[2]]
    if(rb[2] + 1 == capacity(rb)):
        rb[2] = 0
    else:
        rb[2] += 1
    rb[1] -= 1

    return v


def peek(rb):

    """
    Return the item buff[first] in the given ring buffer.
    Return (but do not delete) item from the front of the buffer rb.
    """

    if(is_empty(rb)):
        sys.exit("Error: cannot peek an empty buffer.")
    return rb[0][rb[2]]


def _main():

    """
    Test client [DO NOT EDIT].
    """

    N = int(sys.argv[1])
    rb = create(N)
    for i in range(1, N + 1):
        enqueue(rb, i)
    t = dequeue(rb)
    enqueue(rb, t)
    stdio.writef('Size after wrap-around is %d\n', size(rb))
    while size(rb) >= 2:
        x = dequeue(rb)
        y = dequeue(rb)
        enqueue(rb, x + y)
    stdio.writeln(peek(rb))


if __name__ == '__main__':
    _main()
