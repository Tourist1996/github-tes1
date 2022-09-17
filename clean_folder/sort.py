import shutil
import sys
from pathlib import Path
cyrilica = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
latin_lang = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")
folder_format = {
    'images': ('.jpeg', '.png', '.jpg', '.svg'),
    'video': ('.avi', '.mp4', '.mov', '.mkv'),
    'documents': ('.doc', '.docx', '.txt', '.pdf', '.xls', '.pptx'),
    'audio': ('.mp3', '.ogg', '.wav', '.amr'),
    'archives': ('.zip', '.gz', '.tar')
}

perevod = {}
main_path_folder: Path | None = None
def main():
    global main_path_folder

    if len(sys.argv) < 2:
        print('Enter path to folder which should be sort')
        exit()

    root_dir = Path(sys.argv[1])

    if (not root_dir.exists()) or (not root_dir.is_dir()):
        print('please input correct path')
        exit()
    main_path_folder = root_dir
    translate()
    cleaner(root_dir)


def cleaner(folder: Path):

    for file in folder.iterdir():
        if file.is_file():
            sort_file(file)
        if file.is_dir():
            cleaner(file)
            if not any(file.iterdir()):
                file.rmdir()

def translate():
    for cyril, latin in zip(cyrilica, latin_lang):
        perevod[ord(cyril)] = latin
        perevod[ord(cyril.upper())] = latin.upper()


def normalize(file_name: str):
    normalized = file_name.translate(perevod)
    for i in normalized:
        if not i.isdigit() and not i.isalpha() and i != '_':
            normalized = normalized.replace(i, '_')
    return normalized


def sort_file(file: Path):
    suffix = file.suffix.lower()
    file_name = file.stem
    for key, values in folder_format.items():
        if suffix in values:
            normalizedname = normalize(file_name)
            file_name_new = normalizedname + suffix
            past_folder = main_path_folder.joinpath(key)
            past_folder.mkdir(exist_ok=True)
            file_path = past_folder.joinpath(file_name_new)
            file.rename(file_path)      
            if key == 'archives':
                file_archive = past_folder.joinpath(normalizedname)
                file_archive.mkdir(exist_ok=True)
                shutil.unpack_archive(file_path, file_archive)

if __name__ == '__main__':
    main()
    print('ready')
    exit()