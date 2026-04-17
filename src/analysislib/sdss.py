# Import necessary libraries
import numpy as np
from scipy.integrate import quad

# Define setup function to clean and prepare the data
def setup(df):
    df = df[df["zWarning"] == 0] # Set the dataframe to only include instances where zWarning was 0

    photometry_bands = ["u", "g", "r", "i", "z"] # Define a list of all the photometry bands

    # Loop through every passband and check if the value is OK
    for band in photometry_bands:
        df = df[df[band] > 0]

    # Separate dataframe
    global galaxies
    global galaxies_extended
    global galaxies_full
    global stars
    global qsos
    
    galaxies = df[df["class"] == "GALAXY"]
    stars = df[df["class"] == "STAR"]
    qsos = df[df["class"] == "QSO"]

    # Remove galaxies with zero or negative values
    galaxies = galaxies[(galaxies["petroRad_r"] > 0) & (galaxies["fracDeV_r"] > 0)]

    # Add additional columns for galaxies
    galaxies_extended = galaxies.copy()
    galaxies_extended["g_r"] = galaxies_extended["g"] - galaxies_extended["r"]
    galaxies_extended["C"]   = 5 * np.log10(np.abs(galaxies_extended["petroR90_r"] / galaxies_extended["petroR50_r"]))

    # Add derived physical quantities for galaxies
    galaxies_full = galaxies_extended.copy()
    galaxy_z = galaxies["redshift"] # Extract redshift values
    galaxies_full["d_L_mpc"] = d_L_mpc(galaxy_z.values) # Compute luminosity distance for each galaxy
    galaxies_full["d_L_pc"] = galaxies_full["d_L_mpc"] * 1e6 # Convert Mpc to parsecs
    galaxies_full["mu"] = 5 * np.log10(np.abs(galaxies_full["d_L_pc"] / 10)) # Distance modulus
    galaxies_full["M_r"] = galaxies_full["r"] - galaxies_full["mu"] # Absolute magnitude in r-band
    galaxies_full["d_L_mly"] = galaxies_full["d_L_mpc"] * 3.2616 # Convert Mpc to million light-years

    # Drop unnecessary columns
    stars = stars.drop(columns=["petroRad_r",  "petroR50_r", "petroR90_r", "petroMag_r", "fracDeV_r", "expAB_r", "deVAB_r"])
    qsos = qsos.drop(columns=["petroRad_r", "petroR50_r", "petroR90_r", "petroMag_r", "fracDeV_r", "expAB_r", "deVAB_r"])

# Return the four dataframes
def _galaxies():
    return galaxies

def _galaxies_extended():
    return galaxies_extended

def _galaxies_full():
    return galaxies_full

def _stars():
    return stars

def _qsos():
    return qsos

H0, Om, OL, c_kms = 70.0, 0.3, 0.7, 2.998e5

def E(z): # dimensionless Hubble parameter
    return np.sqrt(Om*(1+z)**3 + OL)

def d_L_mpc(z): # Luminosity distance in Mpc
    if np.isscalar(z): # Check if z is a single value or an array
        dc, _ = quad(lambda zp: 1/E(zp), 0, z) # Comoving distance integral
        return c_kms/H0 * dc * (1+z) # Convert to luminosity distance
    return np.array([d_L_mpc(zi) for zi in z]) # Handle array input by applying the function element-wise
