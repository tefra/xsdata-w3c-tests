from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "foo"


@dataclass
class Foo:
    class Meta:
        name = "foo"

    foo: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    bar: Optional["Foo.Bar"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )

    @dataclass
    class Bar:
        foo: Optional[object] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
            }
        )
        bar: Optional["Foo.Bar"] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
            }
        )


@dataclass
class Root(Foo):
    class Meta:
        name = "root"
        namespace = "foo"
