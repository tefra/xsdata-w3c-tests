from dataclasses import dataclass, field
from typing import Optional


@dataclass
class RootType:
    """
    :ivar date_ele:
    """
    class Meta:
        name = "rootType"

    date_ele: Optional[str] = field(
        default=None,
        metadata={
            "name": "dateEle",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass
class Root(RootType):
    class Meta:
        name = "root"
