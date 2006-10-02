---
title: Monochromatic Neutron and X-ray Triple-Axis Spectrometer
permalink: Monochromatic_Neutron_and_X-ray_Triple-Axis_Spectrometer/
layout: wiki
---

&lt;!-- URL: http://www.nexus.anl.gov/classes/xml/NXmonotas.xml Editor:
NIAC NIAC Version: 0.1 $Id: monotas.docbook,v 1.1 2005/06/14 16:50:35
pfp Exp $ Template of a generic NeXus file containing neutron or x-ray
triple-axi s data.--&gt; &lt;NXentry name="{Name of entry}"&gt;
&lt;title&gt; {Extended title for entry} &lt;/title&gt; &lt;definition
URL="http://www.nexus.anl.gov/instruments/xml/NXmonotas.xml"
version="1.0"&gt; NXmonotas &lt;/definition&gt; &lt;start\_time
type="ISO8601"&gt; {Starting time of measurement} &lt;/start\_time&gt;
&lt;NXsample name="sample"&gt; &lt;name type="NX\_CHAR"&gt; {Descriptive
name of sample}? &lt;/name&gt; &lt;unit\_cell
type="NX\_FLOAT32\[1,6\])"&gt; {Unit cell parameters (lengths and
angles)}? &lt;/unit\_cell&gt; &lt;plane\_vector\_0
type="NX\_FLOAT32\[3\]"&gt; {Reciprocal space vector of primary
reflection in the scattering plane} &lt;/plane\_vector\_0&gt;
&lt;plane\_vector\_1 type="NX\_FLOAT32\[3\]"&gt; {Reciprocal space
vector of secondary reflection in the scattering plane}
&lt;/plane\_vector\_1&gt; &lt;polar\_angle units="degree"
type="NX\_FLOAT32\[:\]"&gt; {Polar angle of the sample with respect to
the beam incident on the monoch romator} &lt;/polar\_angle&gt;
&lt;azimuthal\_angle units="degree" type="NX\_FLOAT32"&gt; {Azimuthal
angle of the sample with respect to the beam incident on the
monochromator} &lt;/azimuthal\_angle&gt; &lt;rotation\_angle
units="degree" type="NX\_FLOAT32\[:\]"&gt; {Rotation angle of the
sample} &lt;/rotation\_angle&gt; &lt;Qh type="NX\_FLOAT32\[:\]"&gt;
{Reciprocal space component of scan} &lt;/Qh&gt; &lt;Qk
type="NX\_FLOAT32\[:\]"&gt; {Reciprocal space component of scan}
&lt;/Qk&gt; &lt;Ql type="NX\_FLOAT32\[:\]"&gt; {Reciprocal space
component of scan} &lt;/Ql&gt; &lt;energy\_transfer units="meV"
type="NX\_FLOAT32\[:\]"&gt; {Energy transfer of scan}
&lt;/energy\_transfer&gt; &lt;/NXsample&gt; &lt;NXinstrument name="{Name
of instrument}"&gt; &lt;NXcollimator
name="premonochromator\_collimator"&gt; &lt;type type="NX\_CHAR"&gt;
"Soller"|"radial" &lt;/type&gt; &lt;soller\_angle units="minute"
type="NX\_FLOAT32"&gt; {Angular divergence of Soller collimator}
&lt;/soller\_angle&gt; &lt;/NXcollimator&gt; &lt;NXfilter
name="premonochromator\_filter"&gt; &lt;description type="NX\_CHAR"&gt;
{"Beryllium" | "Pyrolytic Graphite" | "Graphite"} &lt;/description&gt;
&lt;/NXfilter&gt; &lt;NXcrystal name="monochromator"&gt; &lt;type
type="NX\_CHAR"&gt; {"PG (Highly Oriented Pyrolytic Graphite)" | "Ge" |
"Si" | "Cu" | "Fe3Si" | "CoFe" | "Cu2MnAl (Heusler)" | "Multilayer"}
&lt;/type&gt; &lt;energy units="meV" type="NX\_FLOAT32\[:\]"&gt;
{Optimum diffracted energy} &lt;/energy&gt; &lt;d\_spacing
units="Angstrom" type="NX\_FLOAT32"&gt; {The planar spacing of the
nominal reflection} &lt;/d\_spacing&gt; &lt;rotation\_angle
units="degree" type="NX\_FLOAT32\[:\]"&gt; {Rotation angle of the
monochromator} &lt;/rotation\_angle&gt; &lt;/NXcrystal&gt;
&lt;NXcollimator name="presample\_collimator"&gt; &lt;type
type="NX\_CHAR"&gt; "Soller"|"radial" &lt;/type&gt; &lt;soller\_angle
units="minute" type="NX\_FLOAT32"&gt; {Angular divergence of Soller
collimator} &lt;/soller\_angle&gt; &lt;/NXcollimator&gt; &lt;NXfilter
name="presample\_filter"&gt; &lt;description type="NX\_CHAR"&gt;
{"Beryllium" | "Pyrolytic Graphite" | "Graphite"} &lt;/description&gt;
&lt;/NXfilter&gt; &lt;NXcollimator name="preanalyzer\_collimator"&gt;
&lt;type type="NX\_CHAR"&gt; "Soller"|"radial" &lt;/type&gt;
&lt;soller\_angle units="minute" type="NX\_FLOAT32"&gt; {Angular
divergence of Soller collimator} &lt;/soller\_angle&gt;
&lt;/NXcollimator&gt; &lt;NXfilter name="preanalyzer\_filter"&gt;
&lt;description type="NX\_CHAR"&gt; {"Beryllium" | "Pyrolytic Graphite"
| "Graphite"} &lt;/description&gt; &lt;/NXfilter&gt; &lt;NXcrystal
name="analyzer"&gt; &lt;type type="NX\_CHAR"&gt; {"PG (Highly Oriented
Pyrolytic Graphite)" | "Ge" | "Si" | "Cu" | "Fe3Si" | "CoFe" | "Cu2MnAl
(Heusler)" | "Multilayer"} &lt;/type&gt; &lt;energy units="meV"
type="NX\_FLOAT32\[:\]"&gt; {Optimum diffracted energy} &lt;/energy&gt;
&lt;d\_spacing units="Angstrom" type="NX\_FLOAT32"&gt; {The planar
spacing of the nominal reflection} &lt;/d\_spacing&gt; &lt;polar\_angle
units="degree" type="NX\_FLOAT32\[:\]"&gt; {Polar angle of the analyzer
with respect to the beam incident on the monochromator}
&lt;/polar\_angle&gt; &lt;azimuthal\_angle units="degree"
type="NX\_FLOAT32"&gt; {Azimuthal angle of the analyzer with respect to
the beam incident on the monochromator} &lt;/azimuthal\_angle&gt;
&lt;rotation\_angle units="degree" type="NX\_FLOAT32\[:\]"&gt; {Rotation
angle of the monochromator} &lt;/rotation\_angle&gt; &lt;/NXcrystal&gt;
&lt;NXcollimator name="predetector\_collimator"&gt; &lt;type
type="NX\_CHAR"&gt; "Soller"|"radial" &lt;/type&gt; &lt;soller\_angle
units="minute" type="NX\_FLOAT32"&gt; {Angular divergence of Soller
collimator} &lt;/soller\_angle&gt; &lt;/NXcollimator&gt; &lt;NXdetector
name="detector"&gt; &lt;counts signal="1"
axes="energy\_transfer|Qh|Qk|Ql" type="NX\_INT32\[:\]"&gt; {Integer
counts} &lt;/counts&gt; &lt;polar\_angle units="degree"
type="NX\_FLOAT32\[:\]"&gt; {Polar angle of the detector with respect to
the beam incident on the monochromator} &lt;/polar\_angle&gt;
&lt;azimuthal\_angle units="degree" type="NX\_FLOAT32"&gt; {Azimuthal
angle of the detector with respect to the beam incident on the analyzer}
&lt;/azimuthal\_angle&gt; &lt;/NXdetector&gt; &lt;/NXinstrument&gt;
&lt;NXmonitor name="monitor"&gt; &lt;mode type="NX\_CHAR"&gt;
"monitor"|"timer" &lt;/mode&gt; &lt;preset type="NX\_FLOAT32\[1\]"&gt;
{preset value for time or monitor} &lt;/preset&gt; &lt;data
type="NX\_INT\[:\]"&gt; {Monitor data}? &lt;/data&gt; &lt;/NXmonitor&gt;
&lt;NXdata name="data"&gt; &lt;Qh NAPIlink="NXentry/NXsample/Qh"&gt;
&lt;/Qh&gt; &lt;Qk NAPIlink="NXentry/NXsample/Qk"&gt; &lt;/Qk&gt; &lt;Ql
NAPIlink="NXentry/NXsample/Ql"&gt; &lt;/Ql&gt; &lt;energy\_transfer
NAPIlink="NXentry/NXsample/energy\_transfer"&gt;
&lt;/energy\_transfer&gt; &lt;counts
NAPIlink="NXentry/NXinstrument/detector/counts"&gt; &lt;/counts&gt;
&lt;energy NAPIlink="NXentry/NXinstrument/analyzer/energy"&gt;
&lt;/energy&gt; &lt;/NXdata&gt; &lt;/NXentry&gt;
