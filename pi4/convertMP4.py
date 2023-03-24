import subprocess
import os
import logging
ANIME_PATH="/home/teko/webserver/volumes/multimedia/media/anime"
logging.basicConfig(
    filename="/home/teko/bin/logs/convertMP4.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
)
logging.info("Starting MP4 conversion")

for path, subdirs, files in os.walk(ANIME_PATH):
    for name in files:
        if ".mp4" not in name:
            file=os.path.join(path,name)
            logging.info(f"Found file {file}")
            converted_file=file[:-3]+"mp4"
            result = subprocess.run(['ffmpeg','-i',file,"-codec","copy", converted_file], stdout=subprocess.PIPE)
            os.remove(file)
            logging.info(f"Converted {file} to {result}")

logging.info("Finished conversion")
