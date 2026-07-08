from collections import deque

def round_robin(processes, quantum):
    q = deque(processes)
    time = 0

    while q:
        name, burst = q.popleft()

        if burst <= quantum:
            time += burst
            print(name, "hoàn thành lúc", time)
        else:
            time += quantum
            q.append((name, burst - quantum))


processes = [
    ("P1",5),
    ("P2",3),
    ("P3",7)
]

round_robin(processes,2)