# Ray Parallel Inference Benchmark

A minimal benchmarking of Python "inference" at scale on local cores with Ray and parallel processing.

- **Serial Tasks**: runs one input at a time  
- **Parallel Tasks**: sends all compute tasks to Ray at once, allowing Ray to run them in parallel on all available CPU cores (e.g. if ran on 8-core CPU, only 8 tasks will can run in parallel at a time)

**Results**  

| Run | Serial Time (s) | Parallel Time (s) | Speedup (×) |
|-----|-----------------|-------------------|-------------|
| 1   |         2.07        |      0.33             |     6.27        |
| 2   |        2.09         |        0.35           |      5.97       |
| 3   |          2.09       |        0.34           |       6.15      |
| 4   |            2.08     |           0.33        |       6.30      |
| 5   |          2.07       |           0.33        |       6.27      |
| **Avg** |      2.08       |        0.34           |       6.19      |
