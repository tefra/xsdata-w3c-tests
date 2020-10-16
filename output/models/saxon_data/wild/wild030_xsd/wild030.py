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
        metadata={
            "name": "CPU",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    memory: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    monitor: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    speaker: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    any_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        }
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
        metadata={
            "name": "CPU",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    memory: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    monitor: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    speaker: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    any_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        }
    )
