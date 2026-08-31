#!/usr/bin/env python3
"""
asset_localization_report.py — לומדת נפח (STEM Chem 1 — Volume)

Hand-maintained list of image assets with Hebrew text baked into the
graphic itself (not translatable as text). There is no reliable way to
auto-detect this, so re-review new/changed images by eye and update the
ASSETS list below, then re-run this script.

This project follows a "no baked Hebrew text" rule for anything content-
related (all sentence/question/dialogue text is live HTML per project
convention — see project memory), so this list should stay short: mainly
reusable UI-chrome graphics like the check/submit button.

Usage:
    python3 translation/tools/asset_localization_report.py
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
EXPORT_DIR = ROOT / "translation" / "export"
OUT_PATH = EXPORT_DIR / "asset_localization_report.json"

ASSETS = [
    {
        "file": "assets/images/check-button.png",
        "bakedText": "צדקתי?",
        "usedInScreens": [
            "screen-6", "screen-11", "screen-12", "screen-14", "screen-16",
            "screen-18", "screen-20", "screen-24", "screen-25", "screen-28",
        ],
        "note": (
            "Reusable submit-button graphic (the check-btn <img>), used identically "
            "on every question screen. Needs one fresh Arabic export to replace "
            "everywhere it's referenced — not a per-screen translation."
        ),
    },
]


def main():
    EXPORT_DIR.mkdir(parents=True, exist_ok=True)
    out = {
        "meta": {
            "unit": "לומדת נפח — STEM כימיה 1, כיתות ז'-ח'",
            "method": (
                "Hand-reviewed by eye against index.html + assets/images/ — this "
                "project's convention keeps all question/dialogue/instruction text "
                "as live HTML (never baked into images) specifically so it can be "
                "translated as text, so this list is expected to stay short and "
                "cover only reusable UI-chrome graphics."
            ),
            "regenerate": "python3 translation/tools/asset_localization_report.py (after updating the ASSETS list by hand)",
        },
        "assets": ASSETS,
    }
    OUT_PATH.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote {OUT_PATH} — {len(ASSETS)} asset(s)")


if __name__ == "__main__":
    main()
