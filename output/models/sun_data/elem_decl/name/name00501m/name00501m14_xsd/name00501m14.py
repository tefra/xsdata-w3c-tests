from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "ElemDecl/name"


@dataclass
class Main:
    class Meta:
        namespace = "ElemDecl/name"

    value: Optional[bool] = field(
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

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class Global:
    class Meta:
        namespace = "ElemDecl/name"

    main: list[Main] = field(
        default_factory=list,
        metadata={
            "name": "Main",
            "type": "Element",
            "min_occurs": 1,
        },
    )
