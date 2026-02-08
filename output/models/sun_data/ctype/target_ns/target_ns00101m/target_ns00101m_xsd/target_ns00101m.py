from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "targetNS"


@dataclass(kw_only=True)
class Test:
    abc: str = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
