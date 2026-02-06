from ._anvil_designer import Form1Template
from anvil import *
import anvil.server

MAJOR =                 "1,0,1,0,1,1,0,1,0,1,0,1"
MINOR = 			      	  "1,0,1,1,0,1,0,1,1,0,1,0"
MAJOR_BLUES =           "1,0,0,1,0,1,1,1,0,0,1,0"
MINOR_BLUES  =          "1,0,1,0,1,0,0,1,0,1,0,0"
MAJOR_PENTATONIC =      "1,0,1,0,1,0,0,1,0,1,0,0"
MINOR_PENTATONIC =      "1,0,0,1,0,1,0,1,0,0,1,0"
MAJOR_HARMONIC =        "1,0,1,0,1,1,0,1,1,0,0,1"
MINOR_HARMONIC =        "1,0,1,1,0,1,0,1,1,0,0,1"
DORIAN =                "1,0,1,1,0,1,0,1,0,1,1,0"
PHRYGIAN =			  "1,1,0,1,0,1,0,1,1,0,1,0"
LYDIAN = 				  "1,0,1,0,1,0,1,1,0,1,0,1"
MIXOLYDIAN = 			  "1,0,1,0,1,1,0,1,0,1,1,0"
AEOLIAN = 			  "1,0,1,1,0,1,0,1,1,0,1,0"
LOCRIAN =               "1,1,0,1,0,1,1,0,1,0,1,0"
BEBOP = 				  "1,0,1,0,1,1,0,1,0,1,1,1"
GYPSY = 				  "1,0,1,1,0,0,1,1,1,0,1,0"
HIRAJOSHI =			  "1,0,0,0,1,0,1,1,0,0,0,1"
HUNGARIAN = 			  "1,0,1,1,0,0,1,1,1,0,0,1"
LOCRIAN = 			  "1,1,0,1,0,1,1,0,1,0,1,0"
PERSIAN = 			  "1,1,0,0,1,1,1,0,1,0,0,1"
UKRANIAN = 			  "1,0,1,1,0,0,1,1,0,1,1,0"

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
    anvil.server.call('pico_fn_scales', C_MAJOR) # Choose any number you like!
    self.label_chosenscale.text = self.button_maj.text

  @handle("button_min", "click")
  def button_min_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.server.call('pico_fn_scales', C_MINOR) # Choose any number you like!
    self.label_chosenscale.text = self.button_min.text

  @handle("button_majblu", "click")
  def button_majblu_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.server.call('pico_fn_scales', C_MAJOR_BLUES) # Choose any number you like!
    self.label_chosenscale.text = self.button_majblu.text

  @handle("button_minblu", "click")
  def button_minblu_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.server.call('pico_fn_scales',C_MINOR_BLUES) # Choose any number you like!
    self.label_chosenscale.text = self.button_minblu.text

  @handle("button_majpen", "click")
  def button_majpen_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.server.call('pico_fn_scales' ,C_MAJOR_PENTATONIC) # Choose any number you like!
    self.label_chosenscale.text = self.button_majpen.text

  @handle("button_minpen", "click")
  def button_minpen_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.server.call('pico_fn_scales', C_MINOR_PENTATONIC) # Choose any number you like!
    self.label_chosenscale.text = self.button_minpen.text

  @handle("button_majhar", "click")
  def button_majhar_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.server.call('pico_fn_scales',C_MAJOR_HARMONIC) # Choose any number you like!
    self.label_chosenscale.text = self.button_majhar.text

  @handle("button_minhar", "click")
  def button_minhar_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.server.call('pico_fn_scales', C_MINOR_HARMONIC) # Choose any number you like!
    self.label_chosenscale.text =  self.button_minhar.text

  @handle("button_dor", "click")
  def button_dor_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.server.call('pico_fn_scales', C_DORIAN) # Choose any number you like!
    self.label_chosenscale.text = self.button_dor.text

  @handle("button_phr", "click")
  def button_phr_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.server.call('pico_fn_scales',C_PHRYGIAN) # Choose any number you like!
    self.label_chosenscale.text = self.button_phr.text

  @handle("button_lyd", "click")
  def button_lyd_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.server.call('pico_fn_scales', C_LYDIAN) # Choose any number you like!
    self.label_chosenscale.text = self.button_lyd.text

  @handle("button_mix", "click")
  def button_mix_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.server.call('pico_fn_scales', C_MIXOLYDIAN) # Choose any number you like!
    self.label_chosenscale.text = self.button_mix.text

  @handle("button_aeo", "click")
  def button_aeo_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.server.call('pico_fn_scales', C_AEOLIAN) # Choose any number you like!
    self.label_chosenscale.text = self.button_aeo.text

  @handle("button_startleds", "click")
  def button_startleds_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.server.call('pico_fn_startleds', 18) # Choose any number you like!

  @handle("drop_down_1", "show")
  def drop_down_1_show(self, **event_args):
    self.drop_down_1.items = ([("NONE", ""),
                           ("LOCRIAN", "1,1,0,1,0,1,1,0,1,0,1,0"), 
                           ("BEBOP", "1,0,1,0,1,1,0,1,0,1,1,1")])
    
  @handle("drop_down_1", "change")
  def drop_down_1_change(self, **event_args):
    """This method is called when an item is selected"""
    anvil.server.call('pico_fn_scales', ) # Choose any number you like!
    self.label_chosenscale.text = self.drop_down_1.selected_value
 
