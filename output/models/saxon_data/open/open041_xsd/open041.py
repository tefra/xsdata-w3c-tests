from dataclasses import dataclass, field
from typing import List
from output.models.saxon_data.open.open041_xsd.open041x import Beta


@dataclass
class Alpha:
    class Meta:
        name = "alpha"


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
