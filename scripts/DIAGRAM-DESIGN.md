# Diagram design notes (maintainers / AI)

Not linked from the public wiki. Use when editing SVGs in `doc/assets/`.

## Audience context

- **Students** are typically **ages 7–13**, mostly Chinese heritage, learning at Sharon Chinese School on weekends.
- Draw students **smaller/shorter** than parents and teachers (see `char_student` scale in `generate-diagrams.py`).
- **Parents** are adults; **teachers** and **admin** are adults with distinct flat colors.

## Visual style

- Flat design: solid fills, rounded shapes, no emoji in exported diagrams.
- **English only** on diagram labels (The Web Design LLC developers).
- Reusable characters: `doc/assets/characters/*.svg`

## Regenerating

```bash
python3 scripts/generate-diagrams.py
python3 scripts/apply-diagrams-to-wiki.py
```

Do not add age ranges or “wiki source of truth” copy to README or vendor-facing pages.
