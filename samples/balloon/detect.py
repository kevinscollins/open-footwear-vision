import os
import openfootballoon

cmd = """
python3 balloon.py splash --dataset ../../mask_rcnn/datasets/balloon/ --weights %smask_rcnn_balloon.h5 --image party.jpg 
diff -s party_splashed.png splash_expected.png
""" % openfootballoon.datapath

print (cmd)
os.system(cmd)