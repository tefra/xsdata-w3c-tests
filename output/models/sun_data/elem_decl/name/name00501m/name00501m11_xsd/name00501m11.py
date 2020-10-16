from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "ElemDecl/name"


@dataclass
class GlobalType:
    """
    :ivar local:
    """
    class Meta:
        name = "Global"
        namespace = "ElemDecl/name"

    local: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Local",
            "type": "Element",
            "namespace": "",
            "required": True,
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
