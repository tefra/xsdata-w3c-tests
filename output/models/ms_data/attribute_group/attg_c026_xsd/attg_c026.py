from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Foo:
    """
    :ivar currency:
    """
    class Meta:
        name = "foo"

    currency: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class TestElem(Foo):
    """
    :ivar model:
    :ivar age:
    :ivar att_fix:
    """
    class Meta:
        name = "testElem"

    model: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    age: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    att_fix: int = field(
        init=False,
        default=37,
        metadata={
            "name": "attFix",
            "type": "Attribute",
        }
    )


@dataclass
class DocElem:
    """
    :ivar test:
    """
    class Meta:
        name = "docElem"

    test: Optional[TestElem] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass
class Doc(DocElem):
    class Meta:
        name = "doc"
