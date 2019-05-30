import os
import os.path

# dataset directory parallel to this module's directory
DATASETS_PATH = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'datasets'))


def find_files(path, ext='.txt'):
    """Recursively find all files of given type from given root path."""
    files = []
    # r=root, d=directories, f = files
    for r, d, f in os.walk(path):
        for file in f:
            if ext in file:
                files.append(os.path.join(r, file))
    return files


def acl_arc_files():
    """Returns list of all the file paths for the ACL corpus."""
    acl_txt_dir = os.path.join(DATASETS_PATH, 'acl-arc', 'txt', 'pdfbox-0.72')
    acl_txt_files = find_files(acl_txt_dir)
    return acl_txt_files
