#!/usr/bin/env python
# encoding: utf-8
# TITLE: smk - simple bookmarkmanager 
# AUTHOR: 0x17 
# WEBSITE: https://www.nerdbude.com 

# TODO:
# [X] add a bookmark to list
# [X] bookmarkcounter (only count level 1 entries) 
# [ ] input for open
# [ ] global config path  
# [ ] tags
# [ ] search (name / tag)
# [ ] check if entry already exist 
#---------------------
# [ ] default webbrowser in config 
# [ ] default bookmarklist path in config 
# [ ] colors in config 

import os
import subprocess
import sys
import yaml
import webbrowser
import csv

bookmarkfile = "/home/pho/.config/SMK/marks.csv"
marks_num   = sum(1 for _ in open(bookmarkfile))
marks_total = str(marks_num - 1)

class bcolors:
    OK      = '\033[92m'
    FAIL    = '\033[91m'
    RESET   = '\u001b[0m'
    DEFAULT = '\033[35m'
    CHECK   = '\033[33m'
    PINK    = '\033[95m'

def main():
    os.system('clear')
    print(bcolors.PINK + '<< SMK >>' + bcolors.RESET)
    print(':: ' + bcolors.OK + marks_total + bcolors.RESET + ' Bookmarks')

    while True: 
        # Main Input
        command = input(bcolors.CHECK + ">>> " + bcolors.RESET)
        
        # add bookmark
        # [OPEN] create id
        if command == "add":
            url     = input('url: ')
            title   = input('title: ')
            desc    = input('desc: ')
#           tags    = input('tags: ')

            mark_line = '"' + title + '","' + url + '","' + desc + '"\n'  

            marks_file = open(bookmarkfile, 'a')
            marks_file.write(mark_line)
            marks_file.close()
            print('[' + bcolors.OK + '+' + bcolors.RESET + '] ' + title + ' added' )

        # delete bookmark
        # [OPEN] delete entries by name
        if command == "del":
          


        # show bookmarks
        # [DONE]
        # CSV
        if command == "show":
            with open('/home/pho/.config/SMK/marks.csv', newline='') as marksfile:
                reader = csv.DictReader(marksfile)
                for row in reader:
                    print(bcolors.PINK + '  ' + row['TITLE'] + bcolors.RESET + '\n' + bcolors.CHECK + '   ' + row['LINK'] + bcolors.RESET + '\n' + '   ' + row['DESC'] + '\n')

        # open bookmark in browser 
        # [DONE]
        if command == "open":
            open_link = input('Name: ')
            marks_file = csv.reader(open('/home/pho/.config/SMK/marks.csv', "r"), delimiter=",")
            for row in marks_file:
                if open_link == row[0]:
                    mark_target = row[1]
                    webbrowser.open(mark_target)
       
        # exit 
        # [DONE]
        if command == "exit":
            # CLOSE THE SCRIPT
            os.system('clear')
            break

main()

