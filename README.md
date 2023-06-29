# VideoSplit

This script allows you to split a video into multiple shorter videos based on your desired start and end times. It utilizes OpenCV for video processing. 

## Prerequisites

To use this script, you need to have OpenCV installed. If you haven't installed it yet, you can do so by running the following command:

```
pip install opencv-python
```

## Usage

1. Clone this repository to your local machine or download the script directly.

2. Open a terminal or command prompt and navigate to the directory where the script is located.

3. Run the script using the following command:

```
python videosplit.py
```

4. Follow the prompts on the command line:

   - Enter the path to the video file you want to split.
   - Specify the start time (in seconds) from where you want to begin the split.
   - Specify the end time (in seconds) where you want to end the split.

5. The script will create a directory named `split_videos` in the same location as the script file (if it doesn't exist already).

6. The resulting split videos will be saved inside the `split_videos` directory with names like "split_1.mp4", "split_2.mp4", and so on, based on the order of splitting.

**Note:** Please ensure that the video file you provide is in a format supported by OpenCV, such as MP4. If your video file is in a different format, you may need to install additional codecs or modify the script accordingly.

Feel free to customize and modify the script as per your requirements. Happy video splitting!
