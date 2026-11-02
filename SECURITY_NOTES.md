# Security notes

- TLS: must fail if verification cannot be enabled
- Auth: CALL-E API key separate from SIMRS credentials
- Writeback: needs SIMRS auth header; idempotent PATCH
- Logging: mask phones/tokens/keys; truncate transcripts
- Emergency: handled during call flow
- Retries: contact retries separate from technical retries
