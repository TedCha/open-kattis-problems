n, p, k = list(map(int, input().split()))
events = list(map(int, input().split()))

events.append(k)

last_event = 0
orig_length = 0.0
multiplier = 1.0

for i in range(len(events)):
    orig_length += (events[i] - last_event) * multiplier
    multiplier = (100 + (p * (i+1))) / 100
    last_event = events[i]

print(f"{orig_length:.6f}")
