from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "ElemDecl/name"


@dataclass
class Global1:
    class Meta:
        namespace = "ElemDecl/name"

    value: str = field(
        default="",
        metadata={
            "pattern": r"false",
        }
    )


@dataclass
class Global2:
    class Meta:
        namespace = "ElemDecl/name"

    value: str = field(
        default="",
        metadata={
            "pattern": r"false",
        }
    )


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "ElemDecl/name"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        }
    )
