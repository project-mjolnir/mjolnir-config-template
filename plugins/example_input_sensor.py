"""Example minimal sensor class plugin for the Mjolnir-Config-Template."""

# Local imports
import brokkr.pipeline.baseinput


class ExampleSensorClass():
    """An example sensor simulating (user-provided) data attributes."""

    def __init__(self, attribute_dict=None, as_methods=False):
        """
        Generate an example sensor class object with the specified attributes.

        Parameters
        ----------
        attribute_dict : dict or None, optional
            The attribute dictionary to add to the example sensor.
            The default is None, which adds no attributes.
        as_methods : bool, optional
            If True, the passed attributes will be created as methods
            instead of as properties. The default is False.

        Returns
        -------
        None.

        """
        if attribute_dict is None:
            attribute_dict = {}
        for attribute_key, attribute_value in attribute_dict.items():
            if as_methods:
                setattr(self, attribute_key, lambda val=attribute_value: val)
            else:
                setattr(self, attribute_key, attribute_value)


class ExampleSensorPropertyInput(brokkr.pipeline.baseinput.PropertyInputStep):
    """Thin shim class to load ExampleSensorClass for use with Brokkr."""

    def __init__(self, **property_input_kwargs):
        """
        Thin shim class to load ExampleSensorClass for use with Brokkr.

        Parameters
        ----------
        **property_input_kwargs : kwargs
            Keyward arguments to pass to the PropertyInputStep constructor.

        Returns
        -------
        None.

        """
        super().__init__(
            sensor_class=ExampleSensorClass, **property_input_kwargs)


class ExampleSensorFunctionInput(brokkr.pipeline.baseinput.MethodInputStep):
    """Thin shim class to load ExampleSensorClass for use with Brokkr."""

    def __init__(self, **method_input_kwargs):
        """
        Thin shim class to load ExampleSensorClass for use with Brokkr.

        Parameters
        ----------
        **method_input_kwargs : kwargs
            Keyward arguments to pass to the MethodInputStep constructor.

        Returns
        -------
        None.

        """
        super().__init__(
            sensor_class=ExampleSensorClass, **method_input_kwargs)
