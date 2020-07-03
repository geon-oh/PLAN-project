import sys
import getopt
try :
    opts, args = getopt.getopt(sys.argv[1:], "hi:f:u:",
            ["help=", "id=", "file_path=", "user="])

