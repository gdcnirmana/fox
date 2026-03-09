"""Webhook helpers.

Implements a common pattern: verify HMAC signatures on incoming webhooks.
"""

from __future__ import annotations

import hashlib
import hmac


def compute_hmac_sha256_hex(secret: str | bytes, payload: bytes) -> str:
    """Compute HMAC-SHA256 (hex digest) for payload."""

    key = secret.encode("utf-8") if isinstance(secret, str) else secret
    return hmac.new(key, payload, hashlib.sha256).hexdigest()


def verify_hmac_sha256_hex(
    *, secret: str | bytes, payload: bytes, signature_hex: str
) -> bool:
    """Verify a provided hex signature for payload.

    Uses constant-time comparison.
    """

    expected = compute_hmac_sha256_hex(secret, payload)
    # normalize common formatting issues (whitespace / casing)
    provided = signature_hex.strip().lower()
    return hmac.compare_digest(expected, provided)
