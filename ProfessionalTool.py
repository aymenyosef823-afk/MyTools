import os
import shutil

def organize_safe():
    path = os.getcwd()
    files = [f for f in os.listdir(path) if os.path.isfile(f)] # تنظيم الملفات فقط

    for file in files:
        if file == "ProfessionalTool.py": continue
        ext = file.split('.')[-1]
        if not os.path.exists(ext):
            os.makedirs(ext)
        shutil.move(file, os.path.join(ext, file))
        print(f"Done: {file} -> {ext}")

print("--- أداة يوسف الاحترافية الآمنة ---")
organize_safe()

