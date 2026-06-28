# AGENTS.md

## Cursor Cloud specific instructions

This is a **pure-Python learning repository** (gold-shop / accounting curriculum, week 1–4).
There is no web server, no GUI, no framework (Django not added yet), and no package manager.

### Environment
- Runs on the system `python3` (Python 3.12 in the cloud VM). `.cursorrules` mentions 3.14, but that is the author's local Mac; any Python 3.10+ runs everything here.
- **Zero third-party dependencies.** Every script only imports the standard library (`decimal`, `sqlite3`, `random`). There is nothing to `pip install`, so the update script is a no-op verification.

### Running scripts
- Scripts are standalone and run directly, e.g. `python3 haftte3/capstone_hafte3.py`.
- Best end-to-end demo (gold-shop accounting domain models): `python3 haftte3/capstone_hafte3.py`.
- SQLite demo: run from inside its folder so relative DB paths resolve, e.g. `cd hafte4 && python3 oop_db.py`.
- **Several scripts are interactive** (use `input()`): `hafte1/calculator.py`, `hafte1/invoice.py`, `hafte1/discount.py`, `hafte1/temp_age.py`, `hafte1/loops.py`, and a few in `hafte2`/`hafte4`. Pipe stdin to run them non-interactively, e.g. `printf '1\n10.5\n5.25\n5\n' | python3 hafte1/calculator.py`.

### Notes / gotchas
- Running `hafte4` scripts **creates new `.db` files** (e.g. `tala.db`, `tala_oop.db`) in the working directory. These are scratch artifacts; delete them before committing unless intentionally tracked. Note `tala_oop.db` and `join_tala.db` are already committed.
- No lint config and no automated test framework exist. "Testing" means running a script and inspecting its printed output. Use `python3 -m py_compile <file>` for a quick syntax check.
- Domain rule (from `.cursorrules`): gold value formula is `vazn * ayar / 750 * gheymat_geram`; always use `Decimal` from strings, never `float`.
