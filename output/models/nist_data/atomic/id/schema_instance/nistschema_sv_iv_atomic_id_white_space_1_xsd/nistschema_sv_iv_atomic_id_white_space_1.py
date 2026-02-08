from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-ID-whiteSpace-1-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicIdWhiteSpace1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-ID-whiteSpace-1"
        namespace = "NISTSchema-SV-IV-atomic-ID-whiteSpace-1-NS"

    value: str = field(
        default="",
        metadata={
            "white_space": "collapse",
        },
    )


@dataclass(kw_only=True)
class Out:
    class Meta:
        name = "out"
        namespace = "NISTSchema-SV-IV-atomic-ID-whiteSpace-1-NS"

    any_element: None | object = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )
