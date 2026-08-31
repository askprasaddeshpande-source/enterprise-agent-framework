# EAF Architecture — Current Research Model

```text
Users / Applications / Business Processes
                    |
                    v
          AI Agents / LLM Runtimes
                    |
                    v
+---------------------------------------------------+
| EAF ADMINISTRATION PLANE                          |
| Agent Registry | Identity | Tenant | Lifecycle    |
| Capability Grants | Delegation | Approvals        |
| Revocation | Model Policy | Tool/MCP Admission    |
| Shared Policy | Kill Switch | Audit Configuration |
+---------------------------------------------------+
                    |
                    v
+---------------------------------------------------+
| EAF RUNTIME CONTROL PLANE                         |
| Admission | Evidence | Authority | Policy         |
| Approval | Execution Gate | Runtime Guard         |
| Readback | Trace | Claim/Release Gates            |
+---------------------------------------------------+
                    |
                    v
        MCP / A2A / APIs / RAG / Events
                    |
                    v
        Authoritative Enterprise Systems
```

## Architectural principle
**Intelligence does not create enterprise authority.**

## Boundary
The administration plane defines and versions administrative state.
The runtime-control plane enforces that state for a mission.
Authoritative enterprise systems retain system-of-record and native execution authority.
