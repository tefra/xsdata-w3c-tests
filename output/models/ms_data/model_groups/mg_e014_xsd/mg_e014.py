from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(kw_only=True)
class PersonName:
    class Meta:
        name = "personName"

    title: None | object = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass(kw_only=True)
class SimpleName(PersonName):
    class Meta:
        name = "simpleName"

    title: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )


@dataclass(kw_only=True)
class Who(SimpleName):
    class Meta:
        name = "who"
