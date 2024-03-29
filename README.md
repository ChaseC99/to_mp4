# to_mp4
Convert batches of video to .mp4 format  

Given a source folder and a destination folder, this script will take all videos in the source folder and subdirectories of the source folder, and convert them to mp4.  
All converted files will be placed in the destination folder, following the directory structure of the source folder.  

Example:
```
- source
    - video1.mov
    - folder1
        - video2.mov
    - folder2
        - video3.mov
        - video4.mov
```
```
- destination
    - video1.mp4
    - folder1
        - video2.mp4
    - folder2
        - video3.mp4
        - video4.mp4
```

## Usage
`python3 to_mp4.py [source_folder] [destination_folder]`

## License
The python code that I have written falls under the [MIT License](https://github.com/ChaseC99/to_mp4/blob/master/LICENSE)  
However to use this script, you must have [FFmpeg](http://ffmpeg.org) installed, 
which is  licensed under the [LGPLv2.1](http://www.gnu.org/licenses/old-licenses/lgpl-2.1.html)
