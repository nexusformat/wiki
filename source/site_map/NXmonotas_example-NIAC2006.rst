==========================
NXmonotas example-NIAC2006
==========================

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8"?>
    <!--
    URL:     http://www.nexus.anl.gov/classes/xml/NXmononxtas.xml
    Editor:  NIAC
    NIAC Version: 0.80
    Date: 27 Apr 2005
    $Id$

    Template of a generic NeXus file containing neutron or x-ray triple-axis data.

    -->
    <NXroot filename="NXmononxtas_example.xml">

     <NXentry name="entry_0">
      <title> La1.2Sr1.8Mn2O7 m=2.4g phonons </title>
      <definition version="1.0" URL="http://www.nexus.anl.gov/instruments/xml/NXmononxtas.xml">
       NXmononxtas
      </definition>
      <start_time type="ISO8601">
       2000-05-23T19:37
      </start_time>
      <end_time type="ISO8601">
       2000-05-23T21:04
      </end_time>
      <duration type="NX_INT32" units="seconds">
       1620
      </duration>
      <command_line>
       sc en 2.0 den 0.25 np 21 mn 1013000
      </command_line>
      <NXuser name="Stephan Rosenkranz">
       <name type="NX_CHAR">
        Stephan Rosenkranz
       </name>
       <affiliation type="NX_CHAR">
        Argonne National Laboratory
       </affiliation>
      </NXuser>

      <NXsample name="sample">
       <name type="NX_CHAR">
        Bilayer Manganite
       </name>
       <unit_cell type="NX_FLOAT32[1,6])">
        3.874 3.874 20.145 90.000 90.000 90.000
       </unit_cell>
       <plane_vector_0 type="NX_FLOAT32[3]">
        -1.0 0.0 0.0
       </plane_vector_0>
       <plane_vector_1 type="NX_FLOAT32[3]">
        0.0 0.0 1.0
       </plane_vector_1>
       <temperature type="NX_FLOAT32[21]" units="K">
        295.2380 295.2360 295.2350 295.2320 295.2310 295.2290
        295.2270 295.2260 295.2250 295.2230 295.2220 295.2200
        295.2190 295.2180 295.2180 295.2170 295.2160 295.2160
        295.2150 295.2150 295.2150
       </temperature>
       <polar_angle type="NX_FLOAT32[21]" units="degrees">
        41.172 41.172 41.172 41.172 41.172 41.172 41.172 41.172
        41.172 41.172 41.172 41.172 41.172 41.172 41.172 41.172
        41.172 41.172 41.172 41.172 41.172
       </polar_angle>
       <rotation_angle type="NX_FLOAT32[21]" units="degrees">
        218.439 218.976 219.518 220.065 220.617 221.174 221.736
        222.304 222.878 223.458 224.044 224.637 225.236 225.843
        226.457 227.080 227.710 228.349 228.998 229.656 230.324
       </rotation_angle>
       <azimuthal_angle type="NX_FLOAT32" units="degrees">
        180.0
       </azimuthal_angle>
       <Qh type="NX_FLOAT32[21]">
        2.0000 2.0000 2.0000 2.0000 2.0000 2.0000 2.0000 2.0000
        2.0000 2.0000 2.0000 2.0000 2.0000 2.0000 2.0000 2.0000
        2.0000 2.0000 2.0000 2.0000 2.0000
       </Qh>
       <Qk type="NX_FLOAT32[21]">
        0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000
        0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000
        0.0000 0.0000 0.0000 0.0000 0.0000
       </Qk>
       <Ql type="NX_FLOAT32[21]">
        0.6000 0.6000 0.6000 0.6000 0.6000 0.6000 0.6000 0.6000
        0.6000 0.6000 0.6000 0.6000 0.6000 0.6000 0.6000 0.6000
        0.6000 0.6000 0.6000 0.6000 0.6000
       </Ql>
       <energy_transfer type="NX_FLOAT32[21]" units="meV">
        2.0000 2.2500 2.5000 2.7500 3.0000 3.2500 3.5000 3.7500
        4.0000 4.2500 4.5000 4.7500 5.0000 5.2500 5.5000 5.7500
        6.0000 6.2500 6.5000 6.7500 7.0000
       </energy_transfer>
      </NXsample>

      <NXinstrument name="BT2">
       <NXcollimator name="premonochromator_collimator">
        <type type="NX_CHAR">
         "Soller"
        </type>
        <soller_angle type="NX_FLOAT32" units="minutes">
         60.0
        </soller_angle>
       </NXcollimator>
       <NXfilter name="premonochromator_filter">
        <description type="NX_CHAR">
         "Pyrolytic Graphite"
        </description>
       </NXfilter>
       <NXcrystal name="monochromator">
        <type type="NX_CHAR">
          "PG (Highly Oriented Pyrolytic Graphite)"
        </type>
        <energy type="NX_FLOAT32[21]" units="meV">
         14.700 14.700 14.700 14.700 14.700 14.700 14.700 14.700
         14.700 14.700 14.700 14.700 14.700 14.700 14.700 14.700
         14.700 14.700 14.700 14.700 14.700
        </energy>
        <d_spacing type="NX_FLOAT32" units="Angstrom">
          3.354
        </d_spacing>
        <rotation_angle type="NX_FLOAT32[21]" units="degrees">
         20.586 20.586 20.586 20.586 20.586 20.586 20.586 20.586
         20.586 20.586 20.586 20.586 20.586 20.586 20.586 20.586
         20.586 20.586 20.586 20.586 20.586
         </rotation_angle>
       </NXcrystal>
       <NXcollimator name="presample_collimator">
        <type type="NX_CHAR">
         "Soller"
        </type>
        <soller_angle type="NX_FLOAT32" units="minutes">
         40.0
        </soller_angle>
       </NXcollimator>
       <NXcollimator name="preanalyzer_collimator">
        <type type="NX_CHAR">
         "Soller"
        </type>
        <soller_angle type="NX_FLOAT32" units="minutes">
         40.0
        </soller_angle>
       </NXcollimator>
      <NXcrystal name="analyzer">
       <type type="NX_CHAR">
        "PG (Highly Oriented Pyrolytic Graphite)"
       </type>
       <energy type="NX_FLOAT32[21]" units="meV">
        16.7 16.95 17.2 17.45 17.7 17.95 18.2 18.45 18.7 18.95 19.2
        19.45 19.7 19.95 20.2 20.45 20.7 20.95 21.2 21.45 21.7
       </energy>
       <d_spacing type="NX_FLOAT32" units="Angstrom">
          3.354
       </d_spacing>
       <polar_angle type="NX_FLOAT32[21]" units="degrees">
        78.344 78.766 79.195 79.631 80.074 80.526 80.985 81.453
        81.930 82.417 82.914 83.422 83.941 84.471 85.015 85.572
        86.144 86.731 87.335 87.956 88.597
       </polar_angle>
       <rotation_angle type="NX_FLOAT32[21]" units="degrees">
        22.230 22.465 22.706 22.956 23.214 23.481 23.758 24.044
        24.342 24.650 24.971 25.304 25.652 26.014 26.392 26.787
        27.200 27.634 28.088 28.567 29.070
       </rotation_angle>
       <azimuthal_angle type="NX_FLOAT32" units="degrees">
        0.0
       </azimuthal_angle>
      </NXcrystal>
      <NXcollimator name="predetector_collimator">
       <type type="NX_CHAR">
        "Soller"
       </type>
       <soller_angle type="NX_FLOAT32" units="minutes">
        99.0
       </soller_angle>
      </NXcollimator>
      <NXdetector name="detector">
       <counts type="NX_INT32[21]" signal="1" axes="energy_transfer">
        49 43 29 22 25 21 27 44 53 80 89 80 36 20 9 18 12 16 8 13 12
       </counts>
       <polar_angle type="NX_FLOAT32[21]" units="degrees">
        44.461 44.929 45.412 45.912 46.428 46.962 47.515 48.089 48.683
        49.300 49.942 50.609 51.304 52.028 52.784 53.574 54.401 55.267
        56.177 57.133 58.140
       </polar_angle>
       <azimuthal_angle type="NX_FLOAT32" units="degrees">
        180.0
       </azimuthal_angle>
      </NXdetector>
      </NXinstrument>

      <NXmonitor name="monitor">
       <preset type="NX_FLOAT32[1]">
        4052000
       </preset>
      </NXmonitor>
      <NXtimer name "timer">
       <duration type="NX_FLOAT32[21]" units="seconds">
        238.20 238.20 238.20 238.20 238.20 238.20 238.20 238.20 238.20
        238.20 238.20 238.20 238.20 238.20 238.20 238.20 238.20 238.20
        238.20 238.20 238.20
       </duration>
      </NXtimer>
      <NXdata name="data">
       <Qh NAPIlink="/entry_0/sample/Qh" primary="1" />
       <Qk NAPIlink="/entry_0/sample/Qk" />
       <Ql NAPIlink="/entry_0/sample/Ql" />
       <energy_transfer NAPIlink="/entry_0/sample/energy_transfer" />
       <counts NAPIlink="/entry_0/BT2/detector/counts" signal="1" axes="Qh" />
       <count_durations NAPIlink="/entry_0/timer/duration" />
      </NXdata>
     </NXentry>
    </NXroot>
