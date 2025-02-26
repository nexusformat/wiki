========
XESraw
========

.. container:: content

   .. container:: page

      .. rubric:: XESraw
         :name: xesraw
         :class: page-title

      XESraw is a draft example of an X-Ray Experimental (Synchrotron)
      raw Nexus file.

      It is essentially a simple scanning format with a few mandatory
      items (mainly NXsource - to indicate the originating facility).
      The variables being scanned are inferred from the links
      for the "axis data" within the NXdata class(es).

      In this example, the axis data links point to values within NXpositioner
      classes, which is likely typical for most scan variables
      in a synchrotron experiment. However, they could just as easily refer to
      another place within the NXinstrument hierarchy.

      Example of an XML representation of the Nexus file:

      .. code-block:: xml

         <?xml version="1.0" encoding="UTF-8"?>
         <!--
         URL:      http://www.nexus.anl.gov/
         Editor:   Stuart Campbell, DLS
         $Id$
         Draft example of an X-Ray Experimental (Synchrotron) raw Nexus file.
         -->

         <NXroot>
            <NXentry name="Entry1">
               <title>"Example Data File"</title>

               <NXinstrument name="I18">
                  <name>"I18"</name>
                  <NXsource name="source">
                     <name>"Diamond Light Source"</name>
                     <type>"Synchrotron X-ray Source"</type>
                     <probe>"x-ray"</probe>
                  </NXsource>
                  <NXpositioner name="sampleX">
                     <value>[3001.0, 3002.0, 3003.0]</value>
                  </NXpositioner>
                  <NXpositioner name="time">
                     <value>[1.22, 2.34, 3.53]</value>
                  </NXpositioner>
                  <NXdetector name="detector1">
                     <description>"Ortec C-TRAIN"</description>
                     <type>"Counter Timer"</type>
                     <data>[203.0, 245.0, 233.0]</data>
                  </NXdetector>
                  <NXdetector name="detector2">
                     <description>"Quantum 315"</description>
                     <type>"CCD"</type>
                     <data>
                       {a data array with dimensions [3, nx, ny]}
                     </data>
                  </NXdetector>
               </NXinstrument>

               <NXdata name="detector1">
                  <data>{Link to detector1 counts}</data>
                  <sampleX axis="1" primary="1">
                     {Link to values in NXpositioner}
                  </sampleX>
                  <time axis="1" primary="2">
                     {Link to values in NXpositioner}
                  </time>
               </NXdata>
               <NXdata name="detector2">
                  <data>{Link to detector2 counts}</data>
                  <sampleX axis="1" primary="1">
                     {Link to values in NXpositioner}
                  </sampleX>
                  <time axis="1" primary="2">
                     {Link to values in NXpositioner}
                  </time>
               </NXdata>
            </NXentry>
         </NXroot>
