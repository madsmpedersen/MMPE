
import sys
from mmpe.ui import OutputUI, InputUI, UI, StatusUI
import time
from getpass import getpass



class TextOutputUI(OutputUI):
    last_text = ""
    
    def __init__(self, parent=None):
        OutputUI.__init__(self, parent=parent)
        self.errors = sys.stdout.errors
        self.encoding = sys.stdout.encoding
        sys.stdout = self
        sys.stderr = self
        
        
        
    def show_message(self, msg, title="Information"):
        #self.last_text = msg
        if title != "":
            print ("\n\n%s\n%s\n%s\n" % (title, "-"*len(title), msg))
        else:
            print (msg)

    def show_warning(self, msg, title="Warning"):
        #self.last_text = msg
        print ("%s\n%s\n%s" % (title, "-"*len(title), msg))

    def show_text(self, text, end="\n", flush=False):
        #self.last_text = text
        #print (text, end=end)
        self.write(text+end)
        if flush:
            sys.stdout.flush()
            
    def flush(self):
        sys.__stdout__.flush()
            
    def write(self, txt):
        if txt!="":
            self.last_text = txt
        sys.__stdout__.write(txt)
        
    @property
    def last_text(self):
        try:
            with open(".last_text.txt") as fid:
                return fid.read()
        except:
            return ""
        
    @last_text.setter
    def last_text(self, txt):
        try:
            with open(".last_text.txt",'w') as fid:
                return fid.write(txt)
        except:
            pass
        

class TextInputUI(InputUI):
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
    
    def get_password(self, msg):
        return getpass(msg)



class TextStatusUI(StatusUI, TextOutputUI):
    
    def progress_iterator(self, sequence, text="Working... Please wait", allow_cancel=True, always_refresh=False):
        global pct
        it = iter(list(sequence))
        self.last_text = ""
        if it.__length_hint__() > 0:
            def init():
                global pct
                sys.__stdout__.write("\n\n|0" + " " * 46 + "50%" + " " * 46 + "100%|\n")
                pct = 0
                sys.__stdout__.write("|")

            sys.__stdout__.write(text)
            sys.__stdout__.flush()
            #sys.__stdout__.flush()
            N = it.__length_hint__()
            init()
            for n, v in enumerate(it):
                #if n % 100 == 99:
                #    self.show_text("")
                
                if (self.last_text != "." and n > 0) or (always_refresh and int((n + 1) / N * 100) > pct+1):
                    #print ("#"+self.last_text+"#", int((n + 1) / N * 100), pct)
                    
                #if self.last_text!="":
                    init()
                    self.last_text = "."
                
                while ((n + 1) / N * 100 > pct):
                    sys.__stdout__.write(".")
                    sys.__stdout__.flush()
                    pct += 1
                yield(v)
            self.show_text("|")


    def exec_long_task(self, text, allow_cancel, task, *args, **kwargs):
        print (text)
        return task(*args, **kwargs)

    def _start_wait(self):
        #print ("Working please wait")
        pass

    def _end_wait(self):
        #print ("finish")
        pass


    def progress_callback(self, text="Working... Please wait", always_refresh=False):
        class ProgressCallBack():
            
            def __init__(self, ui, text, always_refresh=False):
                self.ui = ui
                self.text = text
                self.always_refresh = always_refresh
                self.pct = None
            
            def init(self):
                self.ui.show_text("\n\n" + self.text, flush=True)
                self.ui.show_text("|0" + " " * 46 + "50%" + " " * 46 + "100%|")
                self.pct = 0
                self.ui.show_text("|", end="")
                
            def __call__(self, n, N):
                if (self.pct is None) or (self.ui.last_text != "." and n > 0) or (self.always_refresh and ((n + 1) / N * 100 > pct)):
                    self.init()
                while ((n + 1) / N * 100 > self.pct):
                    self.ui.show_text(".", end="", flush=True)
                    self.pct += 1
                if self.pct==100:
                    self.ui.show_text("|")
        return ProgressCallBack(self, text, always_refresh)
                
class TextUI(TextInputUI, TextStatusUI):
    def __init__(self):
        TextStatusUI.__init__(self)
    pass


if __name__ == "__main__":
    pass
        