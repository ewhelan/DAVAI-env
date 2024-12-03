#!/usr/bin/env python3
# -*- coding:Utf-8 -*-

import argparse

from ..experiment import ThisXP

__all__ = ['main']


def main():
    parser = argparse.ArgumentParser(description='Prints the version of tests currently in use in this experiment.')
    parser.parse_args()
    this_xp = ThisXP()
    print(this_xp.davai_tests_version)

