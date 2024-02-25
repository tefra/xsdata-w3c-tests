from dataclasses import dataclass, field
from typing import Optional, Type, Union

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
    name_or_type: Optional[Union["A.Name", "A.TypeType"]] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "name",
                    "type": Type["A.Name"],
                    "namespace": "",
                },
                {
                    "name": "type",
                    "type": Type["A.TypeType"],
                    "namespace": "",
                },
            ),
        },
    )

    @dataclass
    class Name:
        value: Optional[str] = field(
            default=None,
            metadata={
                "required": True,
            },
        )

    @dataclass
    class TypeType:
        value: Optional[str] = field(
            default=None,
            metadata={
                "required": True,
            },
        )
