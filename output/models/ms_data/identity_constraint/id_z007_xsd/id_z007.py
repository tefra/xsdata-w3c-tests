from dataclasses import dataclass, field
from typing import List, Optional, Type


@dataclass
class NewDataSet:
    t1_or_t2: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "t1",
                    "type": Type["NewDataSet.T1"],
                    "namespace": "",
                },
                {
                    "name": "t2",
                    "type": Type["NewDataSet.T2"],
                    "namespace": "",
                },
            ),
        }
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
            }
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
            }
        )
