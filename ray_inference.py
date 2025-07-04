import ray
import time

#remote task for inference
@ray.remote
def infer(x):
    """Simulated inference: sleeps then returns x*x."""
    time.sleep(0.1) #mimic a time-consuming operation (model inference latency)
    return x * x