========================================
Update for NXflou application definition
========================================


.. container:: content

   .. container:: page

      .. rubric:: Update for NXflou application definition
         :name: update-for-nxflou-application-definition
         :class: page-title

      .. rubric:: Problem
         :name: problem

      In todays fluorescence experiments users often raster the sample
      with the beam and record a single spectrum at each sample
      location. For beamline P06 at DESY this procedure became virtually
      the default mode of operation. The current NXfluo application
      definition does not include this kind of experiments as it only
      allows to store a single spectrum below
      /:NXentry/:NXinstrument/:NXdetector. However NXfluo could be
      easily modified to accommodate raster scans.

      .. rubric:: Proposed modification
         :name: proposed-modification

      The changes concern only the NXdetector instance of NXfluo. The
      layout should be changed as follows

      .. container:: language-plaintext highlighter-rouge

         entry:NXentry
            instrument:NXinstrument
               flourescence:NXdetector
                  data[npts,nenergy]
                  energy[npts,nenergy]

      where npts denotes the number of raster points. It is important to
      note that we do not care about the particular pattern used to
      raster the sample. This would be hard to achieve taking into
      account that there is a nearly arbitrary number of patterns
      available. Even entirely irregular paths would be possible (and
      have already been requested by one of the beamline scientists here
      at DESY). One advantage of this pattern agnostic approach would be
      that analysis software can stick to its current workflow:
      processing the spectra recorded during an experiment in a simple
      sequential order.

      If the energy dataset is of shape [nenergy] (rank one) we can
      assume that the energy range was the same for each point recorded.
      A single spectrum can easily be stored by using the original
      schema of the definition which could be interpreted as ntps=0.

      Just as a recommendation (must not go into the standard), it would
      make sense to store the position of the beam on the sample like
      this

      .. container:: language-plaintext highlighter-rouge

         entry:NXentry
            sample:NXsample
               x[npts]:NX_FLOAT
               y[npts]:NX_FLOAT

      .. rubric:: Status 01/2015
         :name: status-012015

      The suggested change is in line with NeXus scan rules. Thus the
      change was accepted at NIAC 2014. No vote was necessary.
