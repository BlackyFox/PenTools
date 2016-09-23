#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
This script aim is to retreive and install some usefull pentest tools
Author: BlackyFox
https://github.com/BlackyFox
"""

import os
import argparse
import sys
import string
import logging
import git
import csv
import signal
import colorama
import subprocess

class Progress(git.remote.RemoteProgress):
    def line_dropped(self, line):
        print "\033[K", line, "\r",
    def update(self, *args):
        print "\033[K", self._cur_line, "\r",

def signal_handler(signal, frame):
    print('You pressed Ctrl+c!')
    exit(0)


def main(arguments):
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('-g', '--gitList', default="gitList.csv", help="specify the gitList file")
    parser.add_argument('-p', '--path', default="/opt/", help="installation path (default is /opt)")
    group = parser.add_mutually_exclusive_group(required=False)
    group.add_argument('-d', '--download', help="download only, no installation", action="store_true")
    parser.add_argument('-v', '--verbose', help="increase output verbosity", action="store_true")
    group.add_argument('-u', '--update', help="update git repositories", action="store_true")
    parser.add_argument('-c', '--configure', help="auto configure the tools", action="store_true")
    args = parser.parse_args(arguments)

    signal.signal(signal.SIGINT, signal_handler)
    colorama.init(autoreset=True)

    if args.verbose:
        logging.basicConfig(level=logging.DEBUG)
        logging.debug("Debug mode activated")

    if not os.path.isdir(args.path):
        print("Installation path " + args.path + " not found.\nQuitting...")
        exit(1)
    else:
        logging.debug("Path " + args.path + " exists.")
        if args.path.endswith("/"):
            path = args.path
        else:
            path = args.path + "/"

    if not os.path.exists(args.gitList):
        print("Git list file (" + args.gitList + ") not found. Skipping git tools.")
    else:
        if args.update:
            updateGits(args.gitList, path)
            print("Update function will come soon....")
        else:
            getGits(args.gitList, path)

    if args.configure:
        configure(args.gitList, path)


# Update repo list from CSV
def updateGits(listFile, path):
    print("Starting updating git repositories")
    with open(listFile) as rawcsv:
        csvfile = csv.DictReader(rawcsv, delimiter=',', quotechar='"')
        rawcsv.seek(0)
        for row in csvfile:
            url = row['url']
            name = row['name']
            if os.path.isdir(path + name):
                print("  - Updating " + name + "...")
                try:
                    repo = git.Repo(path + name)
                    g = repo.remotes.origin
                    g.pull(progress=Progress())
                    print "\033[K", colorama.Fore.GREEN + "        Done!"
                except:
                    print "\033[K", colorama.Fore.RED + "        Failed!"

# Get git repos from CSV file and download them in the given path
def getGits(listFile, path):
    print("Starting downloading git repos")
    with open(listFile) as rawcsv:
        csvfile = csv.DictReader(rawcsv, delimiter=',', quotechar='"')
        rawcsv.seek(0)
        for row in csvfile:
            url = row['url']
            name = row['name']
            print("  - Getting " + name + "...")
            if os.path.exists(path + name):
                sys.stdout.write(colorama.Fore.YELLOW + "        Already exist! Try updating.\n")
                sys.stdout.flush()
            else:
                try:
                    git.Repo.clone_from(url.rstrip('\n'), path + name, progress=Progress())
                except:
                    print "\033[K", colorama.Fore.RED + "        Failed!"
                else:
                    print "\033[K", colorama.Fore.GREEN + "        Done!"

# Auto-configure some tools
def configure(listFile, path):
    print("Starting configuring tools")
    with open(listFile) as rawfile:
        csvfile = csv.DictReader(rawfile, delimiter=',', quotechar='"')
        rawfile.seek(0)
        for row in csvfile:
            name = row['name']
            setup = row['setup']
            if "NA" in setup or not setup or "TODO" in setup:
                print("  - Nothing to do for " + name)
            else:
                print("  - Configuring " + name + "...")
                os.chdir(path + name)
                print(os.getcwd())
                try:
                    out = subprocess.call(setup, shell=True)
                except:
                    sys.stdout.write(colorama.Fore.RED + " Failed!\n")
                    sys.stdout.flush()
                else:
                    sys.stdout.write(colorama.Fore.GREEN + " Done!\n")
                    sys.stdout.flush()

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
