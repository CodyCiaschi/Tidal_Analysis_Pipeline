
def make_cutouts(imagename, catalog):
    import numpy as np
    from astropy.nddata import Cutout2D
    from astropy.io import fits
    import astropy.wcs as wcs

    #read in csv catalog.
    raw_data = np.genfromtxt(catalog, dtype = None, names = True, delimiter = ',')

    #read in the total fits image.
    fits_image = fits.open(imagename, memmap = True)

    #get the world coordinate system from the fits image header.
    image_wcs = wcs.WCS(imagename)

    for each in raw_data:
        #may implement any cuts to data that are deemed necessary
        if each['PhotFlag'] == 0 and each['Hmag'] < 24.5:

            ra = each['RAdeg']
            dec = each['DECdeg']

            #convert the objects coordinates from wcs degrees to pixels. 0  is to set the order or the image will be 1 pixel off.
            x, y = image_wcs.wcs_world2pix(ra,dec,0)

            #make cutout of image around object at x,y with a box of 100,100 pixels
            cutout = Cutout2D(fits_image[0].data, (x, y), (100, 100), image_wcs)

            #save image to file. Will create way to save it to a certain directory
            cutout_name = 'uds_F160_%s.fits'%(each['ID'])
            fits.writeto('/Users/cpcyr8/Documents/CANDELS/UDS/cutouts/' + cutout_name, cutout.data, cutout.wcs.to_header())

    return
