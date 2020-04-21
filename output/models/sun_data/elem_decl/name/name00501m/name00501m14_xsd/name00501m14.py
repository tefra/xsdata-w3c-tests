from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "ElemDecl/name"


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


@dataclass
class GlobalType:
    """
    :ivar main:
    """
    class Meta:
        name = "Global"
        namespace = "ElemDecl/name"

    main: List[Main] = field(
        default_factory=list,
        metadata=dict(
            name="Main",
            type="Element",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
