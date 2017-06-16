import os
import pickle

STORAGE_PATH = '/home/biswajit/Documents/'
def create_log():
    """
    Creates and stores the log in a file.
    """
    root = raw_input("Enter directory path to be logged.")
    if not os.path.exists(root):
        return False
    file_meta_data = {}
    print 'logging started'
    for path, subdir_arr, file_arr in os.walk(root):
        for file_name in file_arr:
            print 'logging ',file_name
            file_path_absolute = os.path.join(path, file_name)
            file_meta_data[file_path_absolute] = {}
            file_meta_data[file_path_absolute]['la_time'] = os.stat(file_path_absolute).st_atime
            file_meta_data[file_path_absolute]['lm_time'] = os.stat(file_path_absolute).st_mtime
    STORAGE_PATH += root.split('/')[-1]+'.py'
    f = open(STORAGE_PATH, 'wb')
    pickle.dump(file_meta_data, f)
    f.close()

def check_log():
    """
    Checks the stored log and identifies the files
    added,accessed and modified.
    """
    path = raw_input("Enter path of directory to check for log.")
    log_file = STORAGE_PATH + path.split('/')[-1]+".py"
    print log_file
    if not os.path.exists(log_file):
        print 'No log found'
        return False
    existing_log = pickle.load(open(log_file))
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
    print 'new files added'
    for file_name in new_file_arr:
        print file_name
    print '-----------------'
    print 'last accessed files'
    for file_name in accessed_file_arr:
        print file_name
    print '-----------------'
    print 'last modified files'
    for file_name in modified_file_arr:
        print file_name

def start():
    res = raw_input("Log current state of a directory? (y/n)")
    if res == 'y':
        create_log()
    else:
        check_log()

start()
