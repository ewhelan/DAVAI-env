#!/usr/bin/env python3
# -*- coding:Utf-8 -*-

import argparse

from ..experiment import ThisXP

__all__ = ['main']


def main():
    args = get_args()
    this_xp = ThisXP()
    this_xp.build(
                  skip_fetching_sources=args.skip_fetching_sources,
                  drymode=args.drymode,
                  # gmkpack arguments
                  preexisting_pack=args.preexisting_pack,
                  cleanpack=args.cleanpack,
                  )


def get_args():
    parser = argparse.ArgumentParser(description='Fetch sources (interactively) and build executables (batch/scheduler). To be executed from the XP directory !')
    parser.add_argument('-s', '--skip_fetching_sources',
                        action='store_true',
                        help="Skip fetching the sources (assuming they have been fetched / and pack preexists for gmkpack).")
    parser.add_argument('-e', '--preexisting_pack',
                        action='store_true',
                        help="Gmkpack: assume the pack already preexists, and repopulate it with sources changes.")
    parser.add_argument('-c', '--cleanpack',
                        action='store_true',
                        help="Gmkpack: clean pack before git2pack+pack2bin.")
    parser.add_argument('--drymode',
                        action='store_true',
                        help="Dry mode: print commands to be executed, but do not run them")
    return parser.parse_args()

