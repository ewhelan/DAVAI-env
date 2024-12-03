#!/usr/bin/env python3
# -*- coding:Utf-8 -*-

import argparse

from ..experiment import ThisXP

__all__ = ['main']

def main():
    parser = argparse.ArgumentParser(description="(Re-)Initialize experiment in Ciboulai dashboard server. " +
                                                 "To be executed from the XP directory !")
    args = parser.parse_args()
    this_xp = ThisXP()
    this_xp.ciboulai_init()

