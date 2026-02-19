import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server


# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
# @anvil.server.callable
# def say_hello(name):
#   print("Hello, " + name + "!")
#   return 42
#
@anvil.server.callable
def add_scale_definition(scale_data):
  if scale_data.get('listbox_text') and scale_data.get('scale_name') and scale_data.get('scale_definition'):
    app_tables.listbox_scale_definitions.add_row(**scale_data)

@anvil.server.callable
def update_scale_definition(scale_definition, scale_data):
  if scale_data['listbox_text'] and scale_data['scale_name'] and scale_data['scale_definition']:
    scale_definition.update(**scale_data)

@anvil.server.callable
def delete_scale_definition(scale_definition):
  scale_definition.delete()    

@anvil.server.callable
def edit_led_positions(led_data):
  pass
  