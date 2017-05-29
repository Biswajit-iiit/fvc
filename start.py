import os
import pickle

STORAGE_PATH = '/home/biswajit/Documents/log.py'
def create_log():
    # root = raw_input()
    root = '/home/biswajit/Desktop'
    if not os.path.exists(root):
        return False
    file_meta_data = {}
    for path, subdir_arr, file_arr in os.walk(root):
        for file_name in file_arr:
            file_path_absolute = os.path.join(path, file_name)
            file_meta_data[file_path_absolute] = {}
            file_meta_data[file_path_absolute]['la_time'] = os.stat(file_path_absolute).st_atime
            file_meta_data[file_path_absolute]['lm_time'] = os.stat(file_path_absolute).st_mtime
    f = open(STORAGE_PATH, 'wb')
    pickle.dump(file_meta_data, f)
    f.close()

def check_log(path):
    existing_log = pickle.load(open(STORAGE_PATH))
    current_log = {}
    current_log = {}
    for path, subdir_arr, file_arr in os.walk(path):
        for file_name in file_arr:
            file_path_absolute = os.path.join(path, file_name)
            current_log[file_path_absolute] = {}
            current_log[file_path_absolute]['la_time'] = os.stat(file_path_absolute).st_atime
            current_log[file_path_absolute]['lm_time'] = os.stat(file_path_absolute).st_mtime
    new_file_arr = []
    accessed_file_arr = []
    modified_file_arr = []
    for file_path in existing_log:
        try:
            if existing_log[file_path]['la_time'] != current_log[file_path]['la_time']:
                accessed_file_arr.append(file_path)
            if existing_log[file_path]['lm_time'] != current_log[file_path]['lm_time']:
                modified_file_arr.append(file_path)
        except KeyError:
            new_file_arr.append(file_path)
    print 42,new_file_arr
    print 43,accessed_file_arr
    print 44,modified_file_arr
            

