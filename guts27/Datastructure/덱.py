import sys
input = sys.stdin.readline
N = int(input())
deque = []

for _ in range(N):
    command = input().split()
    if 'push_front' == command[0]:
        temp = [int(command[1])]
        deque = temp+deque
    elif 'push_back' == command[0]:
        deque.append(int(command[1]))
    elif command[0] == 'pop_front':
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[0])
            deque = deque[1:]
    elif command[0] == 'pop_back':
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[-1])
            deque.pop()
    elif command[0] == 'size':
        print(len(deque))
    elif command[0] == 'empty':
        if len(deque) == 0:
            print(1)
        else:
            print(0)
    elif command[0] == 'front':
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[0])
    elif command[0] == 'back':
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[-1])
```

```kotlin
import sys
from collections import deque

input = sys.stdin.readline
N = int(input())
queue = deque([])

for i in range(N):
    command = input().split()
    
    if command[0] == "push_front":
        queue.appendleft(int(command[1]))
    
    elif command[0] == "push_back":
        queue.append(int(command[1]))
    
    elif command[0] == "pop_front":
        if queue:
            print (queue.popleft())
        else:
            print (-1)

    elif command[0] == "pop_back":
        if queue:
            print (queue.pop())
        else:
            print (-1)
    
    elif command[0] == "size":
        print (len(queue))
    
    elif command[0] == "empty":
        if queue:
            print (0)
        else:
            print (1)

    elif command[0] == "front":
        if queue:
            print (queue[0])
        else:
            print (-1)
        
    elif command[0] == "back":
        if queue:
            print (queue[-1])
        else:
            print (-1)


