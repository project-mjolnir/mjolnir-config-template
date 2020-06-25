"""Example minimal input plugin for the Mjolnir-Config-Template."""

# Local imports
import brokkr.pipeline.baseinput


class ExampleMinimalInput(brokkr.pipeline.baseinput.ValueInputStep):
    def __init__(
            self,
            example_argument=True,
            **value_input_kwargs):
        super().__init__(binary_decoder=False, **value_input_kwargs)

         # YOUR INIT LOGIC AND ARGUMENT HANDLING HERE
        self._example_attribute = example_argument

    def read_raw_data(self, input_data=None):
        # YOUR DATA READING LOGIC HERE
        if not self._example_attribute:
            return None
        raw_data = []
        for data_type in self.data_types:
            try:
                raw_data_value = data_type.example_value
            except Exception as e:
                self.logger.error("%s occurred: %s", type(e).__name__, e)
                raw_data_value = None
            raw_data.append(raw_data_value)
        return raw_data
