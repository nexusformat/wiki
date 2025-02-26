==========
NXlrcs.f90
==========


.. code-block:: fortran

  program NXlrcs
    use IPNS_module
    use NXUmodule
    type(IPNS_histogram) :: hist
    type(IPNS_sgarray) :: sgarray
    type(IPNS_subgroup) :: sg
    type(IPNS_timefield) :: tf
    integer, dimension(:), allocatable :: sglist
    integer :: int_value
    real :: real_value
    character(len=80) :: char_value, entry
    character(len=40) :: argv
    character(len=4) :: run_no
    character(len=24) :: iso_time
    character(len=18) :: IPNS_time
    real :: L1
    integer :: char_size, Nhist, Nsg, i, j, status
    type(NXhandle) :: file_id
    type(NXlink) :: phi_id, time_id, M1_id, M2_id

    ! Open LRMECS run file
    i = IARGC()
    if (i == 0) then
      write (unit=*, fmt="(a)", advance="no") " Give run number : "
      read *, int_value
    else
      call GETARG (i, argv)
      read (trim(argv), "(i10)") int_value
    end if

    write (run_no, fmt="(i4.4)") int_value
    call open_IPNS_file ("/data/lrmecs/lrcs"//run_no//".run")
    if (.not. IPNS_OK) then
      print *, IPNS_message
      stop
    end if

    ! Open NeXus output file and write global attributes
    if (NXopen("lrcs"//run_no//".nxs", NXACC_CREATE, file_id) /= NX_OK) stop
    call get_IPNS_item ("NAM", char_value, item_size=char_size)
    if (NXUwriteglobals(file_id, trim(char_value(1:char_size))) /= NX_OK) stop

    call get_IPNS_item ("NHT", Nhist)

    ! Set default compression algorithm for larger data sets
    if (NXUsetcompress(file_id, NX_COMP_LZW) /= NX_OK) stop

    ! Loop over each run-file histogram
    do i = 1, Nhist
      ! Open one NXentry for each histogram
      write (entry, fmt="(a,i1)") "Histogram", i
      if (NXUwritegroup(file_id, entry, "NXentry") /= NX_OK) stop
      call get_IPNS_item ("TTL", char_value)
      if (NXUwritedata(file_id, "title", char_value) /= NX_OK) stop
      if (NXUwritedata(file_id, "analysis", "TOFNDGS") /= NX_OK) stop
      call get_IPNS_item ("SDT", char_value)
      IPNS_time(1:10) = char_value//" "
      call get_IPNS_item ("STM", char_value)
      IPNS_time(11:18) = char_value
      call convert_time(IPNS_time, iso_time)
      if (NXUwritedata(file_id, "start_time", iso_time) /= NX_OK) stop
      call get_IPNS_item ("EDT", char_value)
      IPNS_time(1:10) = char_value//" "
      call get_IPNS_item ("ETM", char_value)
      IPNS_time(11:18) = char_value
      call convert_time(IPNS_time, iso_time)
      if (NXUwritedata(file_id, "end_time", iso_time) /= NX_OK) stop
      call get_IPNS_item ("RUN", int_value)
      if (NXUwritedata(file_id, "run_number", int_value) /= NX_OK) stop

      ! Open NXsample
      if (NXUwritegroup(file_id, "sample", "NXsample") /= NX_OK) stop
      call get_IPNS_item ("L1", L1)
      if (NXUwritedata(file_id, "distance", 0.0, "m") /= NX_OK) stop
      if (NXUwritedata(file_id, "moderator_distance", L1, "m") /= NX_OK) stop
      if (NXclosegroup(file_id) /= NX_OK) stop

      ! Open NXinstrument
      call get_IPNS_item (i, hist)
      Nsg = size(hist%sg)
      if (i == 1) then
        allocate(sglist(nsg-2))
        sglist = (/ (i, i=3,Nsg) /)
      else
        allocate(sglist(Nsg))
        sglist = (/ (i, i=1,Nsg) /)
      end if
      call get_IPNS_item(sglist, sgarray, i)
      deallocate(sglist)
      if (NXUwritegroup(file_id, "LRMECS", "NXinstrument") /= NX_OK) stop

      ! Open NXsource
      if (NXUwritegroup(file_id, "source", "NXsource") /= NX_OK) stop
      if (NXUwritedata(file_id, "distance", -L1, "m") /= NX_OK) stop
      call get_IPNS_item ("PLS", int_value)
      if (NXUwritedata(file_id, "proton_pulses", int_value) /= NX_OK) stop
      if (NXUwritedata(file_id, "name", "IPNS") /= NX_OK) stop
      if (NXUwritedata(file_id, "type", "Spallation Neutron Source") /= NX_OK) stop
      if (NXUwritedata(file_id, "frequency", 30.0, "Hz") /= NX_OK) stop
      if (NXUwritedata(file_id, "target_material", "depleted_U") /= NX_OK) stop
      if (NXUwritedata(file_id, "moderator", "CH4") /= NX_OK) stop
      if (NXclosegroup(file_id) /= NX_OK) stop

      ! Open NXchopper
      if (NXUwritegroup(file_id, "monochromator", "NXchopper") /= NX_OK) stop
      call get_IPNS_item ("LCH", real_value)
      if (NXUwritedata(file_id, "distance", real_value-L1, "m") /= NX_OK) stop
      if (NXUwritedata(file_id, "moderator_distance", real_value, "m") /= NX_OK) stop
      if (NXUwritedata(file_id, "type", "Fermi") /= NX_OK) stop
      call get_IPNS_item ("EIN", real_value)
      if (NXUwritedata(file_id, "energy", real_value, "meV") /= NX_OK) stop
      if (NXputattr(file_id, "calibration_status", "Nominal") /= NX_OK) stop
      if (NXclosegroup(file_id) /= NX_OK) stop

      ! Open NXdetector
      if (NXUwritegroup(file_id, "detector_bank", "NXdetector") /= NX_OK) stop
      if (NXUwritedata(file_id, "distance", sgarray%L2, "m") /= NX_OK) stop
      if (NXUwritedata(file_id, "type", "He3 gas cylinder") /= NX_OK) stop
      if (NXUwritedata(file_id, "gas_pressure", 6.0, "bars") /= NX_OK) stop
      if (NXUwritedata(file_id, "time_of_flight", sgarray%time_of_flight, "microseconds") /= NX_OK) stop
      if (NXgetdataID(file_id, time_id) /= NX_OK) stop
      if (NXputattr(file_id, "long_name", "Time-of-Flight [microseconds]") /= NX_OK) stop
      if (NXUwritedata(file_id, "polar_angle", sgarray%phi, "degrees") /= NX_OK) stop
      if (NXgetdataID(file_id, phi_id) /= NX_OK) stop
      if (NXputattr(file_id, "long_name", "Polar Angle [degrees]") /= NX_OK) stop
      if (NXclosegroup(file_id) /= NX_OK) stop
      if (NXclosegroup(file_id) /= NX_OK) stop

      ! Open NXmonitor
      if (i == 1) then
        if (NXUwritegroup(file_id, "monitor1", "NXmonitor") /= NX_OK) stop
        call get_IPNS_item(1, sg, i)
        if (NXUwritedata(file_id, "distance", sg%L2, "m") /= NX_OK) stop
        if (NXUwritedata(file_id, "moderator_distance", L1+sg%L2, "m") /= NX_OK) stop
        if (NXUwritedata(file_id, "time_of_flight", sg%time_of_flight, "microseconds") /= NX_OK) stop
        if (NXputattr(file_id, "long_name", "Time-of-Flight [microseconds]") /= NX_OK) stop
        if (NXUwritedata(file_id, "data", sg%counts, "counts") /= NX_OK) stop
        if (NXputattr(file_id, "signal", 1) /= NX_OK) stop
        if (NXputattr(file_id, "long_name", "Monitor 1 Counts") /= NX_OK) stop
        if (NXputattr(file_id, "axes", "[time_of_flight]") /= NX_OK) stop
        if (NXgetgroupID(file_id, M1_id) /= NX_OK) stop
        call free_IPNS_subgroup(sg)
        if (NXclosegroup(file_id) /= NX_OK) stop
      else
        if (NXmakelink(file_id, M1_id) /= NX_OK) stop
      end if

      ! Open NXmonitor
      if (i == 1) then
        if (NXUwritegroup(file_id, "monitor2", "NXmonitor") /= NX_OK) stop
        call get_IPNS_item(2, sg, i)
        if (NXUwritedata(file_id, "distance", sg%L2, "m") /= NX_OK) stop
        if (NXUwritedata(file_id, "moderator_distance", L1+sg%L2, "m") /= NX_OK) stop
        if (NXUwritedata(file_id, "time_of_flight", sg%time_of_flight, "microseconds") /= NX_OK) stop
        if (NXputattr(file_id, "long_name", "Time-of-Flight [microseconds]") /= NX_OK) stop
        if (NXUwritedata(file_id, "data", sg%counts, "counts") /= NX_OK) stop
        if (NXputattr(file_id, "signal", 1) /= NX_OK) stop
        if (NXputattr(file_id, "long_name", "Monitor 2 Counts") /= NX_OK) stop
        if (NXputattr(file_id, "axes", "[time_of_flight]") /= NX_OK) stop
        if (NXgetgroupID(file_id, M2_id) /= NX_OK) stop
        if (NXclosegroup(file_id) /= NX_OK) stop
        call free_IPNS_subgroup(sg)
      else
        if (NXmakelink(file_id, M2_id) /= NX_OK) stop
      end if

      ! Open NXdata
      if (NXUwritegroup(file_id, "data", "NXdata") /= NX_OK) stop
      call get_IPNS_item("TTL", char_value)
      if (NXUwritedata(file_id, "title", char_value) /= NX_OK) stop
      if (NXUwritedata(file_id, "data", sgarray%counts, "counts") /= NX_OK) stop
      if (NXputattr(file_id, "signal", 1) /= NX_OK) stop
      if (NXputattr(file_id, "axes", "[polar_angle,time_of_flight]") /= NX_OK) stop
      if (NXputattr(file_id, "long_name", "Sample Data") /= NX_OK) stop
      if (NXclosegroup(file_id) /= NX_OK) stop
    end do

    if (NXclose(file_id) /= NX_OK) stop
  end program NXlrcs
