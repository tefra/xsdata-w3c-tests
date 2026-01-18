from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"

    sub: list[Root.Sub] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )

    @dataclass(kw_only=True)
    class Sub:
        idelt: Root.Sub.Idelt = field(
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
            }
        )

        @dataclass(kw_only=True)
        class Idelt:
            value: int = field(
                metadata={
                    "required": True,
                }
            )
            attr: None | object = field(
                default=None,
                metadata={
                    "type": "Attribute",
                },
            )
