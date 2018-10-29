import numpy as np 
import sys
import json
import os
from scipy.io import wavfile
from pymediainfo import MediaInfo

class AiqtUtil:
    def __init__(self):
        pass
    def splitChannel(self,scrMusicFile,tempDir):
        sampleRate,musicData = wavfile.read(scrMusicFile)
        left = []
        right = []
        for item in musicData:
            left.append(item[0])
            right.append(item[1])
        os.makedirs(str(tempDir)+'/'+scrMusicFile.split('/')[-1].split('.')[0])
        wavfile.write(str(tempDir)+'/'+scrMusicFile.split('/')[-1].split('.')[0]+'/left.wav',sampleRate,np.array(left))
        wavfile.write(str(tempDir)+'/'+scrMusicFile.split('/')[-1].split('.')[0]+'/right.wav',sampleRate,np.array(right))
    def getMediaInfo(self,scrMusicFile):
        meida_info = MediaInfo.parse(scrMusicFile)
        json_info = meida_info.to_json()
        hjson  = json.loads(json_info)
        dur_time = hjson['tracks'][0]['other_duration'][-1]
        print(dur_time)

if __name__ == '__main__':
    util  =AiqtUtil()
    if sys.argv[1] == 'split' :
        util.splitChannel(sys.argv[2],sys.argv[3])
        
    if sys.argv[1] == 'getMediaInfo' :
        util.getMediaInfo(sys.argv[2])
# print(util.getMediaInfo('d:/135600000000120181008122243.wav'))
