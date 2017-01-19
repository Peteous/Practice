# Practice

## Description
 - This repository contains practice code written by me, some for practical purposes, amd some for fun. I make no guarantees about current working operation, since I'm digging a lot of this old code up. The older stuff is generally also not written well (bad variable/object names) because I was young. Now I don't wish to fix it.

## Table of Contents
1. NotGalaga.java
  - I have no idea how much this program actually works. This was the last major java application I worked on (in high school) and I'm actually surprised I saved it at all. It's a GUI Java applet. I don't know if this was the final code or just part of it. A known bug was that the game ran differently depending on the processing power of the machine, due to the way we implemented time delays. I worked on this project with a collaborator. I am working with him to see if we cannot dig up the final code.

2. Dice Roller.py
 - This is a program that takes you inout of dice to roll, in d20 style formatting, and turns that into a simulated dice roll value. This takes place in the console. Code is written in Python. This is my second ever Python project, and my first public Python commit.

3. Intro to Java Certificate.pdf
 - This file is generated upon the completion of the "Learn Java" app for iOS course on the syntax of Java. It is not my only Java training, but it is technically my most recent. The Java course from this company is not as extensive as the Python course from the same company.

4. iOS Slack Code Parser.py
 - This script is meant to run in Pythonista for iOS. I wrote this script because the 2FA codes that Slack generates when you turn on 2FA copy as one long conglomerated string on iOS. This script parses through the string in the clipboard and inserts spaces every 9 characters, where the Slack codes are naturally split. Then is saves the output to the clipboard so it can be pasted into a password manager cleanly.

5. Undo iOS Slack Code Parser.py
 - This script was written purely for testing purposes. It is the inverse operation of "iOS Slack Code Parser.py", so that I could do debugging with one string, without having to go back to the source string. This script does not need to be kept around. The script searches for spaces in a string, removes them, and then outputs the string to the clipboard. 