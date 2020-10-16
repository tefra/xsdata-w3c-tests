from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Test:
    """
    :ivar complex_att1:
    :ivar complex_att2:
    :ivar global_att1:
    :ivar item1:
    :ivar item2:
    :ivar global_att2:
    :ivar foo1:
    :ivar foo2:
    :ivar global_att3:
    :ivar foo3:
    :ivar item3:
    :ivar complex_att3:
    """
    class Meta:
        name = "test"

    complex_att1: Optional[int] = field(
        default=None,
        metadata={
            "name": "complexAtt1",
            "type": "Attribute",
        }
    )
    complex_att2: Optional[int] = field(
        default=None,
        metadata={
            "name": "complexAtt2",
            "type": "Attribute",
        }
    )
    global_att1: Optional[int] = field(
        default=None,
        metadata={
            "name": "globalAtt1",
            "type": "Attribute",
        }
    )
    item1: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    item2: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    global_att2: Optional[int] = field(
        default=None,
        metadata={
            "name": "globalAtt2",
            "type": "Attribute",
        }
    )
    foo1: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    foo2: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    global_att3: Optional[int] = field(
        default=None,
        metadata={
            "name": "globalAtt3",
            "type": "Attribute",
        }
    )
    foo3: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    item3: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    complex_att3: Optional[int] = field(
        default=None,
        metadata={
            "name": "complexAtt3",
            "type": "Attribute",
        }
    )


@dataclass
class Doc:
    """
    :ivar test:
    """
    class Meta:
        name = "doc"

    test: Optional[Test] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
