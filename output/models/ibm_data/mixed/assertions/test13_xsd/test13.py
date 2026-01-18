from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class Example:
    even_number: int = field(
        metadata={
            "name": "even-number",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
