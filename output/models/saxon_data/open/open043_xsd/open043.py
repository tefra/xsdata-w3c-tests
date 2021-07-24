from dataclasses import dataclass, field
from typing import List
from output.models.saxon_data.open.open043_xsd.open043x import Alpha


@dataclass
class Beta:
    class Meta:
        name = "beta"


@dataclass
class Doc:
    class Meta:
        name = "doc"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "a",
                    "type": Alpha,
                    "namespace": "",
                },
                {
                    "name": "b",
                    "type": Beta,
                    "namespace": "",
                },
            ),
        }
    )
