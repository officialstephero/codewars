class Primes:

    @staticmethod
    def stream(n=15486671):
        sieve = [True] * n
        for i in range(3, int(n ** 0.5) + 1, 2):
            if sieve[i]:
                sieve[i * i::2 * i] = [False] * ((n - i * i - 1) // (2 * i) + 1)
        return iter([2] + [i for i in range(3, n, 2) if sieve[i]])
