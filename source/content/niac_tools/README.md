# NIAC Tools

This folder is meant to contain tools helpful to NIAC members so that as new executive assume roles any tools that
are convenient to the role can be passed on in a formal location.

## ICS telco meeting reminder file generator

`ics_creator.py` is a small telco-specific helper which can be used to generate .ics
meeting files that mail recipients can add to their calendars as a convenience.

The intent is simple:
- only the start date/time changes
- sometimes the Zoom link changes
- everything else stays on a fixed template
- every generated `.ics` uses the same event `UID`

*ics_creator.py* is a small Python script that generates an `.ics` file for a recurring telco 
meeting. It allows you to specify the start time and Zoom link, while keeping other details 
constant.

## Minimum command-line usage

Only these arguments are required:
- `--output`
- `--start`
- `--zoom-link`

Example:

```powershell
Set-Location "C:\github\branches\1644-wiki\wiki\source\content\niac_tools"
python .\ics_creator.py --output .\telco.ics --start "2026-10-15T15:00:00+00:00" --zoom-link "https://example.com/zoom"
```

That command uses these defaults automatically:
- title: `NeXus Telco`
- duration: `60` minutes from the CLI default
- meeting ID: `652 7209 1306`
- password: `nexus`
- calendar name: `Export`
- timezone label: `UTC`
- reminder: `30` minutes
- UID: `163a6e67-c7db-4992-b9b9-0aa608172ca8@nexusformat.org`
- sequence: `0`

## Python usage

```python
from datetime import UTC, datetime
from ics_creator import write_telco_ics

write_telco_ics(
    "telco.ics",
    start=datetime(2026, 10, 15, 15, 0, tzinfo=UTC),
    zoom_link="https://example.com/zoom",
)
```

Optional values:
- `end`
- `duration`
- `title`
- `meeting_id`
- `password`
- `sequence`
- `reminder_email`


Update an existing invite for the same event by increasing `sequence`:

```powershell
Set-Location "C:\github\branches\1644-wiki\wiki\source\content\niac_tools"
python .\ics_creator.py --output .\telco.ics --start "2026-10-15T16:00:00+00:00" --zoom-link "https://example.com/zoom" --sequence 1
```
