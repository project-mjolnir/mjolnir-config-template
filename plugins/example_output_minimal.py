"""Example ultra-minimal output plugin for the Mjolnir-Config-Template."""

# Local imports
import brokkr.pipeline.base


class ExamplePluginOutput(brokkr.pipeline.base.OutputStep):
    def __init__(self, **output_step_kwargs):
        # Pass arguments to superclass init
        super().__init__(**output_step_kwargs)

        # Further setup at descretion of plugin author
        self._previous_data = None

    def execute(self, input_data=None):
        # Function contents at plugin author descretion
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
