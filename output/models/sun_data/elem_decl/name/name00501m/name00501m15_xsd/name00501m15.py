from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "ElemDecl/name"


@dataclass
class GlobalType:
    """
    :ivar main:
    """
    class Meta:
        name = "Global"
        namespace = "ElemDecl/name"

    main: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="Main",
            type="Element",
            required=True
        )
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
        metadata=dict(
            required=True
        )
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
        metadata=dict(
            type="Wildcard",
            namespace="##any",
            required=True
        )
    )
