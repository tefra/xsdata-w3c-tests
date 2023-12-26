from dataclasses import dataclass, field
from typing import Optional, Union

__NAMESPACE__ = "particles"


@dataclass
class A:
    class Meta:
        name = "a"
        namespace = "particles"

    id_or_id_str: Optional[Union[int, str]] = field(
        default=None,
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
        },
    )
    name_or_type: Optional[str] = field(
        default=None,
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
        },
    )
