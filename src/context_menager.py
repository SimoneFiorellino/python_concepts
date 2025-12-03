"""
Context managers allow you to allocate and release resources precisely when you want to. 
The most widely used example of context managers is the with statement. 
Suppose you have two related operations which you’d like to execute as a pair, with a block of code in between. 
Context managers allow you to do specifically that. 
For example:

with open('some_file', 'w') as opened_file:
    opened_file.write('Hola!')

Implementing a CM as a class:
class File(object):
    def __init__(self, file_name, method):
        self.file_obj = open(file_name, method)
    def __enter__(self):
        return self.file_obj
    def __exit__(self, type, value, traceback):
        self.file_obj.close()
"""

import time

class Timer:
    def __enter__(self):
        self.start_time = time.time()
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        print(exc_type, exc_value, traceback) # For debugging purposes
        self.end_time = time.time()
        self.elapsed_time = self.end_time - self.start_time
        print(f"Elapsed time: {self.elapsed_time:.4f} seconds")

# Example usage of Timer context manager
if __name__ == "__main__":
    with Timer():
        total = sum(i*i for i in range(1000000))
        print(f"Sum of squares: {total}")