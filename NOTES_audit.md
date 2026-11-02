# Audit notes

- TLS: remove CERT_NONE fallback; fail explicitly
- Masking: centralize phone/token/key sanitization
- Validation: phone E.164, date/time, timezone, calling window 08:00-20:00
- Classification: separate technical vs conversation outcome; failed != confirmed
- Emergency: detect and handle during call flow
- Writeback: require SIMRS auth, idempotent
- State: persist to avoid duplicates
- Retry: 2 attempts max, >=2h apart, respect window
- Reports: truncate transcripts
