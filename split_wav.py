import os
import librosa
import zipfile
import soundfile as sf
import io
import numpy as np
import math


ZIP_PATH = '/home/path/.../file.zip'
SPLIT_PATH = '/home/path/.../splited_files/'
PATTERN1 = '.wav
final_wav = []

def read_n_split_wav(zipPath, start_time, stop_time):
    with zipfile.ZipFile(zipPath, mode='r') as zipObj:
        for somefile in zipObj.namelist():
            if somefile.endswith(PATTERN1):
                with zipObj.open(somefile) as myWav:
                    tmp = io.BytesIO(myWav.read())
                    signal, sample_rate = sf.read(tmp) # not resampled at 22050 Hz it is in original sample rate
                    check1 = int(float(start_time*sample_rate))
                    check2 = int(float(stop_time*sample_rate))
                    for t, samples in enumerate(signal):
                        if (t >= check1) and (t <= check2):
                            final_wav.append(samples)

                    sf.write((SPLIT_PATH + myWav.name), final_wav, sample_rate)
                    # sf.write((SPLIT_PATH + myWav.name), signal[int(start_time):int(stop_time)], sample_rate)
if __name__ == "__main__":
    read_n_split_wav(ZIP_PATH,36.588,39.668)
    print('Done')
