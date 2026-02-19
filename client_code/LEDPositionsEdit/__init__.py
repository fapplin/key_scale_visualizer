from ._anvil_designer import LEDPositionsEditTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class LEDPositionsEdit(LEDPositionsEditTemplate):
  def __init__(self, previous_form=None, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    
    self.previous_form = previous_form
    my_list = app_tables.led_positions.search()
    print(my_list)
    for self.item in my_list:
      # Any code you write here will run before the form opens.
      self.text_box_number_of_leds.text = self.item['number_of_leds']
      self.text_box_led_positions.text = self.item['led_positions']
      self.drop_down_1.selected_value = self.item['number_of_octaves']

  @handle("button_close", "click")
  def button_close_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.item['number_of_octaves'] = self.drop_down_1.selected_value
    self.item.update()
    open_form(self.previous_form)
    
  @handle("drop_down_1", "change")
  def drop_down_1_change(self, **event_args):
    """This method is called when an item is selected"""
    pass
