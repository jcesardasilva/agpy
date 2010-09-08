import math
import read_radex

def grid_radex(radexfilename,outfile,flow,fhigh):
    """
    Use the less-hackey version of read_radex to read a radex.out file and turn it into
    a machine-readable .dat table
    """
    grid = open(outfile,'w')
    fmt  = '%10.3e %10.3e %10.3e %10.3e %10.3e %10.3e %10.3e %10.3e %10.3e %10.3e %10.3e \n'
    grid.write(fmt.replace('.3e','s') % ("Temperature","log10(dens)",
        "log10(col)","Tex_low","Tex_hi","TauLow","TauUpp","TrotLow","TrotUpp","FluxLow","FluxUpp"))

    radexfile  = open(radexfilename)

    rmin = 100
    rmax = 0.1

    while(1):
        radex_out = read_radex.read_radex(radexfile,flow,fhigh)
        if radex_out == 0:
            break
        else:
            temp,dens,col,tlow,tupp,taulow,tauupp,trotlow,trotupp,fluxlow,fluxupp = radex_out

        grid.write(fmt %(temp, math.log10(dens), math.log10(col),
            tlow, tupp, taulow, tauupp, trotlow,trotupp,fluxlow,fluxupp))

    grid.close()
    radexfile.close()
