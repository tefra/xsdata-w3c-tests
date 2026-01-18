from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

__NAMESPACE__ = "http://xsdtesting"


@dataclass(kw_only=True)
class B:
    foo_imported_xsd_bar_element: None | object = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "foo http://importedXSD bar",
        },
    )


@dataclass(kw_only=True)
class R(B):
    foo_imported_xsd_bar_element: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
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
