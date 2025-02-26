==========================
NXmonoref example-NIAC2006
==========================

.. code-block:: xml

    <NXroot filename="NXmonoref_example.xml">
     <NXentry name="entry">
      <definition version="1.0" URL="http://www.nexus.anl.gov/instruments/xml/NXmonoref.xml">NXmonoref</definition>
      <title>Summer-School '02 Group B measurement of unknown sample</title>
      <start_time type="ISO8601">2002-06-04T15:09:03-0400</start_time>
      <end_time type="ISO8601">2002-06-04T16:18:28-0400</end_time>
      <duration type="NX_INT" units="seconds">4165</duration>
      <range name="Qz">0.092328 0.18454</range>
      <NXuser name="">
        <name type="NX_CHAR">SS02 Group B</name>
        <affiliation type="NX_CHAR">NCNR</affiliation>
      </NXuser>

      <NXsample name="sample">
        <name type="NX_CHAR">unknown sample</name>
        <polar_angle type="NX_FLOAT32[51]" units="degree">
          2 2.04 2.08 2.12 2.16 2.2 2.24 2.28 2.32 2.36 2.4 2.44 2.48
          2.52 2.56 2.6 2.64 2.68 2.72 2.76 2.8 2.84 2.88 2.92 2.96 3
          3.04 3.08 3.12 3.16 3.2 3.24 3.28 3.32 3.36 3.4 3.44 3.48
          3.52 3.56 3.6 3.64 3.68 3.72 3.76 3.8 3.84 3.88 3.92 3.96 4
        </polar_angle>
      </NXsample>

      <NXinstrument name="instrument">

       <NXcrystal name="monochromator">
        <wavelength type="NX_FLOAT" units="Angstroms">4.75</wavelength>
        <wavelength_spread type "NX_FLOAT">0.01</wavelength_spread>
       </NXcrystal>

       <NXaperture name="presample_slit1">
        <NXgeometry name="geometry">
         <NXtranslation name="translation">
          <distances type="NX_FLOAT" units="mm">1700</distances>
         </NXtranslation>
         <NXshape name="shape">
          <type type="NX_CHAR">nxslit</type>
          <size type="NX_FLOAT32[51]" units="mm" filter="Qx">
            1.016 1.0363 1.0566 1.077 1.0973 1.1176 1.1379 1.1582 1.1786
            1.1989 1.2192 1.2395 1.2598 1.2802 1.3005 1.3208 1.3411
            1.3614 1.3818 1.4021 1.4224 1.4427 1.463 1.4834 1.5037 1.524
            1.5443 1.5646 1.585 1.6053 1.6256 1.6459 1.6662 1.6866 1.7069
            1.7272 1.7475 1.7678 1.7882 1.8085 1.8288 1.8491 1.8694 1.8898
            1.9101 1.9304 1.9507 1.971 1.9914 2.0117 2.032
         </size>
         </NXshape>
        </NXgeometry>
       </NXaperture>

       <NXaperture name="presample_slit2">
        <NXgeometry name="geometry">
         <NXtranslation name="translation">
          <distances type="NX_FLOAT" units="mm">200</distances>
         </NXtranslation>
         <NXshape name="shape">
          <type type="NX_CHAR">nxslit</type>
          <size type="NX_FLOAT32[51]" units="mm" filter="Qx">
            1.016 1.0363 1.0566 1.077 1.0973 1.1176 1.1379 1.1582 1.1786
            1.1989 1.2192 1.2395 1.2598 1.2802 1.3005 1.3208 1.3411
            1.3614 1.3818 1.4021 1.4224 1.4427 1.463 1.4834 1.5037 1.524
            1.5443 1.5646 1.585 1.6053 1.6256 1.6459 1.6662 1.6866 1.7069
            1.7272 1.7475 1.7678 1.7882 1.8085 1.8288 1.8491 1.8694 1.8898
            1.9101 1.9304 1.9507 1.971 1.9914 2.0117 2.032
         </size>
         </NXshape>
        </NXgeometry>
       </NXaperture>

       <NXdetector name="detector">
        <polar_angle type="NX_FLOAT32[51]" units="degree">
          4 4.08 4.16 4.24 4.32 4.4 4.48 4.56 4.64 4.72 4.8 4.88 4.96 5.04
          5.12 5.2 5.28 5.36 5.44 5.52 5.6 5.68 5.76 5.84 5.92 6 6.08 6.16
          6.24 6.32 6.4 6.48 6.56 6.64 6.72 6.8 6.88 6.96 7.04 7.12 7.2
          7.28 7.36 7.44 7.52 7.6 7.68 7.76 7.84 7.92 8
        </polar_angle>
        <counts type="NX_INT[51]" axes="[polar_angle]" units="count">
          194 239 256 319 291 373 393 397 399 381 375 358 331 275 256 242
          186 171 132 114 69 64 68 49 43 50 41 61 83 80 102 110 109 143 139
          134 138 127 147 134 124 127 106 88 87 70 60 60 49 43 41
        </data>
        <distance type="NX_FLOAT" units="mm">1220</distance>
       </NXdetector>

      </NXinstrument>

      <NXdata>
       <presample_slit1 axis="1" NAPIlink="NXentry/NXinstrument/presample_slit1/NXgeometry/NXshape/size"/>
       <presample_slit2 axis="1" NAPIlink="NXentry/NXinstrument/presample_slit2/NXgeometry/NXshape/size"/>
       <theta axis="1" NAPIlink="NXentry/NXsample/polar_angle"/>
       <twotheta axis="1" NAPIlink="NXentry/NXinstrument/detector/polar_angle"/>
       <counts axes="[twotheta]" NAPIlink="NXentry/NXinstrument/NXdetector/counts"/>
       <count_start NAPIlink="NXentry/timer/time" />
       <count_duration NAPIlink="NXentry/timer/value" />
       <count_monitor NAPIlink="NXentry/monitor/data" />
       <scan_type>specular</specular>
      </NXdata>
      <NXmonitor name="monitor">
       <preset type="NX_INT">600000</preset>
       <data type="NX_INT[51]">
         600000 600000 600000 600000 600000 600000 600000 600000 600000
         600000 600000 600000 600000 600000 600000 600000 600000 600000
         600000 600000 600000 600000 600000 600000 600000 600000 600000
         600000 600000 600000 600000 600000 600000 600000 600000 600000
         600000 600000 600000 600000 600000 600000 600000 600000 600000
         600000 600000 600000 600000 600000 600000
       </data>
      </NXmonitor>
      <NXlog name="timer">
       <start type="ISO8601">2002-06-04T15:09:03-0400</start>
       <time type="NX_FLOAT32[51]" units="second">
         0.0 115.8 228.6 339.6 448.8 555.6 660.6 764.4 865.2 965.4
         1063.2 1160.4 1255.2 1348.2 1440 1531.2 1621.2 1710 1797
         1882.8 1968 2052 2134.8 2215.8 2296.8 2376.6 2455.8 2533.8
         2610.6 2686.8 2761.8 2835.6 2908.8 2982 3052.8 3123.6 3193.8
         3264 3333 3400.8 3468.6 3535.8 3601.8 3666.6 3730.8 3795 3858
         3919.8 3981.6 4043.4 4104.6
       </time>
       <value type="NX_FLOAT32[51]" units="second">
         115.8 112.8 111 109.2 106.8 105 103.8 100.8 100.2 97.8 97.2
         94.8 93 91.8 91.2 90 88.8 87 85.8 85.2 84 82.8 81 81 79.8
         79.2 78 76.8 76.2 75 73.8 73.2 73.2 70.8 70.8 70.2 70.2 69
         67.8 67.8 67.2 66 64.8 64.2 64.2 63 61.8 61.8 61.8 61.2 60
       </value>
      </NXlog>
     </NXentry>
    </NXroot>