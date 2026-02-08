from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class Employees:
    employee: int = field(
        default=1,
        metadata={
            "name": "Employee",
            "type": "Element",
            "namespace": "",
        },
    )
    dept: int = field(
        default=9,
        metadata={
            "name": "Dept",
            "type": "Attribute",
        },
    )
