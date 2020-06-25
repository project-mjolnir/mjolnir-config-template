"""Example minimal sensor class plugin for the Mjolnir-Config-Template."""

# Local imports
import brokkr.pipeline.baseinput


class ExampleSensorClass():
    def __init__(self, attribute_dict=None, as_methods=False):
        attribute_dict = {} if attribute_dict is None else attribute_dict
        for attribute_key, attribute_value in attribute_dict.items():
            if as_methods:
                setattr(self, attribute_key, lambda val=attribute_value: val)
            else:
                setattr(self, attribute_key, attribute_value)


class ExampleSensorPropertyInput(brokkr.pipeline.baseinput.PropertyInputStep):
    def __init__(self, **property_input_kwargs):
        super().__init__(
            sensor_class=ExampleSensorClass, **property_input_kwargs)


class ExampleSensorFunctionInput(brokkr.pipeline.baseinput.MethodInputStep):
    def __init__(self, **method_input_kwargs):
        super().__init__(
            sensor_class=ExampleSensorClass, **method_input_kwargs)
