from dataclasses import dataclass


@dataclass
class Foo:
    class Meta:
        name = "foo"


@dataclass
class FixedType(Foo):
    class Meta:
        name = "fixedType"


@dataclass
class Root(Foo):
    class Meta:
        name = "root"
