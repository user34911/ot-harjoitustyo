import time

class Timer:
    """timer to keep track of time since game start"""
    def __init__(self):
        """init timer"""
        self._start_time = None
        self._stop_time = None

    def start(self):
        """start the timer"""
        self._start_time = time.time()

    def stop(self):
        """stop the timer"""
        self._stop_time = time.time()

    def _format_time(self, interval):
        """formats the time into "mm:ss"

        Args:
            interval: time to format

        Returns:
            str: time im "mm:ss"
        """
        minutes, seconds = divmod(interval, 60)
        return f"{int(minutes)}:{int(seconds):02d}"

    def get_time(self):
        """gets the time in desired format

        Returns:
            str: current elapset time or time when stopped
        """
        if not self._start_time:
            return None
        if not self._stop_time:
            return self._format_time(time.time() - self._start_time)
        return self._format_time(self._stop_time - self._start_time)
