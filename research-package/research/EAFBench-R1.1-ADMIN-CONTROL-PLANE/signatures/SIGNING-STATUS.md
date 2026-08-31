# Signing Status

**ALL_EXECUTABLE_SCRIPTS_DIGITALLY_SIGNED:** TRUE

All `.py` files under `src/` and `tests/` are covered by detached Ed25519
signatures generated for this release and verifiable using
`release-public-key.pem`.

The private signing key is intentionally not included.

These signatures provide release-artifact integrity. They are not a substitute
for an organization-issued Authenticode/code-signing identity where such an
identity is required.
