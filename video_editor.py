from moviepy.editor import VideoFileClip, concatenate_videoclips
import os
import random
import re

def cut_full_video(input_video, output_folder, quality='high', video_cut_length=3):
    clip = VideoFileClip(input_video)
    duration = int(clip.duration)
    
    for i in range(duration):
        sub_clip = clip.subclip(i, i+video_cut_length)
        if quality == 'low':
            sub_clip.write_videofile(f"{output_folder}/clip_{i}.mp4", fps=24, codec='libx264', bitrate="5000k")
        elif quality == 'medium':
            sub_clip.write_videofile(f"{output_folder}/clip_{i}.mp4", fps=24, codec='libx264', bitrate="10000k")
        elif quality == 'high':
            sub_clip.write_videofile(f"{output_folder}/clip_{i}.mp4", fps=24, codec='libx264', bitrate="20000k")
        else:
            print("Invalid quality option. Please choose 'low', 'medium', or 'high'.")

def cut_range_video(input_video, output_folder, start_time, end_time, quality='high'):
    if start_time > end_time:
        print("Start time should be less then end time")
        return
    clip = VideoFileClip(input_video)
    sub_clip = clip.subclip(start_time, end_time)
    if quality == 'low':
        sub_clip.write_videofile(f"{output_folder}/clip_{start_time}_{end_time}.mp4", fps=24, codec='libx264', bitrate="5000k")
    elif quality == 'medium':
        sub_clip.write_videofile(f"{output_folder}/clip_{start_time}_{end_time}.mp4", fps=24, codec='libx264', bitrate="10000k")
    elif quality == 'high':
        sub_clip.write_videofile(f"{output_folder}/clip_{start_time}_{end_time}.mp4", fps=24, codec='libx264', bitrate="20000k")
    else:
        print("Invalid quality option. Please choose 'low', 'medium', or 'high'.")

def concatenate_random_clips(source_folder, destination_path):
    video_files = [f for f in os.listdir(source_folder) if f.startswith('clip_') and f.endswith('.mp4')]
    if not video_files:
        print("No video files found in the source folder.")
        return

    even_numbered_clips = [
        f for f in video_files 
        if int(re.search(r'(\d+)\.mp4$', f).group(1)) % 2 == 0
    ]

    random.shuffle(even_numbered_clips)
    video_clips = [VideoFileClip(os.path.join(source_folder, file)) for file in even_numbered_clips]
    final_clip = concatenate_videoclips(video_clips)
    final_clip.write_videofile(destination_path, codec='libx264')
    for clip in video_clips:
        clip.close()

    print(f"Video created successfully at {destination_path}")

input_video = "/media/rony/ssd-01/movie_explanation/new.webm"
output_folder = "output_folder"
quality = 'high'  # Choose between 'low', 'medium', or 'high'
start_time = 60
end_time = 63

concatenate_random_clips(output_folder, "./output.mp4")
