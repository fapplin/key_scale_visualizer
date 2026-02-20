from ._anvil_designer import ScaleDefsEditTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class ScaleDefsEdit(ScaleDefsEditTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.load_dropdown()

  def load_dropdown(self):
    try:
      items = anvil.server.call('get_dropdown_color_items')
      self.drop_down_color.items = items  # items is a list of (text, value) tuples
    except Exception as e:
      print(f"Error loading dropdown: {e}")
      self.drop_down_color.items = []

    # Any code you write here will run before the form opens.
