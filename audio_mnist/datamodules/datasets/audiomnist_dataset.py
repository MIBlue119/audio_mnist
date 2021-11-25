"""
@brief AudioMNIST dataset. Download from https://github.com/soerenab/AudioMNIST
"""

##################################
# import python library          #
##################################

##################################
# import self-defined library    #
##################################
from audio_mnist.datamodules.datasets import Dataset 

##################################
# config                         #
##################################

##################################
# def                            #
##################################

class AudioMnistDataset(Dataset):
    """The AudioMnist Dataset is a set of 60 speakers to speak 1~10.
       It equips 30,000 wav files. Every speaker spoke 500 utterance and spoke a number with 50 times.
       The original source: https://github.com/soerenab/AudioMNIST
       - The folder structure of the dataset
        <data>
          ├── 01                       # <speaker_id> as the directory name 
            ├── 0_01_0.wav             # <number>_<speaker_id>_<utterence_id>.wav
            ├── 0_01_1.wav
                    :
            ├── 0_01_48.wav
            ├── 0_01_49.wav
            ├── 1_01_0.wav
            ├── 1_01_1.wav
                    :

          ├── 02
          ├── 03
               :
          ├── 58
          ├── 59
          └── 60

       It also contains metadata about every speakers like accent/age/gender/whether is native speaker/origin/recording area/recording time
       - meta_data: https://github.com/soerenab/AudioMNIST/blob/master/data/audioMNIST_meta.txt 
       - Example of the metadata:
        { "01": {
                "accent": "german", 
                "age": 30, 
                "gender": "male", 
                "native speaker": "no", 
                "origin": "Europe, Germany, Wuerzburg", 
                "recordingdate": "17-06-22-11-04-28", 
                "recordingroom": "Kino"
                    },
        } 
    """