import threading

# Exercise 1: Threaded Prime Number Checker
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def check_primes(start, end, result):
    for number in range(start, end):
        if is_prime(number):
            result.append(number)

def threaded_prime_checker(start, end, num_threads):
    threads = []
    result = []
    step = (end - start) // num_threads
    for i in range(num_threads):
        s = start + i * step
        e = start + (i + 1) * step if i != num_threads - 1 else end
        t = threading.Thread(target=check_primes, args=(s, e, result))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    print(sorted(result))

# Exercise 2: Threaded File Processing
from collections import defaultdict

def count_words(lines, result):
    local_count = defaultdict(int)
    for line in lines:
        words = line.strip().split()
        for word in words:
            local_count[word] += 1
    result.append(local_count)

def threaded_word_count(file_path, num_threads):
    with open(file_path, 'r') as f:
        lines = f.readlines()
    chunk_size = len(lines) // num_threads
    threads = []
    results = []
    for i in range(num_threads):
        chunk = lines[i*chunk_size : (i+1)*chunk_size] if i != num_threads - 1 else lines[i*chunk_size:]
        t = threading.Thread(target=count_words, args=(chunk, results))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    final_count = defaultdict(int)
    for partial in results:
        for word, count in partial.items():
            final_count[word] += count
    for word, count in sorted(final_count.items()):
        print(f"{word}: {count}")
