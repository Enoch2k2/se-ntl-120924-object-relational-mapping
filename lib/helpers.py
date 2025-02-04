import os

def clear():
  os.system("clear")

def pause():
  input("Press Enter to Continue...")

def line_space():
  print("")

def invalid_choice():
  clear()
  print("Invalid Choice, Try Again")
  line_space()
  pause()