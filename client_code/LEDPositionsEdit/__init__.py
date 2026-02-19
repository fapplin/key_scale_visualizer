from ._anvil_designer import LEDPositionsEditTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class LEDPositionsEdit(LEDPositionsEditTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self.text_box_number_of_leds.text = str(self.item['number_of_leds'])
    self.text_box_led_positions.text = self.item['led_positions']