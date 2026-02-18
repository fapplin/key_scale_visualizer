from ._anvil_designer import RowTemplate1Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class RowTemplate1(RowTemplate1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  @handle("button_edit_row", "click")
  def button_edit_row_click(self, **event_args):
    """This method is called when the button is clicked"""
    print("button_edit_row_click")
    self.parent.raise_event('x-edit-scale-definition', scale_definition=self.item)

  @handle("button_delete_row", "click")
  def button_delete_row_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.parent.raise_event('x-delete-scale-definition', scale_definition=self.item)
