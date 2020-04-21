from dataclasses import dataclass, field
from typing import Optional


@dataclass
class FooType:
    """
    :ivar my_element:
    :ivar attr_test:
    :ivar attr_test2:
    :ivar attr_test3:
    :ivar attr_test4:
    """
    class Meta:
        name = "fooType"

    my_element: Optional[str] = field(
        default=None,
        metadata=dict(
            name="myElement",
            type="Element",
            namespace="",
            required=True
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
    attr_test3: Optional[str] = field(
        default=None,
        metadata=dict(
            name="attrTest3",
            type="Attribute"
        )
    )
    attr_test4: Optional[str] = field(
        default=None,
        metadata=dict(
            name="attrTest4",
            type="Attribute"
        )
    )


@dataclass
class Root(FooType):
    class Meta:
        name = "root"
