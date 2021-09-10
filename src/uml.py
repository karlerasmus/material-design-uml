import subprocess
from pathlib import Path
import re
from PIL import Image
import os

# to do - convert to input arguments
homePath = '/home/karl/'
materialIconsPath = 'developments/google-material-icons/material-design-icons/png/'
plantUMLjar = '/home/karl/Documents/plantuml.1.2020.18.jar'

dirPath = f"{homePath}/{materialIconsPath}"
dirList = sorted(os.listdir(dirPath))

for dir in dirList:

    fileList = sorted(Path(f"{dirPath}/{dir}").glob('**/materialicons/36dp/1x/*.png'))
    print(f"starting directory {dir}")

    spriteFile = f"{Path.cwd()}/dist/{dir}_sprites.iuml"
    with open(spriteFile, "w") as fp:    
        for file in fileList:
            m = re.search(r"_(.*)_black_\d{2}dp.png$",Path(file).name)
            if m:
                n = m.group(1)
                l = Path(file).stem
                p = Path(file).parts
                print(l)

                tmp_path = f"{Path.cwd()}/tmp/tmp.png"
                img =  Image.open(Path(file)).convert("RGBA")
                tmp_img = Image.new("RGBA", img.size, "WHITE")
                tmp_img.paste(img, mask=img)
                tmp_img.save(tmp_path)

                image_path = Path(tmp_path)
                cmd = ['java', '-Djava.awt.headless=true', 
                    '-jar', 
                    plantUMLjar,
                    '-encodesprite',
                    '16z',
                    image_path]
                output = subprocess.check_output(cmd, universal_newlines=True)
                output = output.replace(f"sprite $tmp", f"sprite ${dir}_{n}")
                #print(output)
                fp.write(output)



        




        