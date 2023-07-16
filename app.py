import os
import shutil
import cv2
import math
import requests
import validators #pip install validators
from pytube import YouTube # pip install pytube

cap = cv2.VideoCapture("videos/video2.mp4")

def Download(link):
    os.chdir(r'C:/Users/Ido/Desktop/videoToImages/videos')

    
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download()
    except:
        print("An error has occurred")
    print("Download is completed successfully")
    return youtubeObject.get_file_path()






def clearDicrectory(dirc_path):

    for filename in os.listdir(dirc_path):
        file_path = os.path.join(dirc_path, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))
            
            
            
def videoTime(cap):
    frame_count = cap.get(cv2.CAP_PROP_FRAME_COUNT)
    fps = cap.get(cv2.CAP_PROP_FPS)
    print(f"fps {fps}")

    seconds = math.floor(frame_count/fps)
    print(seconds)
    return seconds



link = input("Enter the YouTube video URL: ")
print(Download(link))

# clearDicrectory("frams")
# seconds = videoTime(cap)

# video_length_in_seconds = videoTime(cap)

