from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

__NAMESPACE__ = "http://xsdtesting"


@dataclass(kw_only=True)
class B:
    local_target_namespace_foo_imported_xsd_bar_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": (
                "##local ##targetNamespace foo http://importedXSD bar"
            ),
            "max_occurs": 4,
        },
    )


@dataclass(kw_only=True)
class R(B):
    local_target_namespace_foo_imported_xsd_bar_element: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    e1: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 2,
            "max_occurs": 3,
        },
    )


@dataclass(kw_only=True)
class Doc:
    class Meta:
        name = "doc"
        namespace = "http://xsdtesting"

    elem: None | R = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
