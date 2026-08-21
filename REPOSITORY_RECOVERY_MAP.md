# RCIRCUIT Repository Recovery Map

Last reviewed: 2026-08-21

This document defines the role of each repository in the current RCIRCUIT research workspace. It is an operational map, not a claim of technical validation.

## Repository roles

| Repository | Classification | Role | Current action |
|---|---|---|---|
| [rcircuit-phase-engine](https://github.com/jspchp63/rcircuit-phase-engine) | **Canonical** | Primary home for the falsification-oriented transport-vs-local-phase experiment, executable demonstrations, architecture, and current documentation. | Keep active. Route all new core experiments and validated documentation here. |
| [HROS-RCIRCUIT-LAB](https://github.com/jspchp63/HROS-RCIRCUIT-LAB) | **Supporting research** | Companion repository for broader HROS/RCIRCUIT concepts, early phase-computing materials, diagrams, PDFs, and concept code. | Keep active as a supporting lab. Do not duplicate the canonical engine implementation. |
| [rfc-dre-lite](https://github.com/jspchp63/rfc-dre-lite) | **Experimental / pre-demo** | Research scaffold for coherence reconstruction after failure. Metrics and framing are specified; executable reconstruction evidence is not yet present. | Keep separate. No promotion to canonical until a runnable falsification test exists. |
| [HROS-RCIRCUIT](https://github.com/jspchp63/HROS-RCIRCUIT) | **Empty** | Public repository with no content. | Leave untouched until a distinct purpose exists; otherwise archive later. |
| [HROS-RCIRCUIT-v1](https://github.com/jspchp63/HROS-RCIRCUIT-v1) | **Empty / legacy placeholder** | Private, empty versioned repository. | Do not develop here. Archive later if no unrecovered material is expected. |
| [README.md](https://github.com/jspchp63/README.md) | **Practice / unrelated** | GitHub folder-and-file practice repository. It is not the account profile README and not part of RCIRCUIT research. | Leave as practice or archive later. |
| [desktop-tutorial](https://github.com/jspchp63/desktop-tutorial) | **Empty / unrelated** | Private GitHub Desktop tutorial placeholder. | Archive later if no longer needed. |

## Canonical flow

1. **Core hypothesis, executable experiments, and current architecture** → `rcircuit-phase-engine`
2. **Broader concept material and supporting research artifacts** → `HROS-RCIRCUIT-LAB`
3. **Coherence-reconstruction hypothesis and future recovery experiments** → `rfc-dre-lite`
4. **Empty and tutorial repositories** → no new research work

## Attention now

### Priority 1 — protect the canonical repository

- Keep one entry-point README and one authoritative architecture path.
- Add new experiments only when they include a runnable command, inputs, expected outputs, and falsification conditions.
- Preserve source documents until a complete Markdown conversion has been verified.
- Avoid PRs that combine documentation cleanup, media uploads, and conceptual rewrites.

### Priority 2 — clarify the supporting lab boundary

- Label `HROS-RCIRCUIT-LAB` as supporting research.
- Link its readers to `rcircuit-phase-engine` for the current executable core.
- Retain unique historical documents and concept code; remove duplicates only after file-by-file comparison.

### Priority 3 — hold RFC-DRE Lite at experimental status

- Keep its current “no executable demo” notice.
- The next meaningful milestone is one minimal reconstruction comparison with computed CI/POR/drift outputs.
- Until then, treat planned metrics as specifications, not results.

### Priority 4 — defer empty-repository cleanup

Archiving is reversible, but it changes how repositories appear and can confuse recovery. Before archiving an empty repository, verify that no local-only branch, GitHub Desktop checkout, release, or expected upload belongs there.

## Pull-request disposition reviewed on 2026-08-21

- **PR #1 — closed, not merged.** It deleted the ComputeE PDF and replaced it with an unfilled 21-line Markdown template. This would remove the source without completing the conversion.
- **PR #2 — closed, not merged.** Despite its narrow title, it contained 50 commits and 20 changed files, including a large README rewrite, validation documents, images, and video assets. It was also not mergeable. Any useful material should be recovered in small, single-purpose PRs.

The source branches remain available for selective recovery.
