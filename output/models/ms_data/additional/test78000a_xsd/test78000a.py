from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "a"


@dataclass(kw_only=True)
class LaxContainerType:
    other_element: None | object = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
        },
    )


@dataclass(kw_only=True)
class SkipContainerType:
    other_element: None | object = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
            "process_contents": "skip",
        },
    )


@dataclass(kw_only=True)
class StrictContainerType:
    other_element: None | object = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
        },
    )


@dataclass(kw_only=True)
class LaxContainer(LaxContainerType):
    class Meta:
        namespace = "a"


@dataclass(kw_only=True)
class SkipContainer(SkipContainerType):
    class Meta:
        namespace = "a"


@dataclass(kw_only=True)
class StrictContainer(StrictContainerType):
    class Meta:
        namespace = "a"


@dataclass(kw_only=True)
class RootContainerType:
    strict_container: None | StrictContainer = field(
        default=None,
        metadata={
            "name": "StrictContainer",
            "type": "Element",
            "namespace": "a",
        },
    )
    lax_container: None | LaxContainer = field(
        default=None,
        metadata={
            "name": "LaxContainer",
            "type": "Element",
            "namespace": "a",
        },
    )
    skip_container: None | SkipContainer = field(
        default=None,
        metadata={
            "name": "SkipContainer",
            "type": "Element",
            "namespace": "a",
        },
    )


@dataclass(kw_only=True)
class RootContainer(RootContainerType):
    class Meta:
        namespace = "a"


@dataclass(kw_only=True)
class Doc:
    class Meta:
        name = "doc"
        namespace = "a"

    root_container: list[RootContainer] = field(
        default_factory=list,
        metadata={
            "name": "RootContainer",
            "type": "Element",
            "max_occurs": 100,
        },
    )
