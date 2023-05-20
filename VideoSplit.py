import os
import cv2

def split_video(video_path, start_time, end_time):
    # Create a directory to store the split videos
    output_dir = 'split_videos'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Open the video file
    video_capture = cv2.VideoCapture(video_path)
    total_frames = int(video_capture.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = video_capture.get(cv2.CAP_PROP_FPS)

    # Convert the start and end times to frame numbers
    start_frame = int(start_time * fps)
    end_frame = min(int(end_time * fps), total_frames)

    # Calculate the number of frames per split video (60 seconds)
    frames_per_split = int(fps * 60)

    # Initialize variables for tracking split video creation
    current_frame = start_frame
    split_count = 1

    while current_frame < end_frame:
        # Set the start frame for the current split video
        video_capture.set(cv2.CAP_PROP_POS_FRAMES, current_frame)

        # Create a VideoWriter object for the split video
        split_video_path = os.path.join(output_dir, f'split_{split_count}.mp4')
        split_video_writer = cv2.VideoWriter(split_video_path,
                                             cv2.VideoWriter_fourcc(*'mp4v'),
                                             fps,
                                             (int(video_capture.get(3)), int(video_capture.get(4))))

        # Write frames to the split video
        for _ in range(frames_per_split):
            ret, frame = video_capture.read()
            if not ret:
                break
            split_video_writer.write(frame)

        # Release the split video writer
        split_video_writer.release()

        # Update variables for the next split video
        current_frame += frames_per_split
        split_count += 1

    # Release the video capture
    video_capture.release()

    print('Split videos created successfully!')

# Ask for the input from the user
video_path = input('Enter the path to the video file: ')
start_time = float(input('Enter the start time (in seconds): '))
end_time = float(input('Enter the end time (in seconds): '))

# Call the split_video function
split_video(video_path, start_time, end_time)
