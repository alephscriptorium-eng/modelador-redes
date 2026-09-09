# SPDX-License-Identifier: GPL-3.0-or-later
"""Rutas y constantes del proyecto. Sin I/O."""

from __future__ import annotations

from pathlib import Path

PACKAGE_ROOT = Path(__file__).resolve().parent
PROJECT_ROOT = PACKAGE_ROOT.parent

MODELOS_DIR = PROJECT_ROOT / "modelos"
SITE_DIR = PROJECT_ROOT / "site"
PUBLIC_DIR = PROJECT_ROOT / "public"
DATA_DIR = PROJECT_ROOT / "data"
LICENSE = PROJECT_ROOT / "LICENSE"
LLMS = PROJECT_ROOT / "llms.md"

GITHUB_OWNER = "alephscriptorium-eng"
GITHUB_NAME = "modelador-redes"
GITHUB_BRANCH = "main"
GITHUB_REPO = f"https://github.com/{GITHUB_OWNER}/{GITHUB_NAME}"
GITHUB_BLOB = f"{GITHUB_REPO}/blob/{GITHUB_BRANCH}/"
GITHUB_TREE = f"{GITHUB_REPO}/tree/{GITHUB_BRANCH}/"
GITHUB_RAW = f"https://raw.githubusercontent.com/{GITHUB_OWNER}/{GITHUB_NAME}/{GITHUB_BRANCH}/"
PAGES_URL = f"https://{GITHUB_OWNER}.github.io/{GITHUB_NAME}/"

OASIS_REPO = "https://github.com/epsylon/oasis"
OASIS_SHA = "9a657b776fcafc7c24bf3ad61825316385ecf513"
OASIS_SHORT = OASIS_SHA[:7]

MAX_PUBLIC_FILE_BYTES = 300 * 1024


def modelo_dir(modelo_id: str, modelos_dir: Path | None = None) -> Path:
    return (modelos_dir or MODELOS_DIR) / modelo_id


def drafts_dir(modelo_id: str, modelos_dir: Path | None = None) -> Path:
    return modelo_dir(modelo_id, modelos_dir) / "drafts"


def revision_dir(modelo_id: str, modelos_dir: Path | None = None) -> Path:
    return modelo_dir(modelo_id, modelos_dir) / "revision"
