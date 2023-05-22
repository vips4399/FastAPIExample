import multiprocessing

bind = "0.0.0.0:80"

workers = multiprocessing.cpu_count() + 1
worker_class = "uvicorn.workers.UvicornWorker"

loglevel = "debug"
accesslog = "./access_log"
errorlog = "./error_log"