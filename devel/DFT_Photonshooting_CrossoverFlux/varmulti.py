from Multiplevariables import main
import numpy as np
import matplotlib.pyplot as plt

# ["Gaussian", "Moffat", "Double Gaussian", "OpticalPSF", "Kolmogorov * Airy"] - PSF
# ["Gaussian", "Exponential", "Devaucouleurs", "n=2.5 Sersic", "Bulge + Disk"] - GALAXY PROFILE


sersic_n = (2, 4, 6)
FWHM_psf = (0.65, 1, 1.3)
HLR_gal = (.5, 1, 1.5)
nx_ny = (10, 25, 50)
folding_threshold = (.01, .05, .1)
maxk_threshold = (2.e-5, 2.e-3, 2.e-1)
xvalue_accuracy = (1.e-10, 1.e-6, 1.e-2)
kvalue_accuracy = (1.e-7, 1.e-4, 1.e-1)
shoot_accuracy = (1.e-5, 1.e-3, 1.e-1)
pixel_scale = (.15, .35, .55)


over, PSF, Gal, Pix, Shoot, Kvalue, Xvalue, Maxk, Folding, NxNy, FWHM, HLR, SersicN = main(sersic_n, HLR_psf, FWHM_gal, nx_ny, folding_threshold, maxk_threshold, xvalue_accuracy, kvalue_accuracy, shoot_accuracy, pixel_scale)

print (len(over))
print (len(PSF))
print (len(Gal))
print (len(Pix))
print (len(Shoot))
print (len(Kvalue))
print (len(Xvalue))
print (len(Maxk))
print (len(Folding))
print (len(NxNy))
print (len(FWHM))
print (len(HLR))
print (len(SersicN))

print (over)
print (PSF)
print (Gal)
print (Pix)
print (Shoot)
print (Kvalue)
print (Xvalue)
print (Maxk)
print (Folding)
print (NxNy)
print (FWHM)
print (HLR)
print (SersicN)
