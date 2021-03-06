'''
Created on 10/03/2014

@author: MMPE
'''

import os

DEBUG = False
def pexec(args, cwd=None):
    """
    usage: errorcode, stdout, stderr, cmd = pexec("MyProgram.exe arg1, arg2", r"c:\tmp\")

    """
    import subprocess
    if not isinstance(args, (list, tuple)):
        args = [args]
    args = [str(arg) for arg in args]
    for i in range(len(args)):
        if os.path.exists(args[i]):
            args[i] = str(args[i]).replace('/', os.path.sep).replace('\\', os.path.sep).replace('"', '')

    cmd = "%s" % '{} /c "{}"'.format (os.environ.get("COMSPEC", "cmd.exe"), subprocess.list2cmdline(args))
    if cwd and os.path.isfile(cwd):
        cwd = os.path.dirname(cwd)
    proc = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, cwd=cwd)
    stdout, stderr = proc.communicate()
    errorcode = proc.returncode

    return errorcode, stdout.decode(), stderr.decode(), cmd
