from dataclasses import dataclass, field

__NAMESPACE__ = "http://xsdtesting"


@dataclass
class B:
    class Meta:
        name = "b"
        namespace = "http://xsdtesting"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass
class Foo:
    class Meta:
        name = "foo"
        namespace = "http://xsdtesting"

    target_namespace_w3_org_1999_xhtml_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##targetNamespace http://www.w3.org/1999/xhtml",
        },
    )
