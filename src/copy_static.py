# copy static files from /static to /public
import os
import shutil


def copy_static(src, dst):
    # check if src and dst directories exist
    if os.path.exists(src) == False:
        raise ValueError("source directory unfound")

    # loop through all items in the source directory
    src_list = os.listdir(src)
    print(f"Copying {src} items to {dst} directory...\n")
    for item in src_list:
        src_path = os.path.join(src, item)
        dst_path = os.path.join(dst, item)
        
        print(f"＊ {src_path} -> {dst_path}\n")
        if os.path.isfile(src_path):
            shutil.copy(src_path, dst_path)     
        else:
            os.mkdir(dst_path)
            copy_static(src_path, dst_path)