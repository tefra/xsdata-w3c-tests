from __future__ import annotations

from dataclasses import dataclass, field

from output.models.saxon_data.open.open041_xsd.open041x import Beta


@dataclass(kw_only=True)
class Alpha:
    class Meta:
        name = "alpha"


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
