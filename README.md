# CSV to Zip Converter

This Python script demonstrates how to create a CSV file and convert it to a zip file using the `zipfile` library. It also utilizes the `io` module for string input/output operations and the `pandas` library for data manipulation.

## Usage

```python
import zipfile
import io
import pandas as pd

def write(data, fname):
    t = io.StringIO(data)
    with open(fname, 'w') as f:
        for line in t:
            f.write(line)

def com(I, O):
    zf = zipfile.ZipFile(O, mode="w")
    try:
        for f in I:
            zf.write(f, f, compress_type=zipfile.ZIP_DEFLATED)
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
""", "kannada.csv")

write("""
Tmovie,rating
beast,6
varise,8
seetharamam , 10
ram,9
""", "Telegu.csv")

com(["kannada.csv", "Telegu.csv"], "Movies.zip")
print("done")
```

In this script, we define two functions: `write` and `com`. 

The `write` function takes a data string and a filename as input. It creates a CSV file with the provided data using `io.StringIO` for string input/output operations. The data is then written to the file line by line.

The `com` function takes a list of input filenames (`I`) and an output filename (`O`). It creates a new zip file using `zipfile.ZipFile` with the specified mode ("w" for write). It iterates over the input filenames, adds each file to the zip file using `write` method, and applies compression using `zipfile.ZIP_DEFLATED` compression type. Finally, it closes the zip file.

The script then calls the `write` function twice to create two CSV files: `kannada.csv` and `Telegu.csv`. The `com` function is then called with the input filenames and output filename to create a zip file named `Movies.zip`.

After the conversion is complete, the script will print "done" to indicate that the process has finished.



## Acknowledgments

Special thanks to the creators of the `zipfile` library and the `pandas` library for providing the necessary tools for file compression and data manipulation in Python.