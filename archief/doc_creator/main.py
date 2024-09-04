from pathlib import Path
import shutil

IMAGE_EXT = ["png", "jpg", "jpeg", "gif", "jfif"]
VIDEO_EXT = ["mp4", "mkv", "avi"]
DOCS_EXT = ['doc', 'docx', 'odt', 'pdf', 'xls', 'xlsx', 'ods', 'ppt', 'pptx', 'txt']
APPLICATION_EXT = ["exe", "msi"]
ARCHIVE_EXT = ["zip", "rar"]
SUBTITLE_EXT = ["srt"]

path_dir = Path('C:/Users/Svenb/Downloads')
target_dir_docs = ('B:\Downloads\Documents')
target_dir_movies = ('')




for file in path_dir.iterdir():
    if file.is_file() and file.suffix == '.pdf':
        shutil.move(file, target_dir)