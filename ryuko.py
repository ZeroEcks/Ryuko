#!/usr/bin/python2
# Inspired by
# http://rarlindseysmash.com/posts/stupid-programmer-tricks-and-star-wars-gifs
#         via https://news.ycombinator.com/item?id=6633490
# Requires
# * a reasonably recent ffmpeg suite
# * Graphicsmagick or ImageMagick
# * optionally: Gifsicle
# * an input video file
# Usage:
#   python gifgif.py a_video_file.avi

import subprocess
import argparse
import glob
import os


def run(cmd):
    print [str(c) for c in cmd]
    return subprocess.call([str(c) for c in cmd])

convert_command = "C:\Program Files\ImageMagick-6.8.7-Q16\convert.exe"


def get_frames(input_file, start, duration, fps=10, flip=False):
    if flip is True:
        run(["ffmpeg", "-ss", start, "-i", input_file, "-t",
            duration, "-r", fps, "-vf", "scale=500:-1, hflip,vflip",
            os.path.join("./gif", "%08d.png")])
    else:
        run(["ffmpeg", "-ss", start, "-i", input_file, "-t",
            duration, "-r", fps, "-vf", "scale=500:-1",
            os.path.join("./gif", "%08d.png")])
    return glob.glob(os.path.join(os.getcwd(), "gif", "*.png"))


def make_gif(output_file, frames, fps):
    run([convert_command] + [".\gif\*png"] + ["--coalesce", output_file])
    try:
        run(["gifsicle", "-O2", "--colors", 256, "--batch", "-i", output_file])
    except:
        pass


#def create_gif(input_file, output_file, start, duration):
def create_gif(args):
    frames = get_frames(args.input_file, args.start, args.duration,
                        fps=args.fps, flip=args.flip)
    make_gif(args.output_file, frames, args.fps)
    for frame in frames:
        os.unlink(frame)
    print args.output_file

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file",
                        help="The input video file (anything ffmpeg supports)",
                        type=str)
    parser.add_argument("output_file", help="The name of the output gif.",
                        type=str)
    parser.add_argument("start", help="The time in seconds to start the gif",
                        type=float)
    parser.add_argument("duration", help="Duration to create the gif",
                        type=float)
    parser.add_argument("-f", "--flip", help="Flip the image upside down.",
                        action="store_true", default=False)
    parser.add_argument("-fps", "--fps", help="FPS of the gif", type=int,
                        default=8)
    args = parser.parse_args()
    create_gif(args)
