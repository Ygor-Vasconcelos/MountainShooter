from tkinter.font import names

from cx_Freeze import setup, Executable
import os

path = "./asset"
asset_list = os.listdir(path)
asset_list_completa = [os.path.join(path, asset).replace("\\", "/") for asset in asset_list]
print(asset_list_completa)

executables = [Executable("main.py")]
files = {"include _files": asset_list_completa, "packages": ["pygame"]}

setup(
    names="MoutainShooter",
    version="1.0",
    description="Mountain Shoter app",
    options={"build_exe": files},
    executables=executables
)
