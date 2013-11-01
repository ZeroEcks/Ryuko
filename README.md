# Ryuko
Ryuko creates gifs from (almost) any video file. It's pretty neat so like if you like gifs, use it.

## How to use Ryuko!
This is aimed at begginers with no command line knowledge. If you know what your doing, here is the outline.
1. Clone Ryuko
2. Run with Python 2.7
3. Add it to your path if you want.
Skip to the next section if you want help on the command.
### Setting things up
Clone (`git clone`) or download this repository (The "Download Zip" button on the left if you don't know what I mean). Extract everything if you downloaded an archive.

`cd` into the directory where you extracted Ryuko to and use `python ryuko.py` to run it. Here is the example output.

```
PS F:\code\Ryuko> python .\ryuko.py
usage: ryuko.py [-h] [-f] [-b] [-fps FPS]
                input_file output_file start duration
ryuko.py: error: too few arguments
```
If you see an error along the lines of "Python not found" or that Python isn't a command, go and make sure python (2.7 is used) is in your path and uses the command `python`. If you got output like mine, you are ready to rock and roll!

### Using Ryuko
To get the usage for `ryuko.py` just run `python ryuko.py -h`
```
usage: ryuko.py [-h] [-f] [-b] [-fps FPS]
                input_file output_file start duration

positional arguments:
  input_file           The input video file (anything ffmpeg supports)
  output_file          The name of the output gif.
  start                The time in seconds to start the gif
  duration             Duration to create the gif

optional arguments:
  -h, --help           show this help message and exit
  -f, --flip           Flip the image upside down.
  -b, --use-builtin    Use the system `convert`, `ffmpeg` and `gifsicle`
                       commands.
  -fps FPS, --fps FPS  FPS of the gif
```
Most of the options are pretty self explanatory really, `input_file` is any video file that ffmpeg can use and `output_file` is the name of your gif. `start` is the time in seconds to start creating the gif and `duration` is how long to make the gif. The other flags are `-f` to flip the image upside down, `-b` to use the builtin commands (Use this on not windows!) and `-fps FPS` is the FPS of the gif.
