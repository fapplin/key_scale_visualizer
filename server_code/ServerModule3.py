import anvil.server
import os
import io
import csv

# ====== CONFIGURATION ======
# This path only exists on your Raspberry Pi
PI_FILE_PATH = "/home/frank/anvildir/M3_App_2/services/leds.txt"

CHROMATIC = ["C", "C#", "D", "D#", "E", "F",
             "F#", "G", "G#", "A", "A#", "B"]

# ====== HELPER FUNCTIONS ======

def save_to_pi_or_console(content):
  """
    Writes to the Pi's filesystem if available, 
    otherwise prints to the Anvil console for web testing.
    """
  print("in save_to_pi_or_console()")

  target_dir = os.path.dirname(PI_FILE_PATH)

  if os.path.exists(target_dir):
    try:
      with open(PI_FILE_PATH, 'w') as f:
        f.write(content)
      print(f"Successfully wrote to {PI_FILE_PATH}")
    except Exception as e:
      print(f"Error writing to file: {e}")
  else:
      print("--- WEB TESTING MODE (No Pi Filesystem Found) ---")
      print("Data that would be written to leds.txt:")
      print(content)
      print("-----------------------------------------------")
  
  print("out save_to_pi_or_console()")

def csv_to_int_list(csv_string):
    if not isinstance(csv_string, str):
        return csv_string # Already a list? Return as is.
    
    items = csv_string.split(",")
    result = []
    for item in items:
        item = item.strip()
        if item:
            try:
                result.append(int(item))
            except ValueError:
                continue 
    return result

# ====== SCALE LOGIC ======

def scale_mask(root_note: str, intervals: list[int]) -> list[int]:
    root_index = CHROMATIC.index(root_note)
    notes = [root_index]
    current = root_index

    for step in intervals:
        current = (current + step) % 12
        notes.append(current)

    mask = [0] * 12
    for i in notes:
        mask[i] = 1
    return mask

def scale_matrix_for_interval(scale_intervals) -> dict:
    return {
        root: scale_mask(root, scale_intervals)
        for root in CHROMATIC
    }

def get_piano_scale_list(key_type, scale_intervals):
    matrix = scale_matrix_for_interval(scale_intervals)
    return matrix[key_type]

# ====== ANVIL CALLABLES ======

@anvil.server.callable()
def pico_fn_number_of_leds(nbr_leds):
    anvil.server.session["number_of_leds"] = nbr_leds
    # Save immediate update
    save_to_pi_or_console(str(nbr_leds) + "\n")

@anvil.server.callable()
def pico_fn_led_positions(led_pos):
    # Store the positions (keep as string for easier CSV processing later)
    anvil.server.session["LED_Positions"] = led_pos

@anvil.server.callable()
def pico_fn_number_of_octaves(nbr_octs):
    anvil.server.session["nbr_of_piano_octaves"] = int(nbr_octs)
    anvil.server.session["nbr_of_piano_keys"] = int(nbr_octs) * 12

@anvil.server.callable()
def pico_fn_keys(key):
    anvil.server.session["selected_key"] = key

@anvil.server.callable()
def pico_fn_scales(scale):
    anvil.server.session["chosen_scale"] = csv_to_int_list(scale)

@anvil.server.callable()
def pico_fn_scale_color(scale_color):
    anvil.server.session["chosen_color"] = scale_color

@anvil.server.callable()
def pico_fn_startleds():
    # 1. Validation
    sel_key = anvil.server.session.get("selected_key")
    chosen_scale = anvil.server.session.get("chosen_scale")
    led_pos_str = anvil.server.session.get("LED_Positions")
    
    if sel_key is None or chosen_scale is None or not led_pos_str:
        print("Missing session data. Cannot start LEDs.")
        return 0

    # 2. Build the Piano Mask (repeating for octaves)
    key_str = CHROMATIC[sel_key]
    octave_mask = get_piano_scale_list(key_str, chosen_scale)
    
    piano_keys = []
    num_octaves = anvil.server.session.get("nbr_of_piano_octaves", 1)
    for _ in range(num_octaves):
        piano_keys.extend(octave_mask)
    
    # 3. Parse the LED positions CSV string
    f = io.StringIO(led_pos_str)
    reader = csv.reader(f, skipinitialspace=True)
    try:
        string_list = next(reader)
    except StopIteration:
        return 0

    # 4. Generate the File Content
    output_lines = []
    nbr_total_leds = anvil.server.session.get("number_of_leds", len(string_list))
    output_lines.append(str(nbr_total_leds))

    chosen_color = anvil.server.session.get("chosen_color", "white")
    
    # We map the piano keys to the LED list
    # Your original logic used a reverse led_cnt, so we match that here
    led_cnt = len(string_list) - 1
    
    # Iterate through piano keys (adjust range to match available LEDs)
    for i in range(len(piano_keys) - 1, -1, -1):
        if led_cnt < 0: break # Safety check
        
        state = chosen_color if piano_keys[i] == 1 else "off"
        output_lines.append(f"{string_list[led_cnt]},{state}")
        led_cnt -= 1

    final_file_content = "\n".join(output_lines)

    # 5. Save/Print
    save_to_pi_or_console(final_file_content)
    
    return 1
