#!/bin/env python

import sys
import calc


def main():

  val1 = sys.argv[1]
  val2 = sys.argv[2]
  val1 = float(val1)
  val2 = float(val2)

  print calc.calc_wari(val1,val2)

if __name__ == "__main__":
    main()
