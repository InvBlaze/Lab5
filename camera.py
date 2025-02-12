from picamera2 import Picamera2
import time

def get_camera():
    """Returns an initialized Picamera2 instance."""
    picam = Picamera2()
    picam.start()
    time.sleep(2)  # Allow camera to warm up
    print("[DEBUG] Camera Initialized Successfully!")
    return picam

def capture_image(camera, image_out_location, countdown_time=0, preview=False):
    """Captures an image with an optional countdown."""
    if camera is None:
        print("[ERROR] Camera instance is None. Exiting capture_image function.")
        return

    print(f"[DEBUG] Waiting {countdown_time} seconds before capturing image...")
    time.sleep(countdown_time)

    try:
        print(f"[DEBUG] Capturing image and saving to {image_out_location}...")
        camera.capture_file(image_out_location)
        print("[DEBUG] Image Captured Successfully!")
    except Exception as e:
        print(f"[ERROR] Failed to Capture Image: {e}")

def capture_video(camera, video_out_location, video_length, countdown_time=0, preview=False):
    """Captures a video with an optional countdown."""
    if camera is None:
        print("[ERROR] Camera instance is None. Exiting capture_video function.")
        return

    print(f"[DEBUG] Waiting {countdown_time} seconds before starting video capture...")
    time.sleep(countdown_time)

    try:
        print(f"[DEBUG] Recording video for {video_length} seconds to {video_out_location}...")
        camera.start_recording(video_out_location)
        time.sleep(video_length)
        camera.stop_recording()
        print("[DEBUG] Video Recorded Successfully!")
    except Exception as e:
        print(f"[ERROR] Failed to Record Video: {e}")
