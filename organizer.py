import os
import shutil
from datetime import datetime

# Настройки
TRACK_FOLDER = './test_folder'
LOG_FILE = 'activity_log.txt'

# Расширенный словарь
EXTENSIONS = {
    'jpg': 'Images', 'jpeg': 'Images', 'png': 'Images', 'gif': 'Images',
    'pdf': 'Documents', 'docx': 'Documents', 'txt': 'Documents', 'xlsx': 'Documents',
    'mp4': 'Videos', 'mov': 'Videos', 'avi': 'Videos',
    'mp3': 'Music', 'wav': 'Music',
    'zip': 'Archives', 'rar': 'Archives', '7z': 'Archives'
}

def log_action(message):
    """Записывает действие в файл лога с указанием времени"""
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open(LOG_FILE, 'a', encoding='utf-8') as f:
        f.write(f"[{timestamp}] {message}\n")

def clean_folder(target_path):
    if not os.path.exists(target_path):
        os.makedirs(target_path)
        print(f"Папка {target_path} создана.")
        return

    moved_count = 0

    for filename in os.listdir(target_path):
        file_path = os.path.join(target_path, filename)
        
        if os.path.isfile(file_path):
            if '.' in filename:
                ext = filename.split('.')[-1].lower()
                
                if ext in EXTENSIONS:
                    subfolder_name = EXTENSIONS[ext]
                    subfolder_path = os.path.join(target_path, subfolder_name)
                    
                    if not os.path.exists(subfolder_path):
                        os.makedirs(subfolder_path)
                    
                    try:
                        shutil.move(file_path, os.path.join(subfolder_path, filename))
                        msg = f"Перемещен: {filename} -> {subfolder_name}"
                        print(msg)
                        log_action(msg)
                        moved_count += 1
                    except Exception as e:
                        print(f"Ошибка с файлом {filename}: {e}")

    if moved_count > 0:
        print(f"Успех! Перемещено файлов: {moved_count}")
    else:
        print("Новых файлов для сортировки не найдено.")

if __name__ == "__main__":
    print("--- Смарт-Органайзер запущен ---")
    clean_folder(TRACK_FOLDER)
    print("--- Работа завершена ---")