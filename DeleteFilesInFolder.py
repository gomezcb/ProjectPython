import os, shutil

# return the current workiing directory
dir_path = os.path.dirname(os.path.realpath(__file__))

folder = '/Users/carlosgomez/Desktop/DeleteFiles/Test_Folder'
for filename in os.listdir(folder):
    file_path = os.path.join(folder, filename)
    try:
        if os.path.isfile(file_path) or os.path.islink(file_path):
            os.unlink(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)
    except Exception as e:
        print('Failed to delete %s. Reason: %s' % (file_path, e))
