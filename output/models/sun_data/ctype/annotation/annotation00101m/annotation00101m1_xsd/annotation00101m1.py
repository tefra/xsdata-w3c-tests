from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "annotation"


@dataclass(kw_only=True)
class Test:
    """
    This is a complex type definition.
    """


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"
        namespace = "annotation"

    any_element: None | object = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )
