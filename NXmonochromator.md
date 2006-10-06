---
title: NXmonochromator
permalink: NXmonochromator/
layout: wiki
---

This is a base class for everything which selects a wavelength or
energy, be it a monochromator crystal, a velocity selector, a undulator
or whatever.

    <NXmonochromator name="name of monochromator">
      <wavelength type="NX_FLOAT[]" units="angstrom">
         {wavelength selected}
      </wavelength> 
      <wavelength_error type="NX_FLOAT[]" units="angstrom">
         {wavelength standard deviation}
      </wavelength_error> 
      <energy type="NX_FLOAT[]" units="eV">
         {energy selected}
      </energy > 
      <energy_error type="NX_FLOAT[]" units="eV">
         {energy standard deviation}
      </energy_error> 
      <NXdata name="wavelength_distribution"/> 
    </NXmonochromator>
