# http://projecteuler.net/thread=35;page=7

class primes(object):
    """
    the primes with memoization
    """
    #: is N a prime? - initial filling for 0, 1, 2, and 3
    _is_prime = [ False, False, True, True ]
    #: default amount to grow
    DEFAULT_GROWTH = 1000

    def __iter__(self):
        """
        produce primes ad infinitum
        """
        idx = 0
        while True:
            idx += 1
            if idx >= len(self._is_prime):
                self.extend()
            while not self._is_prime[idx]:
                idx += 1
                if idx >= len(self._is_prime):
                    self.extend()
            yield idx

    def extend(self,grow_by=None,grow_upto=None):
        """
        extend by or upto
        """
        if grow_by is None:
            if grow_upto is None:
                grow_by = self.DEFAULT_GROWTH
            else:
                grow_by = grow_upto - len(self._is_prime) + 1
        #
        if grow_by <= 0:
            return
        #
        old_len = len(self._is_prime)
        #
        self._is_prime.extend( [ True ] * grow_by )
        #
        for idx in range( len(self._is_prime) // 2 ):
            if self._is_prime[idx]:
                k = max( old_len // idx, 2 )
                for jdx in range( k*idx, len(self._is_prime), idx ):
                    self._is_prime[jdx] = False

    def upto(self,n):
        """
        iterator for primes upto n
        """
        self.extend(grow_upto=n)
        for p in self:
            if p > n: break
            yield p

    def is_prime(self, p):
        """
        check iff p is a prime
        """
        self.extend(grow_upto=p)
        return self._is_prime[p]