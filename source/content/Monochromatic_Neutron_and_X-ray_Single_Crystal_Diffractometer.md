---
title: Monochromatic Neutron and X-ray Single Crystal Diffractometer
permalink: Monochromatic_Neutron_and_X-ray_Single_Crystal_Diffractometer.html
layout: wiki
---
Monochromatic Neutron and X-ray Single Crystal Diffractometer
=============================================================

This is the instrument definition for a single crystal diffractometer at
a monochromatic beam port, be it X-ray or neutrons. A eulerian cradle is
assumed as the sample positioner. However, with the exchange of a few
fields in NXsample, CAD-4 geometry is covered too. The description also
holds for a rotation camera, just drop the eulerian cradle related
fields in NXsample.

As the mode of measurement an omega or omega two-theta scan covering a
certain range is assumed. There are instructions how to deal with the
case of a general scans in the DTD's. The common case is that multiple
reflections are scanned in succession; in that case each reflection
should have its own entry in the file.

There are actually two DTD's which differ only in the NXdetector group:

-   [Four Circle with Single Detector](MonoXSingle.html "wikilink")
-   [Four Circle with Position Sensitive Detector](MonoXPSD.html "wikilink")

