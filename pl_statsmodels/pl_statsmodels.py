#
# statsmodels ds ChRIS plugin app
#
# (c) 2022 Fetal-Neonatal Neuroimaging & Developmental Science Center
#                   Boston Children's Hospital
#
#              http://childrenshospital.org/FNNDSC/
#                        dev@babyMRI.org
#

from chrisapp.base import ChrisApp
import statsmodels.api as sm
import pandas as pd
from patsy import dmatrices
from os import listdir

Gstr_title = r"""
                                        
    | |      | |                         | |    | |    
 ___| |_ __ _| |_ ___ _ __ ___   ___   __| | ___| |___ 
/ __| __/ _` | __/ __| '_ ` _ \ / _ \ / _` |/ _ \ / __|
\__ \ || (_| | |_\__ \ | | | | | (_) | (_| |  __/ \__ \
|___/\__\__,_|\__|___/_| |_| |_|\___/ \__,_|\___|_|___/
                                                       
"""

Gstr_synopsis = """
(Edit this in-line help for app specifics. At a minimum, the
flags below are supported -- in the case of DS apps, both
positional arguments <inputDir> and <outputDir>; for FS and TS apps
only <outputDir> -- and similarly for <in> <out> directories
where necessary.)

    NAME
       pl_statsmodels
    SYNOPSIS
        docker run --rm fnndsc/pl-statsmodels pl_statsmodels               \\
            [-h] [--help]                                               \\
            [--json]                                                    \\
            [--man]                                                     \\
            [--meta]                                                    \\
            [--savejson <DIR>]                                          \\
            [-v <level>] [--verbosity <level>]                          \\
            [--version]                                                 \\
            <inputDir>                                                  \\
            <outputDir>
    BRIEF EXAMPLE
        * Bare bones execution
            docker run --rm -u $(id -u)                             \
                -v $(pwd)/in:/incoming -v $(pwd)/out:/outgoing      \
                fnndsc/pl-statsmodels pl_statsmodels                   \
                /incoming /outgoing
    DESCRIPTION
        `pl_statsmodels` ...
    ARGS
        [-h] [--help]
        If specified, show help message and exit.
        [--json]
        If specified, show json representation of app and exit.
        [--man]
        If specified, print (this) man page and exit.
        [--meta]
        If specified, print plugin meta data and exit.
        [--savejson <DIR>]
        If specified, save json representation file to DIR and exit.
        [-v <level>] [--verbosity <level>]
        Verbosity level for app. Not used currently.
        [--version]
        If specified, print version number and exit.
"""


class StatsmodelsOLS(ChrisApp):
    """
    An application that can fit an OLS model on the input (specified columns) and save output and results in output directory
    """
    PACKAGE                 = __package__
    TITLE                   = 'A ChRIS statsmodels plugin app'
    CATEGORY                = 'Utility'
    TYPE                    = 'ds'
    ICON                    = ''   # url of an icon image
    MIN_NUMBER_OF_WORKERS   = 1    # Override with the minimum number of workers as int
    MAX_NUMBER_OF_WORKERS   = 1    # Override with the maximum number of workers as int
    MIN_CPU_LIMIT           = 2000 # Override with millicore value as int (1000 millicores == 1 CPU core)
    MIN_MEMORY_LIMIT        = 8000  # Override with memory MegaByte (MB) limit as int
    MIN_GPU_LIMIT           = 0    # Override with the minimum number of GPUs as int
    MAX_GPU_LIMIT           = 0    # Override with the maximum number of GPUs as int

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
        print("defining")
        help_str = "columns to fit OLS on"
        self.add_argument("--columns", dest='columns', default='[]', action='store', type=str, help=help_str, optional=False)

    def run(self, options):
        """
        Define the code to be run by this plugin app.
        """
        def get_dmatrix(inputfile, column):
            y, X = dmatrices(column, data=inputfile, return_type='dataframe')
            return y, X

        def find_csv_filenames( path_to_dir, suffix=".csv" ):
            filenames = listdir(path_to_dir)
            return [ filename for filename in filenames if filename.endswith( suffix ) ]

        print(Gstr_title)
        print('Version: %s' % self.get_version())
        inputdir = options.inputdir
        outputdir = options.outputdir
        columns = options.columns
        print("Fitting OLS on '%s' and saving output to '%s'" % (inputdir, outputdir))
        
        input_df = pd.read_csv("{}/{}".format(inputdir, find_csv_filenames(inputdir)[0]))
        input_df = input_df.dropna()
        y, X = get_dmatrix(input_df, columns)

        mod = sm.OLS(y, X)
        res = mod.fit()

        res_summary = res.summary()
        with open("{}/result_summary.txt".format(outputdir), "w") as f:
            f.write(str(res_summary))

    def show_man_page(self):
        """
        Print the app's man page.
        """
        print(Gstr_synopsis)