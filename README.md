# SDSS Data Analysis

### Small Project by Haylam Yuen
#### If you want to use any part of this project, feel free

The top 500,000 entries of the SDSS dataset were retrieved from:
[https://skyserver.sdss.org/dr19](https://skyserver.sdss.org/dr19)

The following SQL query was used:
```
SELECT TOP 500000
p.objid,p.ra,p.dec,p.u,p.g,p.r,p.i,p.z,
p.run, p.rerun, p.camcol, p.field,
s.specobjid, s.class, s.z as redshift,
s.plate, s.mjd, s.fiberid, p.cx, p.cy, p.cz, p.type, p.flags

FROM PhotoObj AS p

JOIN SpecObj AS s ON s.bestobjid = p.objid
```
The Jupyter Notebook aims to inform the general public about somewhat modern astrophysics, and answer the question:

“What drives galaxy transformation, and can we predict where a galaxy is in its evolutionary lifecycle?”

If any mistakes or inaccuracies are noticed, please notify me.
