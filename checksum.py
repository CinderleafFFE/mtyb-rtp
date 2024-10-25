import os
import hashlib
assets_dirs = ["Graphics", "Audio"]
with open("assets_sum.txt", "w") as sum_file:
    os.chdir("assets")
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
                sum_file.write('"' + fname + '"' + ' ' + md5 + '\n')
