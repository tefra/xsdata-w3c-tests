from dataclasses import dataclass, field

__NAMESPACE__ = "http://xsdtesting"


@dataclass
class AnyType:
    class Meta:
        name = "any"

    any_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "max_occurs": 100,
        },
    )


@dataclass
class Doc:
    class Meta:
        name = "doc"
        namespace = "http://xsdtesting"

    elem: list[AnyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 100,
        },
    )


@dataclass
class Foo(AnyType):
    class Meta:
        name = "foo"
        namespace = "http://xsdtesting"
