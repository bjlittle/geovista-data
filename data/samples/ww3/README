Example unstructured grid files from WAVEWATCH III surface wave model
=====================================================================

The example unstructured grid WAVEWATCH III (WW3) files are formulated
on two different kind of grid:

 - Spherical Multi Cell (SMC) grid
   ===============================
   A quasi-unstructured grid based on an underlying regular grid layout.
   Each grid cell can be split into 4 smaller equal sized cells. This
   process can be performed multiple times to increase resolution by a
   factor of two each time.

   The netCDF file contains the following grid variables defined on a 1D
   "seapoint" dimension:
     - latitude, longitude: the grid cell centres
	 - cx, cy: the integer scaling factor for the cell x/y size

   In addition, the following global attributes are used:
     - base_lon_size, base_lat_size: the smallest grid cell sizes.

   To calculate the bounds of each cell:

      x1, x0 = longitude +/- cx * base_lon_size * 0.5
      y1, y0 =  latitude +/- cy * base_lat_size * 0.5

   Diagnostic variables are defined on the 1D seapoint grid.

 - Unstructured triangular mesh
   ============================
   A traditional unstructured triangular mesh defined as a sequence of
   nodes with connectivity.

   The netCDF file contains the following grid variables
     - latitude, longitude; [dim=node]: The lat/lons of the triangular
	   mesh unique node points.
	 - tri [dims=3,element]: the index of the lat/lon values that form
	   the vertices of each triangular cell. NB: index is fortran 1-indexed.

   Diagnostic variables are defined on the "node" dimension.


The following example files are provided:

  - ww3_gbl_smc_hs.nc
    Significant wave height (7 times) from the Met Office's Global SMC model.

  - ww3_gbl_tri_hs.nc (NOAA, 2019; Brus et al, 2020)
    Sig. wave height (1 time) from an unstructred global triangular mesh
	example. Part of the official WW3 regression test suite (ww3_tp2.21)


Refs:
=====

The WAVEWATCH III® Development Group (WW3DG), 2019: User manual and system documentation of WAVEWATCH III® version 6.07. Tech. Note 333, NOAA/NWS/NCEP/MMAB, College Park, MD, USA, 326 pp. + Appendices.

Brus, Steven, Wolfram, Phillip, & Van Roekel, Luke. (2020). Unstructured global to coastal wave modeling for the Energy Exascale Earth System Model - unstructured (2 degree to 1/2 degree) WaveWatchIII configuration files (1.0.0) [Data set]. Zenodo. https://doi.org/10.5281/zenodo.4088520
