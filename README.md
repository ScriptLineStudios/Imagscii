# Imagscii 📷

**A free ascii image filter API** Just upload an image and get the image back in ascii characters!

![Untitled design(2)](https://user-images.githubusercontent.com/85095943/156199496-ffe9f1ad-8a88-40aa-8e85-915332053e9f.png)

**Its your choice** -> You decide how detailed you want your images to be! Just specify a spacing between characters and the character size!

![Untitled design(3)](https://user-images.githubusercontent.com/85095943/156200670-23b6e9c1-dc36-40f2-80d6-a6daf76b1489.png)

# How to use it ❓

Sample request using Python and the ```requests``` module:
```
import requests
open("OUT_FILE.jpg", "wb").write(requests.post("https://imagscii.com/create/16/8", files={"file": open("FILE_TO_PROCESS.png", "rb")}).content)
```
The format for a request is the following:
```https://imagscii.com/create/FONT_SIZE/SPACING```
