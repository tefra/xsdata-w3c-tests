from dataclasses import dataclass, field
from typing import Any, Optional


@dataclass
class PersonName:
    class Meta:
        name = "personName"

    title: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class SimpleName(PersonName):
    class Meta:
        name = "simpleName"

    title: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )


@dataclass
class Who(SimpleName):
    class Meta:
        name = "who"
