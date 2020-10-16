from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class NewDataSet:
    """
    :ivar t1:
    :ivar t2:
    """
    t1: List["NewDataSet.T1"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    t2: List["NewDataSet.T2"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )

    @dataclass
    class T1:
        """
        :ivar id:
        """
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
        """
        :ivar id:
        """
        id: Optional[str] = field(
            default=None,
            metadata={
                "name": "Id",
                "type": "Element",
                "namespace": "",
                "max_length": 5,
            }
        )
