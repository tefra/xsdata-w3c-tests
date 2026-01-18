from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class Elt1:
    class Meta:
        name = "elt1"

    elt2: None | object = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    elt3: None | object = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    elt4: None | object = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
