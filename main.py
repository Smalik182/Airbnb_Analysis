import patoolib
import os


# The file needed to be extracted from a gz to a csv

# Location
os.chdir(r"C:\Users\MalikSami\Desktop\Data_Analytics\Python_Projects\Airbnb")

# Print contents
print(os.listdir())

# Extraction
patoolib.extract_archive(r"listings.csv.gz", outdir = r"C:\Users\MalikSami\Desktop\Data_Analytics\Python_Projects\Airbnb")
