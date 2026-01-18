from __future__ import annotations

from dataclasses import dataclass, field
from typing import ForwardRef

__NAMESPACE__ = "particles"


@dataclass(kw_only=True)
class A:
    class Meta:
        name = "a"
        namespace = "particles"

    id_or_id_str: None | int | str = field(
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
    name_or_type: None | A.Name | A.Type = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "name",
                    "type": ForwardRef("A.Name"),
                    "namespace": "",
                },
                {
                    "name": "type",
                    "type": ForwardRef("A.Type"),
                    "namespace": "",
                },
            ),
        },
    )

    @dataclass(kw_only=True)
    class Name:
        value: str = field(
            default="",
            metadata={
                "required": True,
            },
        )

    @dataclass(kw_only=True)
    class Type:
        value: str = field(
            default="",
            metadata={
                "required": True,
            },
        )
