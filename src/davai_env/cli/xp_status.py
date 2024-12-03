#!/usr/bin/env python3
# -*- coding:Utf-8 -*-
"""
Check the status of tests in a Davai experiment.
"""

import argparse

from ..experiment import ThisXP


def main():
    args = get_args()
    this_xp = ThisXP()
    this_xp.status(args.task)


def get_args():
    parser = argparse.ArgumentParser(description=' '.join(['Check status of current experiment.',
                                                           'Must be called from the XP directory.',
                                                           'Works with tasks summaries in cache,',
                                                           'hence files may be missing if used too long after',
                                                           'the experiment has been run.']))
    parser.add_argument('-t', '--task',
                        default=None,
                        help="Specify a task name to get the filepath to its detailed summary.")
    return parser.parse_args()

