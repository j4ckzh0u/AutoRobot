#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
#
# Author            : 乔帮主
# Generate Date     : 2019/01/16
#
################################################################################

import autoit

def main():
    print("Enter main:")

    print("*************** t101:")

    autoit.run("notepad.exe")
    autoit.win_wait_active("[CLASS:Notepad]", 3)
    autoit.control_send("[CLASS:Notepad]", "Edit1", "hello world{!}")
    autoit.win_close("[CLASS:Notepad]")
    autoit.control_click("[Class:#32770]", "Button2")

    print("Level main:")

if __name__ == "__main__":
    main()