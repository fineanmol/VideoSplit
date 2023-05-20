# VideoSplit
This Script Split the Video into Multiple Short Videos as per our convenience

To use this script, you need to have OpenCV installed. You can install it using pip:
`pip install opencv-python`

When you run the script, it will prompt you to enter the path to the video file, start time, and end time for splitting. The script will create a directory named `split_videos` in the same location as the script file (if it doesn't exist already) and save the split videos inside that directory as "split_1.mp4", "split_2.mp4", and so on.

Please note that the script assumes the video file is in a format supported by OpenCV (e.g., MP4). If your video file is in a different format, you may need to install additional codecs or modify the script accordingly.
