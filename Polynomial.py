

def main():
    f, g = [1, 2, 3], [4, 5]
    print(Polynomial.add(f, g))
    print(Polynomial.subtract(f, g))
    print(Polynomial.root(g, -1000, 1000, 0.001))

class Polynomial:
    """ f(x) = a0 + a1 * x + a2 * x ^ 2 + ... + an-1 * x ^ (n - 1) """

    @staticmethod
    def remove_trailing_zeroes(f):
        """ Removes trailing zeroes from f. Example: [0 1 0 2 0 0 0] -> [0 1 0 2]. """
        g = f[:]
        i = len(f) - 1
        while g[i] == 0 and 0 <= i:
            g.remove(i)
            i -= 1
        return g

    @staticmethod
    def add_trailing_zeroes(f, n):
        """ Append n zeroes to the end of f. Example: n = 3, [0 1 0 2] -> [0 1 0 2 0 0 0]. """
        return f[:] + [0 for i in range(n)]

    @staticmethod
    def add(f, g):
        """ Returns f + g. """
        if len(f) < len(g):
            h = g[:]
            for i, fi in enumerate(f):
                h[i] += fi
        else:
            h = f[:]
            for i, gi in enumerate(g):
                h[i] += gi
        return h

    @staticmethod
    def subtract(f, g):
        """ Returns f - g. """
        return Polynomial.add(f, Polynomial.scalar_multiply(g, -1))

    @staticmethod
    def scalar_multiply(f, a):
        """ Returns f * a. """
        return [fi * a for fi in f]

    @staticmethod
    def root(f, a, b, e):
        """ Finds or approximates the root of a polynomial f on the range [a, b]. """
        g = Polynomial.remove_trailing_zeroes(f)
        c = a + (b - a) / 2
        if e < b - a:
            ga, gb, gc = Polynomial.evaluate(g, a), Polynomial.evaluate(g, b), Polynomial.evaluate(g, c)
            if ga * gc < 0:
                r = Polynomial.root(g, a, c, e)
            elif gb * gc < 0:
                r = Polynomial.root(g, c, b, e)
            else:
                r = gc
        else:
            r = gc
        return r

    @staticmethod
    def evaluate(f, x):
        y = 0
        for i, fi in enumerate(f):
            y += fi * x ** i
        return y

main()
