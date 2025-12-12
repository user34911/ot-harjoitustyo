import time

class Timer:
    def __init__(self):
        self._start_time = None
        self._stop_time = None

    def start(self):
        self._start_time = time.time()

    def stop(self):
        self._stop_time = time.time()

    def _format_time(self, current_seconds):
        minutes, seconds = divmod(current_seconds, 60)
        return f"{int(minutes)}:{int(seconds):02d}"

    def get_time(self):
        if not self._start_time:
            return None
        if not self._stop_time:
            return self._format_time(time.time() - self._start_time)
        return self._format_time(self._stop_time - self._start_time)
