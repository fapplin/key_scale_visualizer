from ._anvil_designer import ScaleDefsListTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..ScaleDefsEdit import ScaleDefsEdit


class ScaleDefsList(ScaleDefsListTemplate):
  def __init__(self, previous_form=None, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.previous_form = previous_form
    self.repeating_panel_1.items = app_tables.listbox_scale_definitions.search()
    self.repeating_panel_1.add_event_handler('x-edit-scale-definition', self.edit_scale_definition)
    self.repeating_panel_1.add_event_handler('x-delete-scale-definition', self.delete_scale_definition)
  # Any code you write here will run before the form opens.

  @handle("button_add_scale_definition", "click")
  def button_add_scale_definition_click(self, **event_args):
    """This method is called when the button is clicked"""
    item = {}
    editing_form =ScaleDefsEdit(item=item)
    
    #if the user clicks OK on the alert
    if alert(content=editing_form, large=True):
    #add the movie to the Data Table with the filled in information
      anvil.server.call('add_scale_definition', item)
      #refresh the Data Grid
      self.repeating_panel_1.items = app_tables.listbox_scale_definitions.search()
      
      
  def edit_scale_definition(self, scale_definition, **event_args):
    #movie is the row from the Data Table
    item = dict(scale_definition)
    editing_form = ScaleDefsEdit(item=item)

    #if the user clicks OK on the alert
    if alert(content=editing_form, large=True):
      #pass in the Data Table row and the updated info
      anvil.server.call('update_scale_definition', scale_definition, item)
      #refresh the Data Grid
      self.repeating_panel_1.items = app_tables.listbox_scale_definitions.search()

  def delete_scale_definition(self, scale_definition, **event_args):
    if confirm(f"Do you really want to delete the scale_definition {scale_definition['listbox_text']}?"):
      anvil.server.call('delete_scale_definition', scale_definition)
      #refresh the Data Grid
      self.repeating_panel_1.items = app_tables.listbox_scale_definitions.search()

  @handle("button_1", "click")
  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    
    open_form(self.previous_form)
