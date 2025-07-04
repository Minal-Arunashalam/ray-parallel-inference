import ray
import time

#remote task for inference
@ray.remote
def infer(x):
    """Mimic a time-consuming operation (model inference latency)"""
    time.sleep(0.1) 
    return x * x

def serial_inference(inputs):
    """Baseline to benchmark Ray parallel inference: run inference sequentially."""
    def infer_local(y):
        time.sleep(0.1)
        return y * y
    #start timer
    start = time.time()
    #run inference sequentially on each input
    results = [infer_local(x) for x in inputs]
    #end timer and calcualte duration
    duration = time.time() - start
    print(f"Serial inference on {len(inputs)} samples took {duration:.2f}s")
    return results, duration

def parallel_inference(inputs):
    """Parallel via Ray remote tasks."""
    ray.init(ignore_reinit_error=True)
    start = time.time()
    futures = [infer.remote(x) for x in inputs]
    results = ray.get(futures)
    duration = time.time() - start
    print(f"Parallel inference on {len(inputs)} samples took {duration:.2f}s")
    ray.shutdown()
    return results, duration

if __name__ == "__main__":
    inputs = list(range(20))
    serial_inference(inputs)
    parallel_inference(inputs)