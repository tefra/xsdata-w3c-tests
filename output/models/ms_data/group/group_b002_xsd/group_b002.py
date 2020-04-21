from dataclasses import dataclass, field
from typing import Optional


@dataclass
class ComplexType:
    """
    :ivar x:
    """
    class Meta:
        name = "complexType"

    x: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )


@dataclass
class Elem(ComplexType):
    """
    :ivar group_elem:
    :ivar att2:
    :ivar att3:
    """
    class Meta:
        name = "elem"

    group_elem: Optional[object] = field(
        default=None,
        metadata=dict(
            name="groupElem",
            type="Element",
            namespace="",
            required=True
        )
    )
    att2: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    att3: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )


@dataclass
class Doc:
    """
    :ivar elem:
    """
    class Meta:
        name = "doc"

    elem: Optional[Elem] = field(
        default=None,
        metadata=dict(
            type="Element",
            required=True
        )
    )
