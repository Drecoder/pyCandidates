import time
import keyboard

def countdown(seconds):
    for i in range(seconds, 0, -1):
        print(f"Starting in {i} seconds...", end='\r')
        time.sleep(1)
    print("Starting now!")

def simulate_keyboard_actions():
    countdown(30)  # Start with a 10-second countdown

    for iteration in range(1, 21):  # Repeat the sequence 20 times
        # Simulate pressing the "Up" arrow key
        keyboard.press_and_release('up')
        time.sleep(1)

        # Simulate pressing the "Right" arrow key three times
        keyboard.press_and_release('right')
        time.sleep(0.5)
        keyboard.press_and_release('right')
        time.sleep(0.5)
        keyboard.press_and_release('right')
        time.sleep(1)

        # Simulate pressing the "Enter" key
        keyboard.press_and_release('enter')
        time.sleep(1)

        # Simulate pressing Ctrl+A to select all
        keyboard.press_and_release('ctrl+a')
        time.sleep(1)

        # Simulate pressing Ctrl+C to copy
        keyboard.press_and_release('ctrl+c')
        time.sleep(1)

        # Simulate pressing Ctrl+V to paste
        keyboard.press_and_release('ctrl+v')
        time.sleep(1)

        # Simulate pressing Esc
        keyboard.press_and_release('esc')
        time.sleep(1)

        # Simulate pressing the "Left" arrow key three times
        keyboard.press_and_release('left')
        time.sleep(0.5)
        keyboard.press_and_release('left')
        time.sleep(0.5)
        keyboard.press_and_release('left')
        time.sleep(1)

        # Wait for 20 seconds before starting the next iteration
        time.sleep(2)
        # Wait for 40 seconds before starting the next iteration
        countdown(60)

        # Log the number of iterations in the console
        print(f"Iteration: {iteration}")

if __name__ == "__main__":
    simulate_keyboard_actions()
