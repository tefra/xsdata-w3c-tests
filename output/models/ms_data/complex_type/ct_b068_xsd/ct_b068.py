from dataclasses import dataclass, field
from typing import Optional


@dataclass
class FooType:
    """
    :ivar my_element:
    :ivar my_ele2:
    :ivar attr_test:
    :ivar attr_test2:
    """
    class Meta:
        name = "fooType"

    my_element: Optional[str] = field(
        default=None,
        metadata=dict(
            name="myElement",
            type="Element",
            namespace=""
        )
    )
    my_ele2: Optional[str] = field(
        default=None,
        metadata=dict(
            name="myEle2",
            type="Element",
            namespace=""
        )
    )
    attr_test: Optional[str] = field(
        default=None,
        metadata=dict(
            name="attrTest",
            type="Attribute"
        )
    )
    attr_test2: Optional[str] = field(
        default=None,
        metadata=dict(
            name="attrTest2",
            type="Attribute"
        )
    )


@dataclass
class Root(FooType):
    class Meta:
        name = "root"