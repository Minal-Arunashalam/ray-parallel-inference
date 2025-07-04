import ray
import time

#remote task for inference
@ray.remote
def infer(x):
    """Ray remote task definition. It mimics a time-consuming operation (model inference latency)"""
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
    """Run parallel inference experiment using Ray remote tasks for each input."""
    ray.init(ignore_reinit_error=True)
    start = time.time()
    #lauunch tasks, running as many as possible in parallel, based on number of cores available
    futures = [infer.remote(x) for x in inputs]
    #wait for all tasks to complete and collect results``
    results = ray.get(futures)
    #get duration
    duration = time.time() - start
    print(f"Parallel inference on {len(inputs)} samples took {duration:.2f}s")
    ray.shutdown()
    return results, duration

if __name__ == "__main__":
    inputs = list(range(20))
    serial_inference(inputs)
    parallel_inference(inputs)
