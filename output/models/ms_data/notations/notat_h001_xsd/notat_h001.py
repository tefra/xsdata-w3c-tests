from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class Foo:
    class Meta:
        name = "foo"

    foo_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "http://foo",
        },
    )
