import re
E164_RE = re.compile(r'^\+[1-9]\d{1,14}$')
def validate_phone(p):
    return bool(E164_RE.match(p or ''))
def validate_time_window(apt_time):
    try:
        h,m = map(int, apt_time.split(':'))
        if h < 8 or h > 20: return False
        return True
    except:
        return False
def validate_appointment_full(apt):
    errors = []
    if not validate_phone(apt.get('phoneNumber')): errors.append('invalid_phone')
    if not apt.get('appointmentDate'): errors.append('missing_date')
    if not apt.get('appointmentTime'): errors.append('missing_time')
    if not apt.get('appointmentId'): errors.append('missing_id')
    if not validate_time_window(apt.get('appointmentTime','')):
        errors.append('outside_window')
    return errors
