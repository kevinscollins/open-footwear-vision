import os

print ("installing requirements")
os.system("pip install -r requirements1.txt")
os.system("pip install -r requirements2.txt")

if input("install tensorflow-gpu?").lower()[:1] == 'y':
    os.system("pip install -r tensorflow_gpu.txt")

if input("install available trained model: openfootballoon (245 Mbyte)?").lower()[:1] == 'y':
    os.system("pip install -r models.txt")

if input("run test?").lower()[:1] == 'y':
    os.chdir("samples/balloon")
    os.system("python detect.py")
