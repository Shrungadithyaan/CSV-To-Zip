#for it helps to create a csv file and convert to zip

import zipfile, io , pandas as pd

def write (data , fname):
    t = io.StringIO(data)
    with open(fname,'w') as f:
        for line in t:
            f.write(line)

def com(I, O):
    zf = zipfile.ZipFile(O, mode="w")
    try:
        for f in I:
            zf.write(f,f, compress_type=zipfile.ZIP_DEFLATED)
    except FileExistsError as e:
        print("Exception occurred")
    finally:
        zf.close()

write("""
kmovie,rating
KGF,9
RRR,8
kantara , 10
777charly,9
""","kannada.csv")

write("""
Tmovie,rating
beast,6
varise,8
seetharamam , 10
ram,9
""","Telegu.csv")

com(["kannada.csv","Telegu.csv"], "Movies.zip")
print("done")