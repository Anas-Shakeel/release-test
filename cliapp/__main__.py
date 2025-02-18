""" Entry point of the project (to run directly, without installing) """

import os
import sys


if __package__ == "":
    path = os.path.dirname(os.path.dirname(__file__))
    sys.path.insert(0, path)

from cliapp import cli

if __name__ == "__main__":
    cli.main()
