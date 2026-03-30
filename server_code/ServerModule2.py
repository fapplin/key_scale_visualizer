import anvil.server
import os
import time
from collections import namedtuple
import csv
import io


def csv_to_int_list(csv_string):
  """
    Convert a comma-separated string of numbers into a list of integers.
    Handles spaces and validates numeric values.
    """
  if not isinstance(csv_string, str):
    raise TypeError("Input must be a string.")

    # Split by comma and strip spaces
  items = csv_string.split(",")

  result = []
  for item in items:
    item = item.strip()  # Remove leading/trailing spaces
    if item == "":
      continue  # Skip empty entries
    try:
      result.append(int(item))
      #result.append(item)
    except ValueError:
      raise ValueError(f"Invalid number found: '{item}'")

  print("result:")
  print(result)
  return result


def scale_mask(root_note: str, intervals: list[int]) -> list[int]:
  """Return a 12-bit chromatic mask for a given root and interval pattern."""

  print("in scale_mask")
  root_index = CHROMATIC.index(root_note)
  print("root_index:")
  print(root_index)
  notes = [root_index]
  current = root_index

  print("intervals:")
  print(intervals)
  for step in intervals:
    #print("step:")
    #print(step)
    current = (current + step) % 12
    notes.append(current)

  mask = [0] * 12
  for i in notes:
    mask[i] = 1

  print("leaving scale_mask")
  return mask

def scale_matrix_for_interval(scale_intervals) -> dict[str, list[int]]:
    """Return a dict: root -> 12-bit mask for all 12 roots of a given scale type."""
    print("in scale_matrix_for_interval")
    print(f"scale_intervals: {scale_intervals}")
    
    #intervals = SCALE_FORMULAS[scale_type]
    intervals = scale_intervals
    #print("intervals:")
    #print(intervals)
    
    return {
        root: scale_mask(root, intervals)
        for root in CHROMATIC
    }

def print_key_scale_matrix(key_type, scale_intervals):
    """Pretty-print a 12x12 matrix for a given scale type."""
    
    print("in print_key_scale_matrix")
    print(f"key_type: {key_type}, scale_intervals: {scale_intervals}")
    matrix = scale_matrix_for_interval(scale_intervals)

    mask = matrix[key_type]
    bits = ", ".join(str(b) for b in mask)
    print(f" -> {bits}")
    new_list = [int(i) for i in bits.split(',')]
    print(new_list)
    return new_list

def rotate_list(nums, k):
    k = k % len(nums) # Handle cases where k > len(nums)
    return nums[-k:] + nums[:-k]

@anvil.server.callable()
def pico_fn_number_of_leds(nbr_leds):
    print(f"Called pico_fn_number_of_leds")
    print(nbr_leds)
    anvil.server.session["number_of_leds"] = nbr_leds
    tmp_path = "/home/frank/anvildir/led_client/leds.txt"
    with open(tmp_path, 'w') as f:
        f.write(str(nbr_leds))
        f.write("\n")
@anvil.server.callable()
def pico_fn_led_positions(led_pos):
    print(f"Called pico_fn_led_positions")
    print("led_pos:")
    print(led_pos)
    
    #temp_list = csv_to_int_list(led_pos)
    temp_list = led_pos
    #**********************************************************
    # Had to rig the code below because the list getting passed
    # was appending to itself (and I don't know why)
    #**********************************************************
    #unique_list = list(dict.fromkeys(temp_list))
    #print("unique_list:")
    #print(unique_list)
    #largest_value = max(unique_list)
    #unique_list.remove(largest_value)
    
    #anvil.server.session["LED_Positions"] = unique_list
    anvil.server.session["LED_Positions"] = temp_list
    print(anvil.server.session.get("LED_Positions"))
    
@anvil.server.callable()
def pico_fn_number_of_octaves(nbr_octs):
    print(f"Called pico_fn_number_of_octaves")
    print(nbr_octs)
    anvil.server.session["nbr_of_piano_octaves"] = int(nbr_octs)
    anvil.server.session["nbr_of_piano_keys"] = anvil.server.session.get("nbr_of_piano_octaves") * 12

@anvil.server.callable()
def pico_fn_keys(key):
    # Output will go to the Pico W serial port
    print(f"Called pico_fn_keys")
    print(key)
    anvil.server.session["selected_key"] = key
   
@anvil.server.callable()
def pico_fn_scales(scale):
    # Output will go to the Pico W serial port
    print(f"Called pico_fn_scales")
    print(scale)
    
    anvil.server.session["chosen_scale"] = csv_to_int_list(scale)
    
@anvil.server.callable()
def pico_fn_scale_color(scale_color):
    # Output will go to the Pico W serial port
    print(f"Called pico_fn_scale_color")
    print(scale_color)
    
    anvil.server.session["chosen_color"] = scale_color
 
   
@anvil.server.callable()
def pico_fn_startleds():
    print("Called pico_fn_startleds")
    

    if anvil.server.session.get("selected_key") == -1 or anvil.server.session.get("chosen_scale") == "None":
        return
    piano_keys = []
    # Output will go to the Pico W serial port
    
    
    key_str = CHROMATIC[anvil.server.session.get("selected_key")]
    
    new_scale = print_key_scale_matrix(key_str, anvil.server.session.get("chosen_scale"))
    print(f"new_scale: {new_scale}")
    
   
    #***************************************************
    # Fill a list with the particular scale in the
    # seen on a piano from left to right.
    #***************************************************
    for i in range(0, anvil.server.session.get("nbr_of_piano_octaves")):
        for j in range(0, 12):
            piano_keys.insert(0, new_scale[j])
    
            
    print("Original list")
    print(list(piano_keys))
    
    #***************************************************
    # Now, we rotate the list based on the key chosen.
    #***************************************************
    #rotated_piano_keys_list = rotate_list(piano_keys, chosen_key)
    
    piano_keys.reverse()
    
    print("reversed piano_keys: ")
    print(list(piano_keys))
    len_piano_keys = len(piano_keys) - 1
    print("len_piano_keys:")
    print(len_piano_keys)
    

    temp_leds = anvil.server.session.get("LED_Positions")
    print(temp_leds)
    
    sio = io.StringIO(temp_leds)
    reader = csv.reader(sio, skipinitialspace=True)
    string_list = next(reader)
    print("string_list:")
    print(string_list)

    led_cnt = len(string_list) - 2
    print("led_cnt:")
    print(led_cnt)
    
    tmp_path = "/home/frank/anvildir/led_client/leds.txt"
    with open(tmp_path, 'w') as f:
        nbr_leds = anvil.server.session.get("number_of_leds")    
        f.write(str(nbr_leds))
        f.write("\n")
        for i in range(len_piano_keys, -1, -1):
            print(f"{i}, {piano_keys[i]}")
            print("string_list[]:")
            print(string_list[led_cnt])
            if piano_keys[i] == 1:
                #f.write(str(temp_leds[led_cnt]))
                f.write(string_list[led_cnt])
                f.write(",")
                f.write(anvil.server.session.get("chosen_color"))
                f.write("\n")
            else:
                #f.write(str(temp_leds[led_cnt]))
                f.write(string_list[led_cnt])
                f.write(",")
                f.write("off")
                f.write("\n")
            led_cnt -= 1
    
    print(" end pico_fn_startleds")

    return 1


# ====== INITIALIZE ======
# ============================================
# Scale engine: binary masks for many scales
# ============================================

CHROMATIC = ["C", "C#", "D", "D#", "E", "F",
             "F#", "G", "G#", "A", "A#", "B"]
# This is an example Anvil Uplink script for the Pico W.
# See https://anvil.works/pico for more information

