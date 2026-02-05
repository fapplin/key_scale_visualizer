from ._anvil_designer import Form1Template
from anvil import *
import anvil.server

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  @handle("button_c", "click")
  def button_c_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.server.call('pico_fn_c', 18) # Choose any number you like!
    self.label_chosenkey.text = "C"

  @handle("button_db", "click")
  def button_db_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.server.call('pico_fn_db', 18) # Choose any number you like!
    self.label_chosenkey.text = "Db"

  @handle("button_d", "click")
  def button_d_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.server.call('pico_fn_d', 18) # Choose any number you like!
    self.label_chosenkey.text = "D"
    
  @handle("button_eb", "click")
  def button_eb_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.server.call('pico_fn_eb', 18) # Choose any number you like!
    self.label_chosenkey.text = "Eb"
    
  @handle("button_e", "click")
  def button_e_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.server.call('pico_fn_e', 18) # Choose any number you like!
    self.label_chosenkey.text = "E"

  @handle("button_f", "click")
  def button_f_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.server.call('pico_fn_f', 18) # Choose any number you like!
    self.label_chosenkey.text = "F"

  @handle("button_gb", "click")
  def button_gb_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.server.call('pico_fn_gb', 18) # Choose any number you like!
    self.label_chosenkey.text = "Gb"

  @handle("button_g", "click")
  def button_g_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.server.call('pico_fn_g', 18) # Choose any number you like!
    self.label_chosenkey.text = "G"

  @handle("button_ab", "click")
  def button_ab_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.server.call('pico_fn_ab', 18) # Choose any number you like!
    self.label_chosenkey.text = "Ab"

  @handle("button_a", "click")
  def button_a_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.server.call('pico_fn_a', 18) # Choose any number you like!
    self.label_chosenkey.text = "A"

  @handle("button_bb", "click")
  def button_bb_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.server.call('pico_fn_bb', 18) # Choose any number you like!
    self.label_chosenkey.text = "Bb"

  @handle("button_b", "click")
  def button_b_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.server.call('pico_fn_b', 18) # Choose any number you like!
    self.label_chosenkey.text = "B"

  @handle("button_maj", "click")
  def button_maj_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.server.call('pico_fn_maj', 18) # Choose any number you like!
    self.label_chosenscale.text = "Maj"

  @handle("button_min", "click")
  def button_min_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.server.call('pico_fn_min', 18) # Choose any number you like!
    self.label_chosenscale.text = "Min"

  @handle("button_majblu", "click")
  def button_majblu_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.server.call('pico_fn_majblu', 18) # Choose any number you like!
    self.label_chosenscale.text = "MajBlu"

  @handle("button_minblu", "click")
  def button_minblu_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.server.call('pico_fn_minblu', 18) # Choose any number you like!
    self.label_chosenscale.text = "MinBlu"

  @handle("button_majpen", "click")
  def button_majpen_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.server.call('pico_fn_majpen', 18) # Choose any number you like!
    self.label_chosenscale.text = "MajPen"

  @handle("button_minpen", "click")
  def button_minpen_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.server.call('pico_fn_minpen', 18) # Choose any number you like!
    self.label_chosenscale.text = "MinPen"

  @handle("button_majhar", "click")
  def button_majhar_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.server.call('pico_fn_majhar', 18) # Choose any number you like!
    self.label_chosenscale.text = "MajHar"

  @handle("button_minhar", "click")
  def button_minhar_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.server.call('pico_fn_minhar', 18) # Choose any number you like!
    self.label_chosenscale.text = "MinHar"

  @handle("button_dor", "click")
  def button_dor_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.server.call('pico_fn_dor', 18) # Choose any number you like!
    self.label_chosenscale.text = "Dor"

  @handle("button_phr", "click")
  def button_phr_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.server.call('pico_fn_phr', 18) # Choose any number you like!
    self.label_chosenscale.text = "Phr"

  @handle("button_lyd", "click")
  def button_lyd_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.server.call('pico_fn_lyd', 18) # Choose any number you like!
    self.label_chosenscale.text = "Lyd"

  @handle("button_mix", "click")
  def button_mix_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.server.call('pico_fn_mix', 18) # Choose any number you like!
    self.label_chosenscale.text = "Mix"

  @handle("button_aeo", "click")
  def button_aeo_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.server.call('pico_fn_aeo', 18) # Choose any number you like!
    self.label_chosenscale.text = "Aeo"
 
