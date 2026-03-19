"""Configuration management for EthicsCheck."""
from __future__ import annotations

import os
from pathlib import Path
from typing import Any

import yaml
from pydantic import BaseModel, Field

from .models import Framework, Severity

CONFIG_FILENAMES = [".ethicscheck.yaml", ".ethicscheck.yml", "ethicscheck.yaml"]


class EthicsCheckConfig(BaseModel):
    frameworks: list[Framework] = Field(default_factory=lambda: [Framework.EU_AI_ACT, Framework.NIST_RMF])
    fail_on: Severity = Severity.HIGH
    output_format: str = "terminal"  # terminal | json | sarif
    model_card_path: str | None = None
    technical_docs_path: str | None = None
    risk_assessment_path: str | None = None
    data_governance_path: str | None = None
    custom_checks: list[str] = Field(default_factory=list)
    skip_checks: list[str] = Field(default_factory=list)


def find_config(start_dir: Path | None = None) -> Path | None:
    """Walk up directories looking for a config file."""
    directory = start_dir or Path.cwd()
    for parent in [directory, *directory.parents]:
        for name in CONFIG_FILENAMES:
            candidate = parent / name
            if candidate.exists():
                return candidate
    return None


def load_config(config_path: Path | None = None) -> EthicsCheckConfig:
    """Load config from file, environment variables, and defaults."""
    path = config_path or find_config()
    data: dict[str, Any] = {}
    if path and path.exists():
        with open(path) as f:
            data = yaml.safe_load(f) or {}
    # Environment variable overrides
    if env_frameworks := os.environ.get("ETHICSCHECK_FRAMEWORKS"):
        data["frameworks"] = [f.strip() for f in env_frameworks.split(",")]
    if env_fail_on := os.environ.get("ETHICSCHECK_FAIL_ON"):
        data["fail_on"] = env_fail_on
    return EthicsCheckConfig(**data)
