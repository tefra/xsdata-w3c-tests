from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class ParentType:
    """
    :ivar child:
    :ivar grandchild:
    """
    child: Optional["ParentType.Child"] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace=""
        )
    )
    grandchild: Optional["ParentType.Grandchild"] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace=""
        )
    )

    @dataclass
    class Child:
        """
        :ivar name:
        :ivar dob:
        """
        name: Optional[str] = field(
            default=None,
            metadata=dict(
                type="Attribute"
            )
        )
        dob: Optional[str] = field(
            default=None,
            metadata=dict(
                type="Attribute"
            )
        )

    @dataclass
    class Grandchild:
        """
        :ivar name:
        :ivar dob:
        """
        name: Optional[str] = field(
            default=None,
            metadata=dict(
                type="Attribute"
            )
        )
        dob: Optional[str] = field(
            default=None,
            metadata=dict(
                type="Attribute"
            )
        )


@dataclass
class TimerType:
    """
    :ivar time:
    :ivar iterations:
    """
    time: Optional[int] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    iterations: Optional[int] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )


@dataclass
class Data:
    """
    :ivar timer:
    :ivar parent:
    """
    class Meta:
        name = "data"

    timer: List[TimerType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="",
            min_occurs=1,
            max_occurs=3
        )
    )
    parent: List[ParentType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="",
            min_occurs=1,
            max_occurs=5
        )
    )
