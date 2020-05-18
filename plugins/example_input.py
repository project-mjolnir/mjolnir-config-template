"""
Example lightweight input plugin for the Mjolnir-Config-Template.
"""

# Standard library imports
import random

# Local imports
import brokkr.pipeline.baseinput
import brokkr.utils.network


class ExamplePluginInput(brokkr.pipeline.baseinput.ValueInputStep):
    """Simulate an example Brokkr input plugin with random data."""

    def __init__(
            self,
            seed=None,
            na_chance=0.5,
            error_chance=0,
            **value_input_kwargs):
        """
        Simulate an example Brokkr input plugin with random data.

        Parameters
        ----------
        seed : int, str, bytes, bytearray or None, optional
            Seed to initialize the random number generator, as described in
            the docs for random.seed.
            The default is None, which uses the current system time.
        na_chance : float, optional
            The probability that a given data value will be NA.
            The default is 0.5.
        **value_input_kwargs : **kwargs
            Keyword arguments to pass to the ValueInputStep constructor.

        Returns
        -------
        None.

        """
        super().__init__(binary_decoder=False, **value_input_kwargs)
        self._na_chance = na_chance
        self._error_chance = error_chance

        random.seed(seed)

    def read_raw_data(self, input_data=None):
        """
        Read in raw data from an example random data source.

        Parameters
        ----------
        input_data : any, optional
            Per iteration input data passed to this function from previous
            PipelineSteps. Not used here but retained for compatibility with
            the generalized PipelineStep API. The default is None.

        Returns
        -------
        raw_data : list of [float or None]
            Output raw data as read by this function.

        """
        self.logger.debug("Reading example data")

        raw_data = []
        for data_type in self.data_types:
            try:
                raw_data_value = random.random()
                if random.random() < self._na_chance:
                    raise RuntimeError("Error reading example data!")
            except Exception as e:
                if random.random() < self._error_chance:
                    self.logger.error(
                        "%s getting data value %s on step %s: %s",
                        type(e).__name__, data_type.full_name, self.name, e)
                    self.logger.info("Error details:", exc_info=True)
                raw_data_value = None
            raw_data.append(raw_data_value)

        return raw_data
