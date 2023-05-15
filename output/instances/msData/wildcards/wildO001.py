from output.models.ms_data.wildcards.wild_o001_xsd.wild_o001 import Foo


obj = Foo(
    any_attributes={
        "{http://www.w3.org/2001/XMLSchema-instance}schemaLocation": "http://foobar wildO001.xsd",
        "{http://foobar}name": "bar",
    }
)
