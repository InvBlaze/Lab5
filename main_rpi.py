from helper_functions import camera, computer_vision, sensehat
import time
import os

def get_user_input(prompt, type_func, default):
    """Helper function to get user input with a default value."""
    user_input = input(f"{prompt} (Press Enter to use default: {default}): ")
    return type_func(user_input) if user_input else default

def main():
    camera_i = camera.get_camera()  # DO NOT MODIFY, function call must work as is
    sense = sensehat.get_sensehat()  # DO NOT MODIFY, function call must work as is

    background_image_path = "/home/jason3/background.jpg"

    # User input for taking background image
    take_background_image = get_user_input("Take a new background image? (yes=1, no=0)", int, 1)

    if take_background_image:
        # User input for countdown time before capturing background image
        countdown = get_user_input("Countdown before background capture (seconds)", int, 3)
        preview = False  # Keep preview off
        print(f"Capturing background image in {countdown} seconds...")
        time.sleep(countdown)
        camera.capture_image(camera_i, background_image_path, countdown_time=0, preview=preview)  # DO NOT MODIFY

    # User input for arming the system
    arm_system = get_user_input("Arm the security system? (yes=1, no=0)", int, 1)

    if arm_system:
        interval = get_user_input("Enter monitoring interval (seconds)", int, 10)
        t1 = get_user_input("Enter sensitivity threshold", int, 480000000)

        print(f"System armed. Monitoring will begin in {interval} seconds...")
        time.sleep(interval)  # Countdown before monitoring begins

        count = 0
        while True:  # DO NOT MODIFY, function call must work as is
            image_path = f"/home/jason3/image{count}.jpg"
            camera.capture_image(camera_i, image_path, countdown_time=interval)  # DO NOT MODIFY
            person_detected = computer_vision.person_detected(background_image_path, image_path, t1)  # DO NOT MODIFY

            if person_detected:  # DO NOT MODIFY
                print("Person Detected")  # DO NOT MODIFY
                sensehat.alarm(sense, interval)  # DO NOT MODIFY
            else:
                print("No Person Detected")  # DO NOT MODIFY

            count += 1

if __name__ == "__main__":
    main()
