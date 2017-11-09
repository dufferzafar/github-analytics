import sys
import os

path = sys.argv[1]

if os.path.isdir(path):
    files = [os.path.join(path, file) for file in os.listdir(path) if os.path.isfile(os.path.join(path, file))]
else:
    files = [path]

for filename in files:
    if os.path.splitext(filename)[-1] == ".json":
        jlines = open(filename, "r")

        json_objects = ["    " + x for x in jlines.read().strip().split("\n")]
        json_objects = "[\n" + ",\n".join(json_objects) + "\n]"

        out = open(filename, "w")
        out.write(json_objects)
        out.close()
