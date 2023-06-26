import os

def delete_file(file_path):
    try:
        os.remove(file_path)
        print(f"Video file '{file_path}' deleted successfully.")
    except OSError as e:
        print(f"Error occurred while deleting the video file: {e}")