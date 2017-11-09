import sys

filename = sys.argv[1]
jlines = open(filename, "r")

json_objects = "[\n" + ",\n".join(jlines.read().strip().split("\n")) + "]"

out = open(filename, "w")
out.write(json_objects)
out.close()
