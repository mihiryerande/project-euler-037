# Problem 37:
#     Truncatable Primes
#
# Description:
#     The number 3797 has an interesting property.
#     Being prime itself, it is possible to continuously remove digits from left to right,
#       and remain prime at each stage: 3797, 797, 97, and 7.
#     Similarly we can work from right to left: 3797, 379, 37, and 3.
#
#     Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

from typing import List, Set, Tuple


def is_prime(x: int, primes: Set[int]) -> bool:
    """
    Returns True iff `x` is a prime number.

    Args:
        x      (int):      Natural number
        primes (Set[int]): Set of all primes less than x

    Returns:
         (bool): True iff `x` is a prime number

    Raises:
        AssertError: if incorrect args are given
    """
    for q in primes:
        if x % q == 0:
            return False
    return True


def is_truncatable(x: int, primes: Set[int]) -> bool:
    """
    Returns True iff given prime `x` is 'dually' truncatable,
      meaning truncatable from left-to-right and right-to-left.

    Args:
        x      (int):      Prime number
        primes (Set[int]): Set of all primes less than `x`

    Returns:
        (bool): True iff `x` is dually truncatable
    """
    # Assume `x` itself is already prime
    # Check truncation in both directions using `primes`
    # Just do simple str/int manipulation to check
    s = str(x)
    n = len(s)
    return all(map(lambda q: q in primes, [int(s[i:]) for i in range(1, n)] + [int(s[:j]) for j in range(1, n)]))


def main() -> Tuple[List[int], int]:
    """
    Returns the list of exactly 11 primes which are truncatable from left-to-right and right-to-left,
      as well as the sum of those numbers.

    Returns:
        (Tuple[List[int], int]):
            Tuple of:
              * List[int] of 11 dually truncatable primes
              * Sum of those ^
    """
    # Accumulate a set of primes while searching
    primes = {2, 3, 5, 7}  # These aren't candidates, according to instructions

    # Check all odd numbers, storing primes as we find them, and also checking if dually truncatable.
    # Stopping after finding 11, since apparently that's how many there are.
    x = 3
    trunc_primes = []
    while len(trunc_primes) < 11:
        if is_prime(x, primes):
            if is_truncatable(x, primes):
                trunc_primes.append(x)
            primes.add(x)
        x += 2
    return trunc_primes, sum(trunc_primes)


if __name__ == '__main__':
    truncatable_primes, truncatable_sum = main()
    print('List of 11 truncatable primes:')
    for p in truncatable_primes:
        print('  {}'.format(p))
    print('Sum of truncatable primes:')
    print('  {}'.format(truncatable_sum))
