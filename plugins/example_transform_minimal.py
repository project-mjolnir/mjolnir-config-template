"""Example ultra-minimal transform plugin for the Mjolnir-Config-Template."""

# Local imports
import brokkr.pipeline.base


class ExampleTransformPlugin(brokkr.pipeline.base.TransformStep):
    def __init__(self, **transform_step_kwargs):
        # Pass arguments to superclass init
        super().__init__(**transform_step_kwargs)

        # YOUR __INIT__ CODE HERE
        self._previous_data = None

    def execute(self, input_data=None):
        # YOUR EXECUTE CODE HERE
        if self._previous_data is None:
            self._previous_data = input_data
        if (input_data['example_bool'].value
                != self._previous_data['example_bool'].value):
            self.logger.info("Zoinks! Example_bool changed from %s to %s",
                             input_data['example_bool'].value,
                             self._previous_data['example_bool'].value)
        self._previous_data = input_data

        # Passthrough the input for consumption by any further steps
        return input_data
