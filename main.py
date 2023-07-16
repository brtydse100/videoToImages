import shutil
import cv2
import os
import math
from pytube import YouTube # pip install pytube


cap = cv2.VideoCapture("videos/video2.mp4")
os.chdir(r'C:/Users/Ido/Desktop/videoToImages/frams')
fps = cap.get(cv2.CAP_PROP_FPS)
dir_path = r"C:\Users\Ido\Desktop\videoToImages\frams"


def videoTime(cap):
    frame_count = cap.get(cv2.CAP_PROP_FRAME_COUNT)
    fps = cap.get(cv2.CAP_PROP_FPS)
    seconds = math.floor(frame_count/fps)

    return seconds

def videoDownload(link):
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


def videoToImagesByTime(video_path):
    cap = cv2.VideoCapture(video_path)
    clearDicrectory(dir_path)

    frame_counter = 0
    image_counter = 1
    video_length_in_seconds = math.floor(videoTime(cap))

    seconds_between_every_image = float(
        input("please enter the amount of seconds you want between every frame: "))
    start = input(
        f"if you choose {seconds_between_every_image} you will get {int(video_length_in_seconds/seconds_between_every_image)} images do you wish to continue? [N/Y]")

    while (start != "Y" and start != "y"):
        seconds_between_every_image = float(
            input("please enter the amount of seconds you want between every frame: "))
        start = input(
            f"if you will choose {seconds_between_every_image} between every image you will get {int(video_length_in_seconds/seconds_between_every_image)} images do you wish to continue? [N/Y]")

    frames_between_images = math.floor(seconds_between_every_image*fps)

    if start == "Y" or start == "y":
        while cap.isOpened():
            ret, frame = cap.read()
            if ret:
                if (frame_counter == frames_between_images):
                    cv2.imwrite(f"img{image_counter}.jpg", frame)
                    image_counter += 1
                    frame_counter = 0

                frame_counter += 1
            else:
                break


def videoToImagesByFrames(video_path):
    
    cap = cv2.VideoCapture(video_path)
    clearDicrectory(dir_path)

    frame_count = cap.get(cv2.CAP_PROP_FRAME_COUNT)
    frame_counter = 0
    image_counter = 1

    frames_between_every_image = float(
        input("please enter the a mount of frams you want between every frame: "))
    start = input(
        f"if you choose {frames_between_every_image} between every image you will get {int(frame_count/frames_between_every_image)} images do you wish to continue? [N/Y]")

    while (start != "Y" and start != "y"):
        frames_between_every_image = float(
            input("please enter the a mount of seconds you want between every frame: "))
        start = input(
            f"if you will choose {frames_between_every_image} between every image you will get {int(frame_count/frames_between_every_image)} images do you wish to continue? [N/Y]")

    if start == "Y" or start == "y":
        while cap.isOpened():
            ret, frame = cap.read()
            if ret:
                if (frame_counter == frames_between_every_image):
                    cv2.imwrite(f"img{image_counter}.jpg", frame)
                    image_counter += 1
                    frame_counter = 0

                frame_counter += 1
            else:
                break


# videoToImagesByTime(r"C:\Users\Ido\Desktop\videoToImages\videos\video1.mp4")
videoToImagesByFrames(r"C:\Users\Ido\Desktop\videoToImages\videos\video1.mp4")
