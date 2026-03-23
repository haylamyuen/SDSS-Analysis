import pandas as pd

df = pd.read_csv("SDSS_500k_v3.csv")

df = df[df["zWarning"] == 0] # Set the dataframe to only include instances where zWarning was 0

photometry_bands = ["u", "g", "r", "i", "z"] # Define a list of all the photometry bands

# Loop through every passband and check if the value is OK
for band in photometry_bands:
    df = df[df[band] > 0]

galaxies = df[df["class"] == "GALAXY"]
stars = df[df["class"] == "STAR"]
qsos = df[df["class"] == "QSO"]

galaxies = galaxies[(galaxies["petroRad_r"] > 0) & (galaxies["fracDeV_r"] > 0)]

def _galaxies():
    return galaxies

def _stars():
    return stars

def _qsos():
    return qsos
