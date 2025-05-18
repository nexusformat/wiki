---
title: GenericScan
permalink: GenericScan.html
layout: wiki
---
GenericScan
===========

Generic Scan Instrument
-----------------------

This is a DTD for an example generic instrument which performs scans.
This example is for an omega-two-theta (rotation\_angle polar\_angle in
NeXus notation) scan and serves to highlight NeXus scan data storage
principles:

-   Assume np to be the number of scan points
-   Variable data (such as motors) which can vary during the scan are
    stored as arrays of length np at their proper place in the
    NXinstrument hierarchy.
-   In NXdata links to all varied positions and the dectector counts are
    created. This provides for easy access to the popular table format
    for scans.
-   In the case of multi dimensional detectors, the PSD data must be
    stored with the scan variable being the fastest varying
    dimension(the first) for technical reasons.
-   If you to choose to store PSD scans in separate files or separate
    entries, it is the users responsibility to process the data in the
    right order.

<!-- -->

    <?xml version="1.0" ?>
    <!--
    URL: http://www.neutron.anl.gov/nexus/xml/NXscan.xml
    Editor: Mark Koennecke
    Version: October 2006

    Instrument Definition example for a simple two axis scan. This example is for 
    an omega-two-theta (rotation_angle polar_angle in NeXus notation)
    scan and serves to highlight NeXus scan data storage principles:
    - Assume np to be the number of scan points 
    - Variable data (such as motors) which can vary during the scan are stored as arrays of length np at 
      their proper place in the NXinstrument hierarchy.
    - In NXdata links to all varied positions and the dectector counts are created. This
      provides for easy access to the popular table format for scans. 
    - In the case of multi dimensional detectors, the PSD data must be stored with the scan 
      variable being the fastest varying dimension(the first) for technical reasons.
    - If you to choose to store PSD scans in separate files or separate entries, it is the users
      responsibility to process the data in the right order.  

    Note:
    This example is fairly minimal. Feel free to add whatever you think necessary. However, if
    items are missing which are required for standard data reduction tasks, please consult the
    editor of this example.

    -->

    <NXroot>
       <NXentry name="{Entry name}">+
            <title>{Extended title for entry}</title>
            <NXsample name="{sample}">
                <name>{Descriptive name of sample}</name>
                <environment>{Type of sample environment}</environment>
                <polar_angle type="NX_FLOAT32[np]">
                   {polar_angle to monochromator}
                </polar_angle>
                <rotation_angle type="NX_FLOAT32[np]">
                   { sample rotation}
                </rotation_angle>
            </NXsample>
            <NXinstrument name="{name}">
                <name>{name of instrument}</name>
                <NXsource name="{name}">
                    <name>{name of facility}</name>

                    <type>"Reactor"</type>
                    <power units="MW" type="NX_FLOAT32">{reactor power}</power>
                </NXsource>
                <NXcrystal name="monochromator">
                    <wavelength units="Angstrom" type="NX_FLOAT32[np]">
                      {wavelength at each scan position}
                    </wavelength>
                </NXcrystal>
                <NXdetector name="primary">
                  <data type="NX_INT32[np]" signal="1">
                    {Detector counts for each scan position}
                  </data>
                  <polar_angle type="NX_FLOAT32[np]" axis="1">
                     {polar angle for each scan position}
                  </polar_angle>
                </NXdetector>
            </NXinstrument>
            <NXmonitor name="control">
               <mode type="NX_CHAR">monitor | timer</mode>
               <preset type="NX_FLOAT32">
                  {preset value for monitor or timer}
                </preset>
                <data type="NX_INT32[np]">
                   {Monitor counts for each scan position}
                </data>
            </NXmonitor>
            <NXdata name="{data}">
                <data type="NX_INT32[np]" signal="1">
                  {Link to detector counts}
                </data>
                <polar_angle axis="1" primary="2">
                  {Link to detector polar_angle}
               </polar_angle>
               <rotation_angle axis="1" primary="1">
                  {Link to sample rotation_angle}
               </rotation_angle>
            </NXdata>
        </NXentry>
    </NXroot>
