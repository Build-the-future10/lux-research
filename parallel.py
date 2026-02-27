from multiprocessing import Pool

class ParallelExecutor:
    def run(self, func, iterable, processes=4):
        with Pool(processes) as pool:
            return pool.map(func, iterable)
