from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://xstest-tns"


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"
        namespace = "http://xstest-tns"

    meeting: list[Root.Meeting] = field(
        default_factory=list,
        metadata={
            "name": "Meeting",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        },
    )

    @dataclass(kw_only=True)
    class Meeting:
        beverage: str | int = field(
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
            }
        )
        end_time: None | int = field(
            default=None,
            metadata={
                "name": "end-time",
                "type": "Attribute",
            },
        )
