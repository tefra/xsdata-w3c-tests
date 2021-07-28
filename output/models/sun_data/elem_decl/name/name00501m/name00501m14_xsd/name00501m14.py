from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "ElemDecl/name"


@dataclass
class Global:
    class Meta:
        namespace = "ElemDecl/name"

    main: List[bool] = field(
        default_factory=list,
        metadata={
            "name": "Main",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class Main:
    class Meta:
        namespace = "ElemDecl/name"

    value: Optional[bool] = field(
        default=None,
        metadata={
            "required": True,
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
            "required": True,
        }
    )
