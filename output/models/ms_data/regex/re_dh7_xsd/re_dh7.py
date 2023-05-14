from dataclasses import dataclass, field
from typing import List, Optional, Type


@dataclass
class Doc:
    class Meta:
        name = "doc"

    id_or_elem: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ID",
                    "type": Type["Doc.Id"],
                    "namespace": "",
                },
                {
                    "name": "elem",
                    "type": str,
                    "namespace": "",
                    "pattern": r"\c[\c\d]*",
                },
            ),
        }
    )

    @dataclass
    class Id:
        att: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
            }
        )
