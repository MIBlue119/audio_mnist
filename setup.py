from setuptools import setup, find_packages 
import os 
import gdown 


MAJOR = 0 
MINOR = 1
MICRO = 0 
VERSION = '{}.{}.{}'.format(MAJOR, MINOR, MICRO)

# To do : support download noise_canceller model from google drive or somewhere
def download_model(version):
    pass 


def get_requirements():
    with open('./requirements.txt','r')as f:
        reqs = f.readlines()
    return reqs 

def setup_package():
    excluded=[]
    desc = "A module for classifying audio mnist"

    metadata = dict(
        name = 'audio mnist',
        version=VERSION,
        description=desc,
        author='Weiren Lan',
        url='',
        packages=find_packages(exclude=excluded),
        install_requires=get_requirements(),
        classifiers=[
            
        ],
        python_requires='>=3.6',
        #Add some files used by the module
        # package_data={
        #     'noise_canceller':[
        #      'utils/*.md'   
        #     ]
        # }
    )
    setup(**metadata)

if __name__ == '__main__':
    setup_package()
