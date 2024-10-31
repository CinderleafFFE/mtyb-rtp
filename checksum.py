import os
import hashlib
import json
assets_dirs = ["Graphics", "Audio"]
os.chdir("assets")
md5_dict = {}
for assets_dir in assets_dirs:
    for root, dirs, files in os.walk(assets_dir):
        for name in files:
            fname = os.path.join(root, name)
            hasher = hashlib.md5()
            with open(fname, 'rb') as ass:
                while True:
                    data = ass.read(4096)
                    if len(data) == 0:
                        break
                    hasher.update(data)
            md5 = hasher.hexdigest()
            md5_dict.update({fname : md5})
os.chdir("..")
fp = open("assets_sum.json", "w")
json.dump(md5_dict, fp)
fp.close()