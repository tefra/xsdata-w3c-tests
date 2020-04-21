from dataclasses import dataclass, field
from typing import Optional


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

    timer: Optional[TimerType] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )
    parent: Optional[ParentType] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )
