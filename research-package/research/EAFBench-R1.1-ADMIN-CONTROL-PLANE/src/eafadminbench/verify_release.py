from __future__ import annotations
import base64, hashlib, json
from pathlib import Path
from cryptography.hazmat.primitives import serialization

def main():
    root = Path(__file__).resolve().parents[2]
    pub = serialization.load_pem_public_key((root / "signatures" / "release-public-key.pem").read_bytes())

    # Verify executable scripts.
    scripts = sorted((root / "src").rglob("*.py")) + sorted((root / "tests").rglob("*.py"))
    for p in scripts:
        sig_path = root / "signatures" / (p.relative_to(root).as_posix().replace("/", "__") + ".sig")
        sig = base64.b64decode(sig_path.read_text(encoding="ascii"))
        pub.verify(sig, p.read_bytes())

    # Verify signed manifest.
    manifest_path = root / "evidence" / "SHA256SUMS.json"
    manifest_sig = base64.b64decode((root / "signatures" / "SHA256SUMS.json.sig").read_text(encoding="ascii"))
    pub.verify(manifest_sig, manifest_path.read_bytes())

    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    for item in manifest["entries"]:
        p = root / item["path"]
        digest = hashlib.sha256(p.read_bytes()).hexdigest()
        if digest != item["sha256"]:
            raise SystemExit(f"HASH_MISMATCH:{item['path']}")

    print(f"RELEASE_SIGNATURES=VALID scripts={len(scripts)} files={len(manifest['entries'])}")

if __name__ == "__main__":
    main()
