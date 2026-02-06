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
    anvil.server.call('pico_fn_keys', 0) # Choose any number you like!
    self.label_chosenkey.text = "C"

  @handle("button_db", "click")
  def button_db_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.server.call('pico_fn_keys', 1) # Choose any number you like!
    self.label_chosenkey.text = "Db"

  @handle("button_d", "click")
  def button_d_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.server.call('pico_fn_keys', 2) # Choose any number you like!
    self.label_chosenkey.text = "D"
    
  @handle("button_eb", "click")
  def button_eb_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.server.call('pico_fn_keys', 3) # Choose any number you like!
    self.label_chosenkey.text = "Eb"
    
  @handle("button_e", "click")
  def button_e_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.server.call('pico_fn_keys', 4) # Choose any number you like!
    self.label_chosenkey.text = "E"

  @handle("button_f", "click")
  def button_f_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.server.call('pico_fn_keys', 5) # Choose any number you like!
    self.label_chosenkey.text = "F"

  @handle("button_gb", "click")
  def button_gb_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.server.call('pico_fn_keys', 6) # Choose any number you like!
    self.label_chosenkey.text = "Gb"

  @handle("button_g", "click")
  def button_g_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.server.call('pico_fn_keys', 7) # Choose any number you like!
    self.label_chosenkey.text = "G"

  @handle("button_ab", "click")
  def button_ab_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.server.call('pico_fn_keys', 8) # Choose any number you like!
    self.label_chosenkey.text = "Ab"

  @handle("button_a", "click")
  def button_a_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.server.call('pico_fn_keys', 9) # Choose any number you like!
    self.label_chosenkey.text = "A"

  @handle("button_bb", "click")
  def button_bb_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.server.call('pico_fn_keys', 10) # Choose any number you like!
    self.label_chosenkey.text = "Bb"

  @handle("button_b", "click")
  def button_b_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.server.call('pico_fn_keys', 11) # Choose any number you like!
    self.label_chosenkey.text = "B"

  @handle("button_maj", "click")
  def button_maj_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.server.call('pico_fn_scales', self.button_maj.text) # Choose any number you like!
    self.label_chosenscale.text = self.button_maj.text

  @handle("button_min", "click")
  def button_min_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.server.call('pico_fn_scales', self.button_min.text) # Choose any number you like!
    self.label_chosenscale.text = self.button_min.text

  @handle("button_majblu", "click")
  def button_majblu_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.server.call('pico_fn_scales', self.button_majblu.text) # Choose any number you like!
    self.label_chosenscale.text = self.button_majblu.text

  @handle("button_minblu", "click")
  def button_minblu_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.server.call('pico_fn_scales', self.button_minblu.text) # Choose any number you like!
    self.label_chosenscale.text = self.button_minblu.text

  @handle("button_majpen", "click")
  def button_majpen_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.server.call('pico_fn_scales', self.button_majpen.text) # Choose any number you like!
    self.label_chosenscale.text = self.button_majpen.text

  @handle("button_minpen", "click")
  def button_minpen_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.server.call('pico_fn_scales', self.button_minpen.text) # Choose any number you like!
    self.label_chosenscale.text = self.button_minpen.text

  @handle("button_majhar", "click")
  def button_majhar_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.server.call('pico_fn_scales', self.button_majhar.text) # Choose any number you like!
    self.label_chosenscale.text = self.button_majhar.text

  @handle("button_minhar", "click")
  def button_minhar_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.server.call('pico_fn_scales', self.button_minhar.text) # Choose any number you like!
    self.label_chosenscale.text =  self.button_minhar.text

  @handle("button_dor", "click")
  def button_dor_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.server.call('pico_fn_scales', self.button_dor.text) # Choose any number you like!
    self.label_chosenscale.text = self.button_dor.text

  @handle("button_phr", "click")
  def button_phr_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.server.call('pico_fn_scales', self.button_phr.text) # Choose any number you like!
    self.label_chosenscale.text = self.button_phr.text

  @handle("button_lyd", "click")
  def button_lyd_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.server.call('pico_fn_scales', self.button_lyd.text) # Choose any number you like!
    self.label_chosenscale.text = self.button_lyd.text

  @handle("button_mix", "click")
  def button_mix_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.server.call('pico_fn_scales', self.button_mix.text) # Choose any number you like!
    self.label_chosenscale.text = self.button_mix.text

  @handle("button_aeo", "click")
  def button_aeo_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.server.call('pico_fn_scales', self.button_aeo.text) # Choose any number you like!
    self.label_chosenscale.text = self.button_aeo.text

  @handle("button_startleds", "click")
  def button_startleds_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.server.call('pico_fn_startleds', 18) # Choose any number you like!

  @handle("drop_down_1", "change")
  def drop_down_1_change(self, **event_args):
    """This method is called when an item is selected"""
    anvil.server.call('pico_fn_scales', self.drop_down_1.selected_value) # Choose any number you like!
    self.label_chosenscale.text = self.drop_down_1.selected_value
 
