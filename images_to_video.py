#!/usr/bin/env python

"""
################################################################################
#                                                                              #
# images_to_video                                                              #
#                                                                              #
################################################################################
#                                                                              #
# LICENCE INFORMATION                                                          #
#                                                                              #
# This program is a way of processing views of the ATLAS Control Room and OP   #
# Vistars pages.                                                               #
#                                                                              #
# copyright (C) 2015 William Breaden Madden                                    #
#                                                                              #
# This software is released under the terms of the GNU General Public License  #
# version 3 (GPLv3).                                                           #
#                                                                              #
# This program is free software: you can redistribute it and/or modify it      #
# under the terms of the GNU General Public License as published by the Free   #
# Software Foundation, either version 3 of the License, or (at your option)    #
# any later version.                                                           #
#                                                                              #
# This program is distributed in the hope that it will be useful, but WITHOUT  #
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or        #
# FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for     #
# more details.                                                                #
#                                                                              #
# For a copy of the GNU General Public License, see                            #
# <http://www.gnu.org/licenses/>.                                              #
#                                                                              #
################################################################################

Usage:
    program [options]

Options:
    -h, --help           display help message
    --version            display version and exit
    --extension=TEXT     input image files extension
                         [default: png]
    --soundtrack=FILE    soundtrack file
                         [default: None]
    --output=FILE        output video filename
                         [default: video.avi]
"""

name    = "images_to_video"
version = "2015-08-19T1434Z"

import docopt
import os
import time
import re
from   moviepy.editor import *
import shijian

def main(options):

    codecVideo = "png" # "mpeg4"
    codecAudio = "libvorbis"

    # access options and arguments
    extension          = options["--extension"]
    soundtrackFilename = options["--soundtrack"]
    outputFilename     = options["--output"]

    listOfImageFiles = shijian.find_file_sequences(
        extension = extension
    )
    print("list of image files: {listOfImageFiles}".format(
        listOfImageFiles = listOfImageFiles
    ))
    video = ImageSequenceClip(listOfImageFiles, fps = 30)

    raw_input("Press Enter to write video.")

    if soundtrackFilename == "None":
        video.write_videofile(
            outputFilename,
            fps         = 30,
            codec       = codecVideo,
            audio       = False
        )
    else:
        soundtrack = AudioFileClip(soundtrackFilename)
        video = video.set_audio(soundtrack)
        video.write_videofile(
            outputFilename,
            fps         = 30,
            codec       = codecVideo,
            audio_codec = codecAudio,
            audio       = True
        )

if __name__ == "__main__":
    options = docopt.docopt(__doc__)
    if options["--version"]:
        print(version)
        exit()
    main(options)
