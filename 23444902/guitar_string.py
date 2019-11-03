"""
guitar_string.py

Models a guitar string.
"""

import math
import random
import ring_buffer
import stdarray
import stdio
import sys

# Sampling rate.
SPS = 44100


def create(frequency):

    """
    Create and return a guitar string of the given frequency, using a sampling
    rate given by SPS. A guitar string is represented as a ring buffer of
    of capacity N (SPS divided by frequency, rounded up to the nearest
    integer), with all values initialized to 0.0.
    """

    N = int(math.ceil(SPS / frequency))
    rb = ring_buffer.create(N)
    for i in range(N):
        ring_buffer.enqueue(rb, 0.0)
    return rb


def create_from_samples(init):

    """
    Create and return a guitar string whose size and initial values are given
    by the list init. Populate the ring buffer with values from init.
    Return the ring buffer.
    """

    capacity = len(init)
    rb = ring_buffer.create(capacity)
    for i in init:
        ring_buffer.enqueue(rb, i)
    return rb


def pluck(string):

    """
    Pluck the given guitar string by replacing the buffer with white noise.
    Replace each value (dequeue followed by enqueue) in the given ring
    buffer with a random number from the interval [-0.5, 0.5].
    """

    ring_buffer.dequeue(string)
    r = random.uniform(-0.5, 0.5)
    ring_buffer.enqueue(string, r)


def tic(string):

    """
    Advance the simulation one time step on the given guitar string by applying
    the Karplus-Strong update.
    Dequeue a value a in the given ring buffer and peek at the next value
    b. Enqueue the value 0.996 * 0.5 * (a+b) into the ring buffer.
    """

    a = ring_buffer.dequeue(string)
    b = ring_buffer.peek(string)
    ring_buffer.enqueue(string, 0.996 * 0.5 * (a + b))


def sample(string):

    """
    Peek and return the current sample from the given guitar string.
    """

    return ring_buffer.peek(string)


def _main():

    """
    Test client [DO NOT EDIT].
    """

    N = int(sys.argv[1])
    samples = [.2, .4, .5, .3, -.2, .4, .3, .0, -.1, -.3]
    test_string = create_from_samples(samples)
    for t in range(N):
        stdio.writef('%6d %8.4f\n', t, sample(test_string))
        tic(test_string)


if __name__ == '__main__':
    _main()
