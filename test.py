from time import perf_counter
import numpy as np
import cubes

results = [0, 1, 2, 8, 29, 166, 1023, 6922]


all_cubes = [np.ones((1, 1, 1), dtype=np.byte)]
for i in range(1, 8):
    t1_start = perf_counter()
    all_cubes = cubes.compute_next_depth(all_cubes)
    t1_stop = perf_counter()

    print(f"Depth {i+1}: {len(all_cubes):>6} cubes found in {(t1_stop - t1_start):0.3f}s")

    assert len(all_cubes) == results[i]