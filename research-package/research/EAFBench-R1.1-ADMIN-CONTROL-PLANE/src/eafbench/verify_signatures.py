from __future__ import annotations
import base64, sys
from pathlib import Path

try:
    from cryptography.hazmat.primitives import serialization
    from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PublicKey
except Exception as exc:
    raise SystemExit("cryptography package is required for signature verification") from exc

def main():
    root = Path(__file__).resolve().parents[2]
    pub_path = root / "signatures" / "release-public-key.pem"
    pub = serialization.load_pem_public_key(pub_path.read_bytes())
    failures = []
    scripts = sorted((root / "src").rglob("*.py"))
    scripts += sorted((root / "tests").rglob("*.py"))
    for p in scripts:
        sig_path = root / "signatures" / (p.relative_to(root).as_posix().replace("/", "__") + ".sig")
        if not sig_path.exists():
            failures.append(f"MISSING_SIGNATURE:{p.relative_to(root)}")
            continue
        sig = base64.b64decode(sig_path.read_text(encoding="ascii").strip())
        try:
            pub.verify(sig, p.read_bytes())
        except Exception:
            failures.append(f"INVALID_SIGNATURE:{p.relative_to(root)}")
    if failures:
        for f in failures:
            print(f)
        raise SystemExit(1)
    print(f"SCRIPT_SIGNATURES=VALID count={len(scripts)}")

if __name__ == "__main__":
    main()
