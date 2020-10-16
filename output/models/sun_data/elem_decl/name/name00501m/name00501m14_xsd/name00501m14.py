from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "ElemDecl/name"


@dataclass
class GlobalType:
    """
    :ivar main:
    """
    class Meta:
        name = "Global"
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
    """
    :ivar value:
    """
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
    """
    :ivar any_element:
    """
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
