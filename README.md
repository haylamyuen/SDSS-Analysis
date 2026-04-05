# SDSS Data Analysis

### This is a Small Project by Haylam Yuen

<span style="color: #AAAAAA">If you want to use any part of this project, feel free</span>

<br>

In this project, the Sloan Digital Sky Survey (SDSS) was used, and the top 500,000 entries of the dataset were retrieved from:
[https://skyserver.sdss.org/CasJobs/SubmitJob.aspx](https://skyserver.sdss.org/CasJobs/SubmitJob.aspx)

The following SQL query was used:
```
SELECT TOP 500000
p.objid,p.ra,p.dec,p.u,p.g,p.r,p.i,p.z,
s.class, s.zWarning, s.z as redshift,
p.petroRad_r, p.petroMag_r,
p.expRad_r, p.deVRad_r, p.fracDeV_r, p.expAB_r, p.deVAB_r

FROM PhotoObj AS p

JOIN SpecObj AS s ON s.bestobjid = p.objid
```

The Jupyter Notebook aims to inform the general public about somewhat modern astrophysics through being the base for a Science Museum exhibition, and answer the question:

   *“What drives galaxy transformation, and can we predict where a galaxy is in its evolutionary lifecycle?”*

<br>

If any mistakes or inaccuracies are noticed, please notify me.
