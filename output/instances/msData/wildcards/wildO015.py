from output.models.ms_data.wildcards.wild_o015_xsd.wild_o015 import Foo


obj = Foo(
    any_attributes={
        "{http://www.w3.org/2001/XMLSchema-instance}schemaLocation": "http://foobar wildO015.xsd",
        "{http://foobar}name": "bar",
    }
)
