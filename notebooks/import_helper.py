import os
import sys
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir) 

import calculations.fitting as fitting
import calculations.helpers as helpers
import calculations.matrices as matrices
import calculations.workflow as workflow
