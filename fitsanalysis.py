import os

root_dir = os.path.dirname(os.path.abspath(__file__))

raw_dir = os.path.join(root_dir, 'data', 'raw', 'NGC1856_CENTER_P01')

print(raw_dir)


# from astropy.io import fits

# filename1 = 'data/MUSE_LMC/NGC1856_id000022990jd2458548p5363f002.fits'
# filename2 = 'data/MUSE_LMC/NGC1856_id000023541jd2458548p5363f002.fits'
# with fits.open(filename1) as hdul:
#     header = hdul[0].header
#     print(header)

# with fits.open(filename2) as hdul:
#     header = hdul[0].header
#     print(header)