from __future__ import annotations

from dataclasses import dataclass, field

from output.models.saxon_data.open.open043_xsd.open043x import Alpha


@dataclass(kw_only=True)
class Beta:
    class Meta:
        name = "beta"


@dataclass(kw_only=True)
class Doc:
    class Meta:
        name = "doc"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "a",
                    "type": Alpha,
                    "namespace": "",
                },
                {
                    "name": "b",
                    "type": Beta,
                    "namespace": "",
                },
            ),
        },
    )
