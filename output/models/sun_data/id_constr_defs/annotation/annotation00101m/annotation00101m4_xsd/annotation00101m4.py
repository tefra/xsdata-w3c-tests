from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "IdConstrDefs/annotation"


@dataclass
class People:
    class Meta:
        name = "people"
        namespace = "IdConstrDefs/annotation"

    person: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        },
    )


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "IdConstrDefs/annotation"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )
