from tkinter.font import names

from cx_Freeze import setup, Executable
import os

path = "./asset"
asset_list = os.listdir("main.py")
asset_list_completa = [os.path.join(path, asset).replace("\\", "/")for asset in asset_list]
print(asset_list_completa)

executables = [Executable("main.py")]
files = {"include_files": asset_list_completa, "packages": ["pygame"]}

setup(
    name="MountainShooter",
    version="1.0",
    descripton="Mountain Shooter app",
    options={"build.exe": files},
    executables=executables
)