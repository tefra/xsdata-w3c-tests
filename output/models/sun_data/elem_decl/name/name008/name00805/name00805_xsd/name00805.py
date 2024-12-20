from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "ElemDecl/name"


@dataclass
class Type:
    class Meta:
        name = "_-."
        namespace = "ElemDecl/name"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
        },
    )


@dataclass
class Type0:
    class Meta:
        name = "_-0."
        namespace = "ElemDecl/name"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
        },
    )


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "ElemDecl/name"

    low_line_hyphen_minus_full_stop: Optional[Type] = field(
        default=None,
        metadata={
            "name": "_-.",
            "type": "Element",
            "required": True,
        },
    )
    value_0: Optional[Type0] = field(
        default=None,
        metadata={
            "name": "_-0.",
            "type": "Element",
            "required": True,
        },
    )
