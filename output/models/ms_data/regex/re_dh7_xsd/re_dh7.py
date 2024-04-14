from dataclasses import dataclass, field
from typing import ForwardRef, List, Optional, Union


@dataclass
class Doc:
    class Meta:
        name = "doc"

    id_or_elem: List[Union["Doc.Id", str]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ID",
                    "type": ForwardRef("Doc.Id"),
                    "namespace": "",
                    "max_occurs": 2,
                },
                {
                    "name": "elem",
                    "type": str,
                    "namespace": "",
                    "pattern": r"\c[\c\d]*",
                },
            ),
        },
    )

    @dataclass
    class Id:
        att: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )
