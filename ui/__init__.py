from contextlib import contextmanager
d = None
d = dir()



class OutputUI(object):
    def __init__(self, parent=None):
        self.parent = parent

    def run(self, f, *args, **kwargs):
        try:
            return f(*args, **kwargs)
        except Warning as e:
            self.show_warning(e)
        except Exception as e:
            self.show_error(e)
            raise

    def show_error(self, msg, title="Error"):
        pass

    def show_message(self, msg, title="Information"):
        pass

    def show_warning(self, msg, title="Warning"):
        pass

    def show_text(self, text, end="\n", flush=False):
        pass

class InputUI(object):
    def get_confirmation(self, title, msg):
        raise NotImplementedError

    def get_string(self, title, msg):
        raise NotImplementedError

    def get_open_filename(self, title="Open", filetype_filter="*.*", file_dir=None, selected_filter=None):
        raise NotImplementedError

    def get_save_filename(self, title, filetype_filter, file_dir=None, selected_filter=None):
        raise NotImplementedError

    def get_open_filenames(self, title, filetype_filter, file_dir=None):
        raise NotImplementedError

    def get_foldername(self, title='Select directory', file_dir=None):
        raise NotImplementedError

class StatusUI(object):
    is_waiting = False
    def __init__(self, parent=None):
        self.waiting = False
        
    @contextmanager
    def wait_cursor(self):
        if self.waiting:
            yield
        else:
            self.waiting = True
            self._start_wait()
            yield
            self._end_wait()
            self.waiting = False
     
    def progress_iterator(self, sequence, text="Working... Please wait", allow_cancel=True):
        return sequence

    def exec_long_task(self, text, allow_cancel, task, *args, **kwargs):
        return task(*args, **kwargs)

    def _start_wait(self):
        self.is_waiting = True

    def _end_wait(self):
        self.is_waiting = False

    def progress_callback(self):
        def callback(n,N):
            pass 
        return callback

class UI(InputUI, OutputUI, StatusUI):
    pass


from .text_ui import *
from .daemon_ui import *

__all__ = [m for m in set(dir()) - set(d)]
