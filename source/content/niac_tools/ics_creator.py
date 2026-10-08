"""Minimal helper for generating NeXus telco .ics files.

This version is intentionally small: only the meeting time and link normally
change, while the rest stays template-driven.
"""

from __future__ import annotations

from argparse import ArgumentParser
from datetime import UTC, datetime, timedelta
from pathlib import Path


DEFAULT_TITLE = "NeXus Telco"
DEFAULT_DURATION = timedelta(hours=1)
DEFAULT_PRODID = "-//NeXus Telco//Meeting Invite//EN"
DEFAULT_CALENDAR_NAME = "Export"
DEFAULT_CALENDAR_TIMEZONE = "UTC"
DEFAULT_UID = "163a6e67-c7db-4992-b9b9-0aa608172ca8@nexusformat.org"
DEFAULT_MEETING_ID = "652 7209 1306"
DEFAULT_PASSWORD = "nexus"
DEFAULT_REMINDER_MINUTES = 30
DEFAULT_STATUS = "CONFIRMED"
DEFAULT_TRANSPARENCY = "TRANSPARENT"
DEFAULT_MEETING_LEN_MINUTES = 60


def _html_escape(value: str) -> str:
	return (
		value.replace("&", "&amp;")
		.replace("<", "&lt;")
		.replace(">", "&gt;")
		.replace('"', "&quot;")
	)


def _escape_text(value: str) -> str:
	return (
		value.replace("\\", "\\\\")
		.replace("\r\n", "\\n")
		.replace("\n", "\\n")
		.replace(";", "\\;")
		.replace(",", "\\,")
	)


def _fold_ical_line(line: str, limit: int = 75) -> str:
	if len(line.encode("utf-8")) <= limit:
		return line

	parts: list[str] = []
	current = bytearray()
	for character in line:
		encoded = character.encode("utf-8")
		if current and len(current) + len(encoded) > limit:
			parts.append(current.decode("utf-8"))
			current = bytearray(b" ")
		current.extend(encoded)
	parts.append(current.decode("utf-8"))
	return "\r\n".join(parts)


def _format_datetime(value: datetime) -> str:
	if value.tzinfo is None or value.utcoffset() is None:
		raise ValueError("Datetime values must be timezone-aware.")
	return value.astimezone(UTC).strftime("%Y%m%dT%H%M%SZ")


def _parse_iso_datetime(value: str) -> datetime:
	parsed = datetime.fromisoformat(value)
	if parsed.tzinfo is None or parsed.utcoffset() is None:
		raise ValueError("Datetime arguments must include a timezone offset.")
	return parsed


def _alarm_trigger(minutes: int) -> str:
	if minutes <= 0:
		raise ValueError("Reminder minutes must be greater than zero.")
	hours, remainder = divmod(minutes, 60)
	return f"-P0DT{hours}H{remainder}M0S"


def build_description(
	zoom_link: str,
	meeting_id: str = DEFAULT_MEETING_ID,
	password: str = DEFAULT_PASSWORD,
) -> str:
	clean_link = zoom_link.strip()
	if not clean_link:
		raise ValueError("zoom_link is required.")
	return (
		f'<a href="{_html_escape(clean_link)}" target="_blank">'
		f"{_html_escape(clean_link)}</a><br>"
		f"Meeting ID: {_html_escape(meeting_id)}<br>"
		f"Password: {_html_escape(password)}"
	)


def create_telco_ics(
	*,
	start: datetime,
	zoom_link: str,
	end: datetime | None = None,
	duration: timedelta = DEFAULT_DURATION,
	title: str = DEFAULT_TITLE,
	meeting_id: str = DEFAULT_MEETING_ID,
	password: str = DEFAULT_PASSWORD,
	sequence: int = 0,
	dtstamp: datetime | None = None,
	calendar_name: str = DEFAULT_CALENDAR_NAME,
	calendar_timezone: str = DEFAULT_CALENDAR_TIMEZONE,
	reminder_minutes: int = DEFAULT_REMINDER_MINUTES,
	reminder_email: str | None = None,
) -> str:
	if end is None:
		end = start + duration
	if end <= start:
		raise ValueError("end must be later than start.")

	stamp = dtstamp or datetime.now(UTC)
	trigger = _alarm_trigger(reminder_minutes)
	lines = [
		"BEGIN:VCALENDAR",
		f"PRODID:{DEFAULT_PRODID}",
		"VERSION:2.0",
		"CALSCALE:GREGORIAN",
		"METHOD:PUBLISH",
		f"X-WR-CALNAME:{_escape_text(calendar_name)}",
		f"X-WR-TIMEZONE:{_escape_text(calendar_timezone)}",
		"BEGIN:VEVENT",
		f"DTSTART:{_format_datetime(start)}",
		f"DTEND:{_format_datetime(end)}",
		f"DTSTAMP:{_format_datetime(stamp)}",
		f"UID:{DEFAULT_UID}",
		f"DESCRIPTION:{_escape_text(build_description(zoom_link, meeting_id, password))}",
		f"SEQUENCE:{sequence}",
		f"STATUS:{DEFAULT_STATUS}",
		f"SUMMARY:{_escape_text(title)}",
		f"TRANSP:{DEFAULT_TRANSPARENCY}",
	]

	if reminder_email:
		lines.extend(
			[
				"BEGIN:VALARM",
				"ACTION:EMAIL",
				f"ATTENDEE:mailto:{reminder_email}",
				f"TRIGGER:{trigger}",
				"DESCRIPTION:This is an event reminder",
				"SUMMARY:Alarm notification",
				"END:VALARM",
			]
		)

	lines.extend(
		[
			"BEGIN:VALARM",
			"ACTION:DISPLAY",
			f"TRIGGER:{trigger}",
			"DESCRIPTION:This is an event reminder",
			"END:VALARM",
			"END:VEVENT",
			"END:VCALENDAR",
		]
	)
	return "\r\n".join(_fold_ical_line(line) for line in lines) + "\r\n"


def write_telco_ics(output_path: str | Path, **invite_kwargs: object) -> str:
	content = create_telco_ics(**invite_kwargs)
	path = Path(output_path)
	path.parent.mkdir(parents=True, exist_ok=True)
	with path.open("w", encoding="utf-8", newline="") as stream:
		stream.write(content)
	return content


def main() -> None:
	parser = ArgumentParser(description="Generate a NeXus telco .ics file.")
	parser.add_argument("--output", required=True, help="Path to the .ics file to write.")
	parser.add_argument("--start", required=True, help="Start timestamp in ISO-8601 format.")
	parser.add_argument("--end", help="Optional end timestamp in ISO-8601 format.")
	parser.add_argument("--duration-minutes", type=int, default=DEFAULT_MEETING_LEN_MINUTES, help="Meeting duration in minutes.")
	parser.add_argument("--zoom-link", required=True, help="Zoom or meeting URL.")
	parser.add_argument("--summary", default=DEFAULT_TITLE, help="Meeting title.")
	parser.add_argument("--meeting-id", default=DEFAULT_MEETING_ID, help="Meeting ID text.")
	parser.add_argument("--password", default=DEFAULT_PASSWORD, help="Meeting password text.")
	parser.add_argument("--calendar-name", default=DEFAULT_CALENDAR_NAME, help="Calendar name.")
	parser.add_argument("--calendar-timezone", default=DEFAULT_CALENDAR_TIMEZONE, help="Calendar timezone label.")
	parser.add_argument("--reminder-minutes", type=int, default=DEFAULT_REMINDER_MINUTES, help="Reminder lead time in minutes.")
	parser.add_argument("--reminder-email", default="", help="Optional email recipient for the email alarm.")
	parser.add_argument("--sequence", type=int, default=0, help="Sequence number for event updates.")
	args = parser.parse_args()

	write_telco_ics(
		output_path=args.output,
		start=_parse_iso_datetime(args.start),
		end=_parse_iso_datetime(args.end) if args.end else None,
		duration=timedelta(minutes=args.duration_minutes),
		zoom_link=args.zoom_link,
		title=args.summary,
		meeting_id=args.meeting_id,
		password=args.password,
		calendar_name=args.calendar_name,
		calendar_timezone=args.calendar_timezone,
		reminder_minutes=args.reminder_minutes,
		reminder_email=args.reminder_email or None,
		sequence=args.sequence,
	)


if __name__ == "__main__":
	main()
