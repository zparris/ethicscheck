"""Plugin discovery for EthicsCheck.

Third-party plugins register themselves via the ``ethicscheck.frameworks``
entry-point group in their ``pyproject.toml``:

.. code-block:: toml

    [project.entry-points."ethicscheck.frameworks"]
    callchain = "ethicscheck_callchain:AICallChainFramework"

The value must be a dotted import path that resolves to a
:class:`~ethicscheck.frameworks.base.BaseFramework` subclass.

EthicsCheck will discover and load every registered plugin automatically —
no changes to EthicsCheck's own source code are required.
"""
from __future__ import annotations

import importlib.metadata
from typing import TYPE_CHECKING

from rich.console import Console

if TYPE_CHECKING:
    from .frameworks.base import BaseFramework

_ENTRY_POINT_GROUP = "ethicscheck.frameworks"

_console = Console(stderr=True)


def discover_plugins() -> dict[str, type["BaseFramework"]]:
    """Return a mapping of plugin name → framework class for all installed plugins.

    Plugins that fail to import are skipped with a warning printed to *stderr*
    so that a broken plugin never prevents the core tool from running.
    """
    plugins: dict[str, type["BaseFramework"]] = {}

    try:
        eps = importlib.metadata.entry_points(group=_ENTRY_POINT_GROUP)
    except Exception:  # pragma: no cover — only fails on broken stdlib
        return plugins

    for ep in eps:
        try:
            fw_class = ep.load()
            plugins[ep.name] = fw_class
        except Exception as exc:  # noqa: BLE001
            _console.print(
                f"[yellow]⚠ EthicsCheck: plugin '{ep.name}' failed to load "
                f"and will be skipped.[/yellow]\n  {type(exc).__name__}: {exc}"
            )

    return plugins
