# to_mp4
#   
#   Convert videos to mp4 format using ffmpeg
#   Created by Chase Carnaroli - 2019

# Libraries
import os, sys

# Default variable values
extension = ".mp4"
sourceFolder = "./original/"
destinationFolder = "./mp4/"

# Recieve source and destination from cmd line
if len(sys.argv) == 3:
    sourceFolder = "./" + sys.argv[1]
    destinationFolder = "./" + sys.argv[2]
    
def convertFiles (sourceFolder, destinationFolder):
    # Get file path, not including the original source folder
    #   eg: "./orignial/extra/extra2" => "extra/extra2/"
    sourceFolderPath = sourceFolder.split("/")
    subfolderPath = "/".join(sourceFolderPath[2:])

    # For each file/dir in the directory
    for filename in os.listdir(sourceFolder):
        if os.path.isdir(sourceFolder + filename):
            # This is a folder
            # Create a new directory in destinationFolder
            # Run convertFiles on this sub dir
            os.mkdir(destinationFolder + subfolderPath + filename)
            convertFiles(sourceFolder + filename + "/", destinationFolder)
        else:
            # This is a file
            # Convert the file and at it to the destinationFolder
            os.system(f'ffmpeg -i "{sourceFolder + filename}" "{destinationFolder + subfolderPath + filename[:-4] + extension}"')

convertFiles(sourceFolder, destinationFolder)