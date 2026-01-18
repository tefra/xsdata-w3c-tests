from __future__ import annotations

from dataclasses import dataclass, field
from typing import ForwardRef


@dataclass(kw_only=True)
class NewDataSet:
    t1_or_t2: list[NewDataSet.T1 | NewDataSet.T2] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "t1",
                    "type": ForwardRef("NewDataSet.T1"),
                    "namespace": "",
                },
                {
                    "name": "t2",
                    "type": ForwardRef("NewDataSet.T2"),
                    "namespace": "",
                },
            ),
        },
    )

    @dataclass(kw_only=True)
    class T1:
        id: None | str = field(
            default=None,
            metadata={
                "name": "Id",
                "type": "Element",
                "namespace": "",
                "max_length": 5,
            },
        )

    @dataclass(kw_only=True)
    class T2:
        id: None | str = field(
            default=None,
            metadata={
                "name": "Id",
                "type": "Element",
                "namespace": "",
                "max_length": 5,
            },
        )
