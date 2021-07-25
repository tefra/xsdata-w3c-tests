from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "a"


@dataclass
class LaxContainerType:
    other_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
        }
    )


@dataclass
class SkipContainerType:
    other_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
        }
    )


@dataclass
class StrictContainerType:
    other_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
        }
    )


@dataclass
class LaxContainer(LaxContainerType):
    class Meta:
        namespace = "a"


@dataclass
class SkipContainer(SkipContainerType):
    class Meta:
        namespace = "a"


@dataclass
class StrictContainer(StrictContainerType):
    class Meta:
        namespace = "a"


@dataclass
class RootContainerType:
    strict_container: Optional[StrictContainer] = field(
        default=None,
        metadata={
            "name": "StrictContainer",
            "type": "Element",
            "namespace": "a",
        }
    )
    lax_container: Optional[LaxContainer] = field(
        default=None,
        metadata={
            "name": "LaxContainer",
            "type": "Element",
            "namespace": "a",
        }
    )
    skip_container: Optional[SkipContainer] = field(
        default=None,
        metadata={
            "name": "SkipContainer",
            "type": "Element",
            "namespace": "a",
        }
    )


@dataclass
class RootContainer(RootContainerType):
    class Meta:
        namespace = "a"


@dataclass
class Doc:
    class Meta:
        name = "doc"
        namespace = "a"

    root_container: List[RootContainer] = field(
        default_factory=list,
        metadata={
            "name": "RootContainer",
            "type": "Element",
            "max_occurs": 100,
        }
    )
