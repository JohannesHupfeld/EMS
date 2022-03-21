from tkinter import *
from tkinter import ttk
import random
import tkinter.messagebox
import datetime
import time
import tempfile, os

class Employee:

  def __init__(self,root):
    self.root = root
    self.root.title("Employee Management Database")
      