"""
This script causes segmentation fault error
"""

import ctypes

if __name__ == '__main__':
    ctypes.string_at(0)
