# Practice

## Description
 - This repository contains practice code written by me, some for practical purposes, amd some for fun. I make no guarantees about current working operation, since I'm digging a lot of this old code up. The older stuff is generally also not written well (bad variable/object names) because I was young. Now I don't wish to fix it.

## Table of Contents
1. NotGalaga.java
  - I have no idea how much this program actually works. This was the last major java application I worked on (in high school) and I'm actually surprised I saved it at all. It's a GUI Java applet. I don't know if this was the final code or just part of it. A known bug was that the game ran differently depending on the processing power of the machine, due to the way we implemented time delays. I worked on this project with a collaborator. I am working with him to see if we cannot dig up the final code.

2. Dice Roller.py
 - This is a program that takes you inout of dice to roll, in d20 style formatting, and turns that into a simulated dice roll value. This takes place in the console. Code is written in Python. This is my second ever Python project, and my first public Python commit.

3. Intro to Java Certificate.pdf
 - This file is generated upon the completion of the "Learn Java Pro" app for iOS course on the syntax of Java. It is not my only Java training, but it is technically my most recent. The Java course from this company is not as extensive as the Python course from the same company.

4. iOS Slack Code Parser.py
 - This script is meant to run in Pythonista for iOS. I wrote this script because the 2FA codes that Slack generates when you turn on 2FA copy as one long conglomerated string on iOS. This script parses through the string in the clipboard and inserts spaces every 9 characters, where the Slack codes are naturally split. Then is saves the output to the clipboard so it can be pasted into a password manager cleanly.

5. Undo iOS Slack Code Parser.py
 - This script was written purely for testing purposes. It is the inverse operation of "iOS Slack Code Parser.py", so that I could do debugging with one string, without having to go back to the source string. This script does not need to be kept around. The script searches for spaces in a string, removes them, and then outputs the string to the clipboard.

6. Add To Instapaper.py
 - This script was written in Pythonista for iOS. It is, as such, hampered and enabled by the libraries in Pythonista. It is designed to run within the share sheet, but can also be used from the app as long as you have a URL copied. It uses Instapaper's simple API to upload a url of your choice to Instapaper as a bookmark.
 - This script was written mostly for fun to see I could copy the functionality of a Workflow workflow that I had made. I am relatively happy with the results.
 - You will need to enter your own details for username and password, which I did not provide for security reasons.

7. Encode.py
 - This file contains a method for encoding inputs into a url format. The method can take in just a string for encoding, a string and a string for an url for an API, and parameters for url encoding. This method could be used in a script like Add To Instapaper.py instead of writing all the steps out. Eventually, I will add other encoding methods to this file, for encoding systems like base64 encoding for example. This document also contains an internal method, which is not meant for use outside of this document. This method is urlCharShift, which contains the actual character changes in url encoding.

8. urlEncode.java
 - This file is a java class which mimicks the functionality of Encode.py, but in Java. The code was written and compiled in the BlueJay IDE on the Raspberry Pi Zero.

9. shareQuoteWLink.py
 - This script mimics the functionality of a Workflow workflow that I made. It takes a copied quote and a url input to the share sheet, combines them together in markdown format, and output that text to popular writing apps.

10. EmailParser.py
 - This file defines methods for checking input for containing an email formatted string, and extracting an email formatted string from a string. These methods use regular expressions.

11. Python Tutorial Completion Certificate.pdf
 - This file is generated upon the completion of the "Learn Python Pro" app for iOS course on the syntax and ideology of Python. It is not my only formal Python training.

 12. MD2HTML.py
 - I fully recognize that I am reinventing the wheel with this script. However, this script will take in text written/formatted in Markdown and transform it into HTML text. It works via the clipboard function from Pythonista for iOS, but it can also take in text entered via the Python terminal if there is nothing in the clipboard. If not running in Pythonista, you will need to remove all of the clipboard functionality in order to avoid compile errors.

## Feedback Request
 - I am self-taught on Python, and largely self-taught in programming. If you have suggestions for file name changes, class name changes, method name changes, syntax suggestions, or other programming tips, *please* fill out an issue in GutHub in this repo and I will make changes. I want to be better at coding, and your help is always appreciated.
 - If you find bugs, please leave an issue ticket in this repo and be as specific as possible. I want to debug my code.
