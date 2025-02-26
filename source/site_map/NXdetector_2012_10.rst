==================
NXdetector 2012 10
==================


This is from an discussion about additions/modifications to
NXdetector to help Dectris as it decides to write raw image data into
HDF5/NeXus format. on 2012-11-07,

Mark Koennecke wrote
--------------------

Hi, at the last teleconference we
agreed that I do a summary of the state and options on the
DECTRIS/detector_element issue. Well, this is it. In the meantime the
information came in that DECTRIS is joining the two planned workshops
with a date in mid-january. Thus I assume we have a little more time to
sort this out. First the more political part: [...omitted...] Now the
more technical part: let us start with a description of the problem: The
EIGER (and other) detector is composed of multiple modules. All is fine
as long as these modules are arranged on a regular grid in order to form
one joint image. This can be easily stored in one NXdetector group. A
mask stored with the data gives information which pixels are valied and
which are boundaries. The problem starts when the individual modules are
arranged in an irregular arrangement: for example on a half sphere. Then
there are two requirements:

- The user still wants to see an image merged from the individual modules in order to quickly get an overview of the data. This requirement is best fulfilled by keeping the data in one fat array.

- For proper data analysis, more information on each individual module is needed. This is: \* The position of the module within the pixel array, offset and size \* The physical position and orientation of the module with respect to the detector as a whole In order to handle this, there are several propositions.

Use NXgeometry
==============

NXdetector module01,NXgeometry NXtranslation NXorientation module02,NXgeometry NXtranslation NXorientation
..... This option is missing the index information. I am not sure if we want to add
that to NXgeometry. I am also not sure if we still wish to advocate the
use of NXgeometry. IMHO, the CIF mapping is better and NXgeometry may be
deprecated soon.. But is not yet....

NXdetector_element
==================

The second option would be a new group:
NXdetector_element looking like this: NXdetector distance
module01,NXdetector_element x[nx] @transformation_type=translation
@offset=x,y,z @vector= ...
depends_on=/entry/instrument/detector/distance y[ny]
@transformation_type=translation @offset=0,0,0 @vector=.... depends_on=x
pixel_offset[2]=x,y The x any y arrays describe the pixels of the
module. This is wasting space as it is for example for x:
x[0]=0*pixelsize, x[1] = 1*pixelsize,... The offset and vector
attributes the position and orientation in space. The start indices go
into the pixel_offset

Tobias Suggestion
=================
A variant based on the way CIF handles the same problem detector:NXdetector
data[j,k,l] = [....] detector_arm[1] = [250] @transformation=translation
@vector={1,0,0} @units=cm @depends_on=/entry/instrument/something/brick
depends_on=detector_arm module:NXdetector_module data_origin[2] = [l,m]
data_size[2] = [n,o] module_offset[1] = [250]
@transformation=translation @vector={0,1,1} @units=mm
@depends_on="../detector_arm" fast_pixel_direction[1] = [0.172]
@transformation=translation @vector={1,0,0} @units=mm
@depends_on="module_offset" slow_pixel_direction[1] = [0.172]
@transformation=translation @vector={0,1,0} @units=mm
@depends_on="module_offset" module:NXdetector_module .... This uses less
space.

SNS Usage
=========

SNS had a similar problem and has resolved the issue by storing each detector module in a separate
NXdetector group. This works perfectly and would require no change on
our side. However, this would mean that DECTRIS would need to change
their data writing for this case. And vieweing the total image cannot be
done easily anymore without a reconstruction in SW or a duplication of
data. This looks like: module01,NXdetector data[NP,i,j] distance ......
module02,NXdetector data[NP,ij] distance... ....

The General Case
================

What also works is the existing facility in NeXus
to describe each pixel individually. Any pixel gets an ID and there are
arrays for distance, coordinates etc which are nPixel long. With nPixel
being the total number of pixels. But this would again destroy the
image. This looks like: detector,NXdetector data[NP,nPixel]
distance[nPixel] x_pixel_offset[nPixel] y_pixel_offset[nPixel] .... Of
course they may be many more options. But I hope these are enough to
find a solution Best Regards, Mark Koennecke
