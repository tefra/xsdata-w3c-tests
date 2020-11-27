from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Root:
    class Meta:
        name = "root"

    element1: Optional["Root.Element1"] = field(
        default=None,
        metadata={
            "name": "Element1",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )

    @dataclass
    class Element1:
        group2_element1_or_group2_element2: List[object] = field(
            default_factory=list,
            metadata={
                "type": "Elements",
                "choices": (
                    {
                        "name": "Group2_Element1",
                        "type": str,
                        "namespace": "",
                    },
                    {
                        "name": "Group2_Element2",
                        "type": str,
                        "namespace": "",
                    },
                ),
            }
        )
