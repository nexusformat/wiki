---
title: Time-of-Flight Neutron Powder Diffraction
permalink: Time-of-Flight_Neutron_Powder_Diffraction/
layout: wiki
---

Items to think about
--------------------

-   TOFRaw is doing 90% of what is needed
    -   Add data\_error

<!-- -->

-   Missing items for data binning
    -   time\_focusing\_type (e.g. difc, cubic, ..)
    -   time\_focusing\_parameters \[ndetector,nparameters\]
    -   Deadtime correction information (in combination with gang\_..)

<!-- -->

-   Missing items for Rietveld refinement
    -   Profile types and starting parameters
    -   Incident spectrum (parameters or run in NXcharacterization)

<!-- -->

-   Other
    -   Binned data back in NeXus - this actually is used in Rietveld.

Old definition
--------------

    <?xml version="1.0" encoding="UTF-8"?>
    <!--
    URL:     http://www.neutron.anl.gov/nexus/xml/NXtofnpd.xml
    Editor:  Peter Peterson <PFPeterson@anl.gov>
    $Id$

    Instrument definition for a time-of-flight neutron powder diffractometer.

    -->
    <NXentry name="{Entry Name}">

       <title type="NX_CHAR[]">{Extended title for entry}</title>
       <definition type="NX_CHAR[]" version="$Revision$" URL="http://www.neutron.anl.gov/nexus/xml/NXtofnpd.xml">TOFNPD</definition>
       <start_time type="ISO8601">{Starting time of measurement}</start_time>
       <end_time type="ISO8601">{Ending time of measurement}</end_time>

       <NXinstrument name="{name of the instrument}">
          <name short_name="{abbreviated name of instrument}" type="NX_CHAR[]">{Name of instrument}</name>
          <NXsource name="source">
             <distance type="NX_FLOAT" units="meter">{distance from the sample (should be negative)}</distance>
          </NXsource>

          <NXdetector name="{Name of detector bank}">+
             <time_of_flight type="NX_FLOAT[j+1]"
                      axis="1" primary="1?"
                      long_name="{Axis label}"
                          units="10^-6 second|10^-7 second" link="{absolute path to location in NXdetector}">
                  {Total time of flight}</time_of_flight>
             <detector_number type="NX_INT[i]" axis="2" primary="1?" long_name="{Axis
                           label}" link="{absolute path to location in NXdetector}">{Identifier for detector}?</detector_number>
             <data type="NX_FLOAT[i,j,k?,l?]|NX_INT[i,j,k?,l?]" signal="1" axes="[time_of_flight,detector_number,x_offset?,y_offset?]?" long_name="{Title of measurement}?"
                      check_sum="{Integral of data as check of data
                integrity} (NX_INT)?" units="number"  link="{absolute path to location in NXdetector}">
                  {Data values}</data>
             <data_error type="NX_FLOAT[i,j,k?,l?]|NX_INT[i,j,k?,l?]" units="number"  link="{absolute path to location in NXdetector}">
                  {Data values}</data_error>
             <x_offset axis="3" primary="1?" type="NX_FLOAT[k+1]" units="10^-3
    meter|10^-2 meter" long_name="{Axis label}"  link="{absolute path to location in NXdetector}">{offset from the
    detector center in x-direction}?</x_offset>
             <y_offset axis="4" primary="1?" type="NX_FLOAT[l+1]" units="10^-3
    meter|10^-2 meter" long_name="{Axis label}"  link="{absolute path to location in NXdetector}">{offset from the
    detector center in the y-direction}?</y_offset>
         <distance type="NX_FLOAT[j,k?,l?]" axes="detector_number,x_offset?,y_offset?"></distance>
             <polar_angle type="NX_FLOAT[j,k?,l?]" axes="detector_number,x_offset?,y_offset?"></polar_angle>
             <azimuthal_angle type="NX_FLOAT[j,k?,l?]" axes="detector_number,x_offset?,y_offset?"></azimuthal_angle>
          </NXdetector>
       </NXinstrument>

       <NXmonitor name="{name of the monitor}">*
          <distance type="NX_FLOAT" units="meter"></distance>
          <time_of_flight type="NX_FLOAT[i]|NX_INT[i]" units="10^-6 second|10^-7 second"></time_of_flight>
          <data type="NX_FLOAT[i]|NX_INT[i]" units="number"></data>
          <data_error type="NX_FLOAT[i]|NX_INT[i]" units="number">?</data_error>
       </NXmonitor>

       <NXdata name="">+
          <time_of_flight type="NX_FLOAT[j+1]"
                      axis="1" primary="1?"
                      long_name="{Axis label}"
                          units="10^-6 second|10^-7 second" link="{absolute path to location in NXdetector}">
                  {Total time of flight}</time_of_flight>
          <detector_number type="NX_INT[i]" axis="2" primary="1?" long_name="{Axis
                           label}" link="{absolute path to location in NXdetector}">{Identifier for detector}?</detector_number>
          <data type="NX_FLOAT[i,j,k?,l?]|NX_INT[i,j,k?,l?]" signal="1" axes="[time_of_flight,detector_number,x_offset?,y_offset?]?" long_name="{Title of measurement}?"
                      check_sum="{Integral of data as check of data
                integrity} (NX_INT)?" units="number"  link="{absolute path to location in NXdetector}">
                  {Data values}</data>
          <data_error type="NX_FLOAT[i,j,k?,l?]|NX_INT[i,j,k?,l?]" units="number"  link="{absolute path to location in NXdetector}">
                  {Data values}</data_error>
          <x_offset axis="3" primary="1?" type="NX_FLOAT[k+1]" units="10^-3
    meter|10^-2 meter" long_name="{Axis label}"  link="{absolute path to location in NXdetector}">{offset from the
    detector center in x-direction}?</x_offset>
          <y_offset axis="4" primary="1?" type="NX_FLOAT[l+1]" units="10^-3
    meter|10^-2 meter" long_name="{Axis label}"  link="{absolute path to location in NXdetector}">{offset from the
    detector center in the y-direction}?</y_offset>
       </NXdata>

    </NXentry>
