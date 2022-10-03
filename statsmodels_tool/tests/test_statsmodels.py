
from unittest import TestCase
from unittest import mock
from statsmodels_tool.statsmodels_tool import StatsmodelsOLS
import os

class StatsmodelsOLSTests(TestCase):
    """
    Test StatsmodelsOLS.
    """
    def setUp(self):
        self.app = StatsmodelsOLS()

    def test_run(self):
        """
        Test the run code.
        """

        inputdir = 'test_input'
        outputdir = 'test_output'
        expected = "test_expected_output"
        args = []
        if self.app.TYPE == 'ds':
            args.append('test_input')
        args.append('test_output')

        # you may want to add more of your custom defined optional arguments to test
        # your app with
        # eg.
        # args.append('--custom-int')
        # args.append(10)

        args.append('--columns')
        args.append('Lottery ~ Literacy + Wealth + Region')

        options = self.app.parse_args(args)
        self.app.run(options)

        self.maxDiff=None
        # same number of files in input and output
        self.assertEqual(len(os.listdir(inputdir)), len(os.listdir(outputdir)))

        # only txt files in output
        for f in os.listdir(outputdir):
            self.assertTrue(f.endswith(".txt"))

        with open(os.path.join(outputdir, "result_summary.txt"), "r") as f:
            output = "".join(f.readlines())

        with open(os.path.join(expected, "result_summary.txt"), "r") as f:
            expected = "".join(f.readlines())

        self.assertEqual(output.strip(), expected.strip())
