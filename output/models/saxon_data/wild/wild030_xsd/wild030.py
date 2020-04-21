from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Computer:
    """
    :ivar cpu:
    :ivar memory:
    :ivar monitor:
    :ivar speaker:
    :ivar any_element:
    """
    class Meta:
        name = "computer"

    cpu: Optional[str] = field(
        default=None,
        metadata=dict(
            name="CPU",
            type="Element",
            namespace="",
            required=True
        )
    )
    memory: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )
    monitor: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )
    speaker: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace=""
        )
    )
    any_element: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Wildcard",
            namespace="##any",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )


@dataclass
class QuietComputer:
    """
    :ivar cpu:
    :ivar memory:
    :ivar monitor:
    :ivar speaker:
    :ivar any_element:
    """
    class Meta:
        name = "quietComputer"

    cpu: Optional[str] = field(
        default=None,
        metadata=dict(
            name="CPU",
            type="Element",
            namespace="",
            required=True
        )
    )
    memory: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )
    monitor: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )
    speaker: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace=""
        )
    )
    any_element: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Wildcard",
            namespace="##any",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
