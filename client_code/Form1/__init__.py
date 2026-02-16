from ._anvil_designer import Form1Template
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

button_clicked_flag = False

# Find all tuples containing the search string
def find_tuples_with_string(tuple_list, search_str):
  if not all(isinstance(t, tuple) for t in tuple_list):
    raise TypeError("All elements in tuple_list must be tuples")
  if not isinstance(search_str, str):
    raise TypeError("Search term must be a string")

  return [t for t in tuple_list if any(search_str.lower() in str(item).lower() for item in t)]

def tuple_to_list(tup):
  # Validate that the input is a tuple
  if not isinstance(tup, tuple):
    raise TypeError("Input must be a tuple.")

    # Convert tuple to list
  return list(tup)

class RadioButtonGroup:
  """
    A generic radio-button-like group for Anvil Buttons.
    """
  def __init__(self, buttons, on_change=None):
    self.buttons = buttons
    self.selected = None
    self.on_change = on_change

    for btn in self.buttons:
      btn.background = 'grey'  # Reset style
      btn.foreground = 'white'
      
    # Attach click handlers to each button
    for btn in self.buttons:
      btn.set_event_handler('click', self._handle_click)

  def _handle_click(self, sender, **event_args):
    # Deselect all buttons
    for btn in self.buttons:
      btn.background = 'grey'  # Reset style
      btn.foreground = 'white'

      # Select the clicked button
    sender.background = 'green'  # Blue background
    sender.foreground = "white"
    self.selected = sender.text

    # Call the change callback if provided
    if self.on_change:
      self.on_change(self.selected)

  def get_selected(self):
    return self.selected

  
class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.chosen_key = 'None'
    self.chosen_scale = 'None'

    # Any code you write here will run before the form opens.
    scales_list = [(scales['name'], scales['layout']) for scales in app_tables.scales_extra.search()]
    print(scales_list)
    self.drop_down_scales_extra.items = scales_list
    # Create a radio-like group
    self.radio_group_key = RadioButtonGroup(
      [self.button_a, self.button_ab, self.button_b, self.button_bb,
      self.button_c, self.button_d, self.button_db, self.button_e,
      self.button_eb, self.button_f, self.button_g, self.button_gb],
      on_change=self.key_option_changed
    )

    # Create a radio-like group
    self.radio_group_scale = RadioButtonGroup(
      [self.button_aeo, self.button_dor, self.button_lyd, self.button_maj,
      self.button_majblu, self.button_majhar, self.button_majpen, self.button_min,
      self.button_minblu, self.button_minhar, self.button_minpen, self.button_mix,
      self.button_phr],
      on_change=self.scale_option_changed
    )

  def key_option_changed(self, selected_value):
    my_choice = -1
    if selected_value == 'C':
      my_choice = 0
    elif selected_value == 'Db':
      my_choice = 1
    elif selected_value == 'D':
      my_choice = 2
    elif selected_value == 'Eb':
      my_choice = 3
    elif selected_value == 'E':
      my_choice = 4
    elif selected_value == 'F':
      my_choice = 5
    elif selected_value == 'Gb':
      my_choice = 6
    elif selected_value == 'G':
      my_choice = 7
    elif selected_value == 'Ab':
      my_choice = 8
    elif selected_value == 'A':
      my_choice = 9
    elif selected_value == 'Bb':
      my_choice = 10
    elif selected_value == 'B':
      my_choice = 11

    self.chosen_key = selected_value
    anvil.server.call('pico_fn_keys', my_choice) # Choose any number you like!

  def scale_option_changed(self, selected_value):
    my_choice = 'None'
    if selected_value == 'Major':
      my_choice = "major"
    elif selected_value == 'Minor':
      my_choice ="natural_minor"
    elif selected_value == 'MajBlu':
      my_choice = "major_blues"
    elif selected_value == 'MinBlu':
      my_choice = "minor_blues"
    elif selected_value == 'MajPen':
      my_choice = "major_pentatonic"
    elif selected_value == 'MinPen':
      my_choice = "minor_pentatonic"
    elif selected_value == 'MajHar':
      my_choice = "None"
    elif selected_value == 'MinHar':
      my_choice = "harmonic_minor"
    elif selected_value == 'Dor':
      my_choice = "dorian"
    elif selected_value == 'Phr':
      my_choice ="phrygian"
    elif selected_value == 'Lyd':
      my_choice = "lydian"
    elif selected_value == 'Mix':
      my_choice = "mixolydian"
    elif selected_value == 'Aeo':
      my_choice = "aeolian"

    self.chosen_scale = selected_value
    anvil.server.call('pico_fn_scales', my_choice) # Choose any number you like!

  @handle("drop_down_scales_extra", "change")
  def drop_down_scales_extra_change(self, **event_args):
    """This method is called when an item is selected"""
    my_tuple = find_tuples_with_string(self.drop_down_scales_extra.items, self.drop_down_scales_extra.selected_value)
    print(my_tuple)
    my_list = tuple_to_list(my_tuple[0])
    anvil.server.call('pico_fn_scales', self.drop_down_scales_extra.selected_value) # Choose any number you like!
    self.chosen_scale = my_list[0]
  
  @handle("button_startleds", "click")
  def button_startleds_click(self, **event_args):
    """This method is called when the button is clicked"""
    my_key = self.chosen_key.strip()
    print("key:" + my_key)
    if my_key == "None":
      print("here")
      self.label_error_status.text = "No key has been chosen."
      return
    my_scale = self.chosen_scale.strip()
    print("scale:" + my_scale)
    if my_scale == "None":
      self.label_error_status.text = "No scale has been chosen."
      return
    self.label_error_status.text = ""  
    anvil.server.call('pico_fn_startleds', 18) # Choose any number you like!


    
    
 
 
