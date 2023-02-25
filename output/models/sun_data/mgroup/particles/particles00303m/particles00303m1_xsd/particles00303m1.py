from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "particles"


@dataclass
class A:
    class Meta:
        name = "a"
        namespace = "particles"

    id_or_id_str: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "id",
                    "type": int,
                    "namespace": "",
                },
                {
                    "name": "id_str",
                    "type": str,
                    "namespace": "",
                },
            ),
            "max_occurs": 2,
        }
    )
    name_or_type: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "name",
                    "type": str,
                    "namespace": "",
                },
                {
                    "name": "type",
                    "type": str,
                    "namespace": "",
                },
            ),
            "max_occurs": 2,
        }
    )
