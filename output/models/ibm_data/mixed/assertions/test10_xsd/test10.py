from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class BaseType:
    """
    :ivar body:
    :ivar must_understand:
    """
    class Meta:
        name = "baseType"

    body: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    must_understand: Optional[str] = field(
        default=None,
        metadata=dict(
            name="mustUnderstand",
            type="Attribute"
        )
    )


@dataclass
class DerivedType:
    """
    :ivar body:
    :ivar must_understand:
    """
    class Meta:
        name = "derivedType"

    body: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    must_understand: Optional[str] = field(
        default=None,
        metadata=dict(
            name="mustUnderstand",
            type="Attribute"
        )
    )


@dataclass
class Message(DerivedType):
    class Meta:
        name = "message"
