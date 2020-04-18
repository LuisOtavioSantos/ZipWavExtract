import zipfile, fnmatch, os

# This code extracts wavs audio files from a dataseth path
DATASET_PATH = "/home/path/.../DATABASE_folder"
PATH_TO_EXCRACT = "/home/path/.../PATH_TO_EXTRACT"
PATTERN_1 = "*.zip"
PATTERN_2 = ".wav"

# This function does booth comands, its search for zip files and extract it to a specific folder
# The user could use it to unpack his dataset into a specific folder
def find_extract(zipPath, toFolder):
    for root, dirs, files in os.walk(zipPath):
        for filename in fnmatch.filter(files, PATTERN_1):
            print('Found {}'.format(filename))
            print(os.path.join(root, filename))
            with zipfile.ZipFile(os.path.join(root, filename), mode='r') as zipObj:
                for wavfile in zipObj.namelist():
                    if wavfile.endswith(PATTERN_2):
                        print('Extracting ' + wavfile + ' to: ' + toFolder)
                        zipObj.extract(wavfile, toFolder)

# This function does just the search for a zip file
def find_zip(zipPath):
        for root, dirs, files in os.walk(zipPath):
            for filename in fnmatch.filter(files, PATTERN_1):
                print('Found {}'.format(filename))
                print(os.path.join(root,filename))
                extract_wav((DATASET_PATH+'/'+filenames),PATH_TO_EXCRACT)

# This Function does the extraction, if you want just one wav file from a zip
def extract_wav(zipPath, toFolder):
    with zipfile.ZipFile(zipPath, mode='r') as zipObj:
        for filename in zipObj.namelist():
            if filename.endswith(PATTERN_2):
                print('Extracting ' + filename + ' to: ' + toFolder)
                zipObj.extract(filename, toFolder)





if __name__ == "__main__":
    print('Start')
    find_extract(DATASET_PATH, PATH_TO_EXCRACT)
    print('Done!')
