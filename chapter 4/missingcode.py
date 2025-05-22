def seconds_since_midnight(hours, minutes seconds):
	hours_in_seconds = hours * 3600
	minute_in_seconds = minutes * 60
	seconds = seconds * 60
	return hours_in_seconds + minute_in_seconds + seconds