"""Determine windows sleep duration"""
import time

def print_times(delay):
    start_time = time.time()
    time.sleep(delay)

    stop_time = time.time() - start_time

    print(f'Delay time {delay}')
    print(f'Duration of delay {stop_time}')

l_time = [1, 2, 5]
lt_1s = [1,1,1,1]
dec_s = [0.01, 0.001,0.003]

# for x in l_time:
#     print_times(x)

# for x in lt_1s:
#     print_times(x)

for val in dec_s:
    for x in range(10):
        print_times(val)
    print('---------------------------------------')

