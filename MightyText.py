import time
import keyboard

def countdown(seconds):
    for i in range(seconds, 0, -1):
        print(f"Starting in {i} seconds...", end='\r')
        time.sleep(1)
    print("Starting now!")

def simulate_keyboard_actions():
    countdown(10)  # Start with a 10-second countdown

    for iteration in range(1, 21):  # Repeat the sequence 20 times
        # Simulate pressing the "Up" arrow key to move into the cell and copy the information
        keyboard.press_and_release('up')
        time.sleep(0.25)

        # Wait for 20 seconds before pasting the copied information
        time.sleep(20)

        # Simulate pressing Ctrl+V to paste the copied information
        keyboard.press_and_release('ctrl+v')
        time.sleep(0.25)

        # Simulate pressing Ctrl+A to select all
        keyboard.press_and_release('ctrl+a')
        time.sleep(0.25)

        # Simulate pressing Ctrl+C to copy
        keyboard.press_and_release('ctrl+c')
        time.sleep(0.25)

        # Extract the phone number from clipboard text
        clipboard_text = keyboard.clipboard.get()
        phone_number = extract_phone_number(clipboard_text)

        if phone_number:
            print("Extracted phone number:", phone_number)

            # Wait for 20 seconds before pasting the extracted phone number
            time.sleep(10)

            # Simulate typing the extracted phone number
            keyboard.write(phone_number)
            time.sleep(0.25)
        else:
            print("No phone number found in clipboard text.")

        # Wait for 20 seconds before starting the next iteration
        time.sleep(10)

        # Log the number of iterations in the console
        print(f"Iteration: {iteration}")

def extract_phone_number(text):
    # Check if the text matches the format for a phone number (XXX-XXX-XXXX)
    if len(text) == 12 and text[3] == '-' and text[7] == '-':
        return text
    else:
        return None

if __name__ == "__main__":
    simulate_keyboard_actions()
