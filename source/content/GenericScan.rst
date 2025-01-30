===========
GenericScan
===========

Generic Scan Instrument
-----------------------
This is a DTD for an example generic instrument which performs scans.
This example is for an omega-two-theta (rotation_angle polar_angle
in NeXus notation) scan and serves to highlight NeXus scan data storage
principles:

- Assume np to be the number of scan points
- Variable data (such as motors) which can vary during the scan are stored as arrays of length np at their proper place in the NXinstrument hierarchy.
- In NXdata links to all varied positions and the dectector counts are created.

This provides for easy access to the popular table format for scans.
- In the case of multi dimensional detectors, the PSD data must be stored with the scan variable being the fastest varying dimension(the first) for technical reasons.
- If you to choose to store PSD scans in separate files or separate entries, it is the users responsibility to process the data in the right order.

.. code-block:: xml

   {Extended title for entry}
   {Descriptive name of sample}
   {Type of sample environment}
   {polar_angle to monochromator}
   {sample rotation}
   {name of instrument}
   {name of facility}
   "Reactor"
   {reactor power}
   {wavelength at each scan position}
   {Detector counts for each scan position}
   {polar angle for each scan position}
   monitor |
   timer
   {preset value for monitor or timer}
   {Monitor counts for each scan position}
   {Link to detector counts}
   {Link to detector polar_angle}
   {Link to sample rotation_angle}