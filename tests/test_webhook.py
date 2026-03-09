import unittest


from src.services.webhook import compute_hmac_sha256_hex, verify_hmac_sha256_hex


class TestWebhook(unittest.TestCase):
    def test_compute_and_verify(self):
        secret = "topsecret"
        payload = b"hello world"
        sig = compute_hmac_sha256_hex(secret, payload)
        self.assertTrue(
            verify_hmac_sha256_hex(secret=secret, payload=payload, signature_hex=sig)
        )

    def test_verify_rejects_bad_signature(self):
        self.assertFalse(
            verify_hmac_sha256_hex(
                secret="s", payload=b"p", signature_hex="00" * 32  # 64 hex chars
            )
        )


if __name__ == "__main__":
    unittest.main()
