def run_sex(image, output_catalog, mag_zero, seeing_fwhm, sex_config='hot_run.sex', param_file='default.param',
            _print=False):
    """
    Executes SExtractor to generate a single band catalog.
    :param image: 
        The path to the source image.
    :param output_catalog: 
        The path to where the output catalog will be placed.
    :param mag_zero:
        The zero point magnitude to be used by SExtractor.
    :param seeing_fwhm:
        The seeing FWHM for the image to be used by SExtractor.
    :param sex_config: 
        Name of the SExtractor configuration file. Defaults to 'default.sex'.
    :param param_file: 
        Name of the SExtractor parameter file used to sextract the image. Defaults to 'default.param'.
    :param _print:
        Boolean flag determining if the SExtractor output should be printed to the screen. Defaults to 'False'.
    :type image: str
    :type output_catalog: str
    :type mag_zero: float
    :type seeing_fwhm: float
    :type sex_config: str
    :type param_file: str
    :type _print: bool
    """

    import os
    from subprocess import Popen
    from subprocess import PIPE

    # Store the current working directory so we can return to it when completed.
    proj_cwd = os.getcwd()

    # Define locations of files in absolute paths.
    se_executable = '/Applications/Ureka/bin/sex'
    sex_config = os.path.abspath(sex_config)
    param_file = os.path.abspath(param_file)
    image = os.path.abspath(image)

    # weight = os.path.abspath(weight)
    output_catalog = os.path.abspath(output_catalog)
    output_catalog_name = os.path.basename(image).strip('.fits') + '.cat'

    # Convert the zero point magnitude and the seeing fwhm into strings
    mag_zero = str(mag_zero)
    seeing_fwhm = str(seeing_fwhm)

    # Move to the directory where the configuration files are
    os.chdir(os.path.dirname(sex_config))

    # Run the detection image in dual image mode
    s_img = Popen([se_executable, image + ',' + image, '-c', sex_config, '-PARAMETERS_NAME', param_file,
                   '-CATALOG_NAME', output_catalog + '/' + output_catalog_name, '-MAG_ZEROPOINT', mag_zero,
                   '-SEEING_FWHM', seeing_fwhm],
                  stdout=PIPE, stderr=PIPE)
    out, err = s_img.communicate()

    if _print:
        print(out, '\n', err)

    # Return to the project directory
    os.chdir(proj_cwd)

run_sex('~/Documents/CANDELS/GDS/massive_bright_gds_test/H.gf10650.fits','H.gf10650.cat', 25.9463,0.18)