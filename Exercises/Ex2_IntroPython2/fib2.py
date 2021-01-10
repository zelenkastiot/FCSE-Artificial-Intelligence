class Fib2:
    def __init__(self):
        self.fn2 = 1
        self.fn1 = 1
    
    def __next__(self):
        """
        next() - добивање на следни вредности
        """
        (self.fn1, self.fn2, old_fn2) = (self.fn1 + self.fn2, self.fn1, self.fn2)
        
        return old_fn2

    def __iter__(self):
        return self