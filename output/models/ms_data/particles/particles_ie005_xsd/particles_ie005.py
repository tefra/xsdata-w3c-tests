from dataclasses import dataclass

__NAMESPACE__ = "http://xsdtesting"


@dataclass
class Base:
    class Meta:
        name = "base"


@dataclass
class Testing(Base):
    class Meta:
        name = "testing"


@dataclass
class Doc(Testing):
    class Meta:
        name = "doc"
        namespace = "http://xsdtesting"
