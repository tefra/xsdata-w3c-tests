from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "importedXSD"


@dataclass(kw_only=True)
class Foo:
    class Meta:
        name = "foo"
        namespace = "importedXSD"

    any_element: None | object = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )
