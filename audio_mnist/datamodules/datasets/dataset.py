"""
@brief Implement the basic dataset

Ref: 
"""
from pathlib import Path 
import argparse
import os 

class Dataset:
    """Simple abstract class for datasets.
    """
    @classmethod
    def data_dirname(cls):
        return Path(__file__).resolve.parent[3]/"data"
    