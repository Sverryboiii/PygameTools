import sys, os, pygame
from pathlib import Path

base_path = Path(__file__).resolve().parent
def spk_resource_path(relative_path: str) -> str:
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, f"../{relative_path}")
    return os.path.join(base_path, f"../{relative_path}")

src_path = ""
def resource_path(relative_path: str) -> str:
    if not os.path.exists(src_path):
        raise TypeError(f"Please set the src path before you run this function!")
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, f"{relative_path}")
    return os.path.join(src_path, f"{relative_path}")