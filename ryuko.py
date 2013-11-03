#!/usr/bin/python2
# Inspired by
# http://rarlindseysmash.com/posts/stupid-programmer-tricks-and-star-wars-gifs
# via https://news.ycombinator.com/item?id=6633490

import subprocess
import argparse
import glob
import os

CONVERT = os.path.join("bin", "convert")
OPTIMISE = os.path.join("bin", "gifsicle")
FFMPEG = os.path.join("bin", "ffmpeg")
SUBFILE = "sub.srt"

def run(cmd):
    """ Runs a command passed as a list """
    return subprocess.call([str(c) for c in cmd])

def extract_subs(input_file):
    run([FFMPEG, "-loglevel", "fatal", "-i", input_file, "-map", "0:s:0",
         SUBFILE])

def offset_subs(subfile, offset):
    run(["python", "subslider.py", subfile, "-%r" % int(offset)])

def get_frames(input_file, start, duration, fps=10, flip=False):
    """ Extracts the frames using FFMPEG """
    print "Extracting frames (call this 25%)"
    if flip is True:
        run([FFMPEG, "-loglevel", "fatal", "-ss", start, "-i", input_file, "-t",
            duration, "-r", fps, "-vf", "scale=500:-1, hflip,vflip",
            os.path.join("./gif", "%08d.png")])
    else:
        run([FFMPEG, "-loglevel", "fatal", "-ss", start, "-i", input_file, "-t",
            duration, "-r", fps, "-vf", "scale=500:-1,subtitles=sub.srt",
            os.path.join("./gif", "%08d.png")])
    return glob.glob(os.path.join(os.getcwd(), "gif", "*.png"))


def make_gif(output_file, frames):
    """ Creates the gif and optimises it """
    print "Creating gif (Call this 80%)"
    run([CONVERT] + [os.path.join("gif", "*png")] + [output_file])
    print "Optimising (Call this 99%)"
    run([OPTIMISE, "-O3", "--colors", 256, "--batch", "-i", output_file])


def create_gif(args):
    """ Calls functions to extract the frames and create the gif,
then remove the frames """
    extract_subs(args.input_file)
    offset_subs(SUBFILE, args.start)  # I will leave for you to figure out.
    frames = get_frames(args.input_file, args.start, args.duration,
                        fps=args.fps, flip=args.flip)
    make_gif(args.output_file, frames)
    for frame in frames:
        os.unlink(frame)

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
    parser.add_argument("-b", "--use-builtin",
                        help="Use the system `convert`, `ffmpeg`\
and `gifsicle` commands.", action="store_true")
    parser.add_argument("-fps", "--fps", help="FPS of the gif", type=int,
                        default=8)
    arguments = parser.parse_args()
    if arguments.use_builtin is True:
        CONVERT = "convert"
        OPTIMISE = "gifsicle"
        FFMPEG = "ffmpeg"
    create_gif(arguments)
