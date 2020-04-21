from dataclasses import dataclass


@dataclass
class Foo:
    class Meta:
        name = "foo"


@dataclass
class Root(Foo):
    class Meta:
        name = "root"
