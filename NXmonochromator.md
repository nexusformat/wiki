---
title: NXmonochromator
permalink: NXmonochromator/
layout: wiki
---

This is a base class for everything which selects a wavelength, be it a
monochromator crystal, a velocity selector, a undulator or whatever.

    <NXmonochromator name="name of monochromator">
      <wavelength type="NX_FLOAT[]" units="angstrom">
         {wavelength selected}
      </wavelength> 
      <wavelength_fwhm type="NX_FLOAT[]" units="angstrom">
         {wavelength full width at half maximum}
      </wavelength_fwhm> 
      <NXdata name="wavelength_distribution"/> 
    </NXmonochromator>
