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
from subprocess import call

def signal_handler(signal, frame):
    print('You pressed Ctrl+c!')
    exit(0)


def main(arguments):
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('-g', '--gitList', default="gitList.csv", help="specify the gitList file")
    parser.add_argument('-p', '--path', default="/opt/", help="installation path (default is /opt)")
    group = parser.add_mutually_exclusive_group(required=False)
    #parser.add_argument('-d', '--download', help="download only, no installation", action="store_true")
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
            #updateGits(args.gitList, path)
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
                sys.stdout.write("  - Updating " + name + "...")
                sys.stdout.flush()
                try:
                    repo = git.Repo(path + name)
                    o = repo.git.submodule('update', '--init')
                    print(o)
                except:
                    print("Failed")

# Get git repos from CSV file and download them in the given path
def getGits(listFile, path):
    print("Starting downloading git repos")
    with open(listFile) as rawcsv:
        csvfile = csv.DictReader(rawcsv, delimiter=',', quotechar='"')
        rawcsv.seek(0)
        for row in csvfile:
            url = row['url']
            name = row['name']
            sys.stdout.write("  - Getting " + name + "...")
            sys.stdout.flush()
            try:
                repo = git.Repo.init(path + name)
                origin = repo.create_remote('origin', url.rstrip('\n'))
                origin.fetch()
                origin.pull(origin.refs[0].remote_head)
            except git.exc.CacheError:
                sys.stdout.write(colorama.Fore.RED + " Failed!\n")
                sys.stdout.flush()
                logging.debug("CacheError")
            except git.exc.CheckoutError:
                sys.stdout.write(colorama.Fore.RED + " Failed!\n")
                sys.stdout.flush()
                logging.debug("CheckoutError")
            except git.exc.GitCommandError:
                sys.stdout.write(colorama.Fore.RED + " Failed!\n")
                sys.stdout.flush()
                logging.debug("GitCommandError")
            except git.exc.GitCommandNotFound:
                sys.stdout.write(colorama.Fore.RED + " Failed!\n")
                sys.stdout.flush()
                logging.debug("GitCommandNotFound")
            except git.exc.HookExecutionError:
                sys.stdout.write(colorama.Fore.RED + " Failed!\n")
                sys.stdout.flush()
                logging.debug("HookExecutionError")
            except git.exc.InvalidGitRepositoryError:
                sys.stdout.write(colorama.Fore.RED + " Failed!\n")
                sys.stdout.flush()
                logging.debug("InvalidGitRepositoryError")
            except git.exc.NoSuchPathError:
                sys.stdout.write(colorama.Fore.RED + " Failed!\n")
                sys.stdout.flush()
                logging.debug("NoSuchPathError")
            except git.exc.RepositoryDirtyError:
                sys.stdout.write(colorama.Fore.RED + " Failed!\n")
                sys.stdout.flush()
                logging.debug("RepositoryDirtyError")
            except git.exc.UnmergedEntriesError:
                sys.stdout.write(colorama.Fore.RED + " Failed!\n")
                sys.stdout.flush()
                logging.debug("UnmergedEntriesError")
            except git.exc.WorkTreeRepositoryUnsupported:
                sys.stdout.write(colorama.Fore.RED + " Failed!\n")
                sys.stdout.flush()
                logging.debug("WorkTreeRepositoryUnsupported")
            except:
                sys.stdout.write(colorama.Fore.RED + " Failed!\n")
                sys.stdout.flush()
                logging.debug("Unknowned error...")
            else:
                sys.stdout.write(colorama.Fore.GREEN + " Done!\n")
                sys.stdout.flush()

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
                sys.stdout.write("  - Configuring " + name + "...")
                sys.stdout.flush()
                os.chdir(path + name)
                print(os.getcwd())
                try:
                    print(name + ": " + setup)
                    os.system(setup)
                except:
                    sys.stdout.write(colorama.Fore.RED + " Failed!\n")
                    sys.stdout.flush()
                else:
                    sys.stdout.write(colorama.Fore.GREEN + " Done!\n")
                    sys.stdout.flush()

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
