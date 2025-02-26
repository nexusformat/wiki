Storing Event Data
==================

This discussion concerns a proposal from
`[NIAC2008] <../niac/NIAC2008.html>`__ to rename
[NXevent_data] <NXevent_data.html> as NXtofevent_data.
When this proposal was passed to the full committee, a number of issues
were raised and it was decided that a further round of discussion was
required. Please comment on the proposals below on the `[discussion page] <Storing_Event_Data.html>`__.
Listed below are some of the main reasons cited for and against:

REASONS FOR
-----------

-   NXtofevent_data better describes the content of the object, given that
    [NXevent_data] <NXevent_data.html> has a time_of_flight member

REASONS AGAINST
---------------

-   Event data is potentially of importance to the other communities and therefore it
    would be good to ensure that the definition name for event data is as
    general as possible. Event data is not always measured against
    time_of_flight

-   it may be e.g. muon decay time and so a more
    general event_time axis may be applicable

-   I'm not sure why the
    addition of tof is necessary. Pulsed source and chopped continuous
    source event data can be represented in ways that are substantially the
    same. By renaming the fields we can handle different kinds of events in
    the same manner, so there is no need to change the group name to be
    specific to time of flight

-   NXtofevent_data is an ugly name.
    NXtof_event_data is a better name, or just NXevent_data

PROPOSAL from Paul Kienzle regarding contents of NXevent_data
--------------------------------------------------------------

First
note that either pulse_height or pulse_time is the wrong name.

-   pulse_height[i,k?] refers to the voltage pulse measured by the
    detector - pulse_time[j] refers to the time that the neutron pulse
    reached the moderator The description of the pulse_height field is
    confusing. It refer to events_per_pulse, which has length j but it's
    own index is of length i, so something is screwy. I suggest renaming
    time_of_flight to event_time and pulse_time to frame_time and
    you have something that can be used either for continuous or pulsed
    sources.

-   event_time[i]: time relative to the start of the frame

-   pixel_number[i]: detector which registered the event -
    frame_time[j]: time relative to the start of the measurement -
    events_per_frame[j]: as before

-   pulse_height[i,k?]:
    detector voltages The frame_time for continuous sources presumably
    refers to the time when the detector was turned on after moving the
    motors during a scan for multi-point scans. When scanning continuously (a
    potentially useful measurement during alignment operations), the frame
    time would more likely refer to the pulses from the motor position
    detectors.

Conclusion
----------

01/2015: There was no activity on this
for a long time. There is a NXevent_data base class and both SNS and
ISIS are writing data files using that base class. Please consult the
documentation of the base class for the current state.
