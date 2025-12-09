import time

class Timer:
    def __init__(self):
        self._start_time = None
        self._stop_time = None
    
    def start(self):
        self._start_time = time.time()

    def stop(self):
        self._stop_time = time.time()

    def _format_time(self, time):
        minutes, seconds = divmod(time, 60)
        return f"{int(minutes)}:{int(seconds):02d}"

    def __str__(self):
        if not self._start_time:
            return None
        if not self._stop_time:
            return self._format_time(time.time() - self._start_time)
        return self._format_time(self._stop_time - self._start_time)
