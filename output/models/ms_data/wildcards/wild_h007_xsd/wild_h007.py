from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class Foo:
    class Meta:
        name = "foo"

    w3_org_1999_xhtml_element: None | object = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "http://www.w3.org/1999/xhtml",
        },
    )
