from _collections import deque

if __name__ == "__main__":
    line = deque()
    # Stan is first in the queue
    line.append("Stan")
    line.append("Willie")
    line.append("Bubba")

    # Pop the first element
    print(line.popleft())
