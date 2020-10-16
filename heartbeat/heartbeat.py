#!/usr/bin/env python
#
# Simple App that outputs system information periodically
#
# (c) 2016-2019 Fetal-Neonatal Neuroimaging & Developmental Science Center
#                   Boston Children's Hospital
#
#              http://childrenshospital.org/FNNDSC/
#                        dev@babyMRI.org
#

import psutil
import time
import os
from datetime import datetime
from threading import Timer
# import the Chris app superclass
from chrisapp.base import ChrisApp

Gstr_title = """

 _                     _   _                _   
| |                   | | | |              | |  
| |__   ___  __ _ _ __| |_| |__   ___  __ _| |_ 
| '_ \ / _ \/ _` | '__| __| '_ \ / _ \/ _` | __|
| | | |  __/ (_| | |  | |_| |_) |  __/ (_| | |_ 
|_| |_|\___|\__,_|_|   \__|_.__/ \___|\__,_|\__|                               
                                                                
"""

Gstr_synopsis = """
    NAME

        heartbeat.py

    SYNOPSIS

        heartbeat.py                                                   \\
            [-v <level>] [--verbosity <level]                          \\
            [--version]                                                \\
            [--man]                                                     \\
            [--meta]                                                    \\
            [--infoType <typeSystemInfo>]                               \\ 
            [--beatInterval <secondsWait>]                               \\ 
            [--lifetime <secondsLive>]                                    \\
            /tmp


    BRIEF EXAMPLE

        * To display CPU Usage every 5 seconds for 50 seconds:
            python heartbeat.py --infoType CPU --beatInterval 5 --lifetime 50 /tmp

    DESCRIPTION

        `heartbeat.py` basically displays system information
        every few seconds

    ARGS

        [-v <level>] [--verbosity <level>]
        Verbosity level for app. Not used currently.

        [--version]
        If specified, print version number. 
        [--man]
        If specified, print (this) man page.

        [--meta]
        If specified, print plugin meta data.

        [--infoType <typeSystemInfo>] 
        Type of system information to return.

        [--beatInterval <secondsWait>] 
        Time period to wait between outputting system information.

        [--lifetime <secondsLive>] 
        Time to wait until terminating itself.

"""


class RepeatedTimer(object):
    """
    Periodically executes the input function given the interval
    Source: https://stackoverflow.com/a/13151104/11761743
    """
    def __init__(self, interval, function, *args, **kwargs):
        self._timer = None
        self.function = function
        self.interval = interval
        self.args = args
        self.kwargs = kwargs
        self.is_running = False
        self.start()

    def _run(self):
        self.is_running = False
        self.start()
        self.function(*self.args, **self.kwargs)

    def start(self):
        if not self.is_running:
            self._timer = Timer(self.interval, self._run)
            self._timer.start()
            self.is_running = True

    def stop(self):
        self._timer.cancel()
        self.is_running = False


class HeartBeatApp(ChrisApp):
    """
    Add prefix given by the --prefix option to the name of each input file.
    """
    AUTHORS = 'FNNDSC (dev@babyMRI.org)'
    SELFPATH = os.path.dirname(os.path.abspath(__file__))
    SELFEXEC = os.path.basename(__file__)
    EXECSHELL = 'python3'
    TITLE = 'Periodic Output Generator App'
    CATEGORY = ''
    TYPE = ''
    DESCRIPTION = 'Outputs system information periodically'
    DOCUMENTATION = 'https://github.com/FNNDSC/pl-heartbeat'
    LICENSE = 'Opensource (MIT)'
    VERSION = '1.0.0'
    MAX_NUMBER_OF_WORKERS = 1  # Override with integer value
    MIN_NUMBER_OF_WORKERS = 1  # Override with integer value
    MAX_CPU_LIMIT = ''  # Override with millicore value as string, e.g. '2000m'
    MIN_CPU_LIMIT = ''  # Override with millicore value as string, e.g. '2000m'
    MAX_MEMORY_LIMIT = ''  # Override with string, e.g. '1Gi', '2000Mi'
    MIN_MEMORY_LIMIT = ''  # Override with string, e.g. '1Gi', '2000Mi'
    MIN_GPU_LIMIT = 0  # Override with the minimum number of GPUs, as an integer, for your plugin
    MAX_GPU_LIMIT = 0  # Override with the maximum number of GPUs, as an integer, for your plugin

    # Use this dictionary structure to provide key-value output descriptive information
    # that may be useful for the next downstream plugin. For example:
    #
    # {
    #   "finalOutputFile":  "final/file.out",
    #   "viewer":           "genericTextViewer",
    # }
    #
    # The above dictionary is saved when plugin is called with a ``--saveoutputmeta``
    # flag. Note also that all file paths are relative to the system specified
    # output directory.
    OUTPUT_META_DICT = {}

    def define_parameters(self):
        """
        Define the CLI arguments accepted by this plugin app.
        Use self.add_argument to specify a new app argument.
        """
        self.add_argument('--infoType',
                          dest='infoType',
                          type=str,
                          optional=True,
                          help='return this information',
                          default='datetime')

        self.add_argument('--beatInterval',
                          dest='beatInterval',
                          type=int,
                          optional=True,
                          help='wait before outputting information',
                          default=5)

        self.add_argument('--lifetime',
                          dest='lifetime',
                          type=int,
                          optional=True,
                          help='wait before terminating itself',
                          default=10)

    def run(self, options):
        """
        Define the code to be run by this plugin app.
        """
        print(Gstr_title)
        print('Version: %s\n' % self.get_version())

        pl_method = getattr(self, f"print{options.infoType.upper()}Information")
        repeatExecution = RepeatedTimer(options.beatInterval, pl_method)
        try:
            time.sleep(options.lifetime)
        finally:
            repeatExecution.stop()

    @staticmethod
    def printCPUInformation():
        print(f"Total CPU Usage: {psutil.cpu_percent()}%")

    @staticmethod
    def printDATETIMEInformation():
        print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]}")

    @staticmethod
    def printMEMORYInformation():
        print(f"Total Memory Usage: {psutil.virtual_memory().percent}%")

    def show_man_page(self):
        """
        Print the app's man page.
        """
        print(Gstr_synopsis)


# ENTRYPOINT
if __name__ == "__main__":
    app = HeartBeatApp()
    app.launch()
