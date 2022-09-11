import sys
import os
import shutil


def clearfolder(folder):
    all_files = os.listdir(folder)
    for file in all_files:
        file_path = os.path.join(folder, file)
        if file.endswith(('.jpeg', '.png','.PNG', '.jpg', '.svg', '.jfif')):
            new_path = os.path.join(folder, 'image')    
            if not os.path.exists(new_path):
                os.mkdir(new_path)
                new_file = os.path.join(new_path, file)
                os.replace(file_path, new_file)
            else:
                new_file = os.path.join(new_path, file)
                os.replace(file_path, new_file)
        elif file.endswith(('avi', 'mp4', 'mov', 'mkv')):
            new_path = os.path.join(folder, 'video')
            if not os.path.exists(new_path):
                os.mkdir(new_path)
                new_file = os.path.join(new_path, file)
                os.replace(file_path, new_file)
            else:
                new_file = os.path.join(new_path, file)
                os.replace(file_path, new_file)
        elif file.endswith(('.doc', '.docx', '.txt', '.pdf', '.xlsx', '.pptx')):
            new_path = os.path.join(folder, 'documents')
            if not os.path.exists(new_path):
                os.mkdir(new_path)
                new_file = os.path.join(new_path, file)
                os.replace(file_path, new_file)
            else:
                new_file = os.path.join(new_path, file)
                os.replace(file_path, new_file)
        elif file.endswith(('mp3', 'ogg', 'wav', 'amr')):
            new_path = os.path.join(folder, 'audio')
            if not os.path.exists(new_path):
                os.mkdir(new_path)
                new_file = os.path.join(new_path, file)
                os.replace(file_path, new_file)
            else:
                new_file = os.path.join(new_path, file)
                os.replace(file_path, new_file)      
        elif file.endswith(('zip', 'gz', 'tar', 'rar')):
            new_path = os.path.join(folder, 'archives')
            if file.endswith('.zip'):
                new_path2 = os.path.join(folder, 'archives')
                new_file2 = os.path.join(folder, file)
                extract_dir = (os.path.join(new_path2, file))
                shutil.unpack_archive(new_file2, extract_dir)
                os.rename(extract_dir, extract_dir.rsplit('.', maxsplit=1)[0])

if __name__=="__main__":
    folder = sys.argv[1]
    clearfolder(folder)
