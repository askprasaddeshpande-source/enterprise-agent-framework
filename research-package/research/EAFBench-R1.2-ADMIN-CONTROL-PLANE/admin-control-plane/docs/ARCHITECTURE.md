# EAF Administrative Control-Plane Architecture

```text
Users / Business Processes
          |
          v
AI Agents / LLM Runtimes
          |
          v
+--------------------------------------------------+
| EAF ADMINISTRATION PLANE                         |
| registry | identity | tenant | lifecycle         |
| grants | delegation | approvals | revocation     |
| model policy | tool/MCP admission | kill switch  |
| shared policy | audit configuration              |
+--------------------------------------------------+
          |
          v
+--------------------------------------------------+
| EAF RUNTIME CONTROL PLANE                        |
| admission | authority | evidence | policy        |
| approval | execution gate | runtime guard        |
| readback | trace                                 |
+--------------------------------------------------+
          |
          v
MCP / A2A / APIs / Events / RAG
          |
          v
Authoritative Enterprise Systems
```

## Boundary rule

EAF is an administration/control layer, not a substitute for:
- native enterprise authorization;
- system-of-record truth;
- LLM intelligence;
- human accountability.
