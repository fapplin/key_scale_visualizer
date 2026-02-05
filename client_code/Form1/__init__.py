from ._anvil_designer import Form1Template
from anvil import *
import anvil.server

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  @handle("button_1", "click")
  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.server.call('pico_fn_c', 18) # Choose any number you like!

  @handle("button_2", "click")
  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.server.call('pico_fn_db', 18) # Choose any number you like!

  @handle("button_3", "click")
  def button_3_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.server.call('pico_fn_d', 18) # Choose any number you like!

  @handle("button_4", "click")
  def button_4_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.server.call('pico_fn_eb', 18) # Choose any number you like!

  @handle("button_5", "click")
  def button_5_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.server.call('pico_fn_e', 18) # Choose any number you like!

 
