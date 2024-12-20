from dataclasses import dataclass, field
from typing import ForwardRef, Optional, Union


@dataclass
class NewDataSet:
    t1_or_t2: list[Union["NewDataSet.T1", "NewDataSet.T2"]] = field(
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

    @dataclass
    class T1:
        id: Optional[str] = field(
            default=None,
            metadata={
                "name": "Id",
                "type": "Element",
                "namespace": "",
                "max_length": 5,
            },
        )

    @dataclass
    class T2:
        id: Optional[str] = field(
            default=None,
            metadata={
                "name": "Id",
                "type": "Element",
                "namespace": "",
                "max_length": 5,
            },
        )
