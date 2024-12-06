from dataclasses import dataclass, field

__NAMESPACE__ = "http://foobar"


@dataclass
class Bar:
    class Meta:
        name = "bar"
        namespace = "http://foobar"

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
        namespace = "http://foobar"

    a_b_c_d_e_target_namespace_local_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "A B C D E ##targetNamespace ##local",
        },
    )
