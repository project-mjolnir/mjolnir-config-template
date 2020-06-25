"""
Example conditional-action transform plugin for the Mjolnir-Config-Template.
"""

# Local imports
import brokkr.pipeline.base
import brokkr.pipeline.decode


class ExampleTransformPlugin(brokkr.pipeline.base.TransformStep):
    """Demo a Mjolnir transform plugin, executing an action on a condition."""

    def __init__(self, expression, **transform_step_kwargs):
        """
        Demo a Mjolnir transform plugin, executing an action on a condition.

        Parameters
        ----------
        expression : str
            The simplified Python expression to evaluate.
        transform_step_kwargs : **kwargs, optional
            Keyword arguments to pass to the TransformStep constructor.

        Returns
        -------
        None.

        """
        # Pass arguments to superclass init
        super().__init__(**transform_step_kwargs)

        # Setup simpleeval parser and class initial state
        self._eval_parser = brokkr.pipeline.decode.generate_eval_parser()
        self._expression = expression
        self._previous_data = None

    def execute(self, input_data=None):
        """
        Executing an action upon detection an arbitrary condition in the data.

        Parameters
        ----------
        input_data : any, optional
            Per iteration input data passed to this function from previous
            PipelineSteps. Not used here but retained for compatibility with
            the generalized PipelineStep API. The default is None.

        Returns
        -------
        input_data : same as input_data
            Input data passed through unchanged, for further steps to consume.

        """
        # Handle first iteration
        if self._previous_data is None:
            self._previous_data = input_data
        # Set the variables visible to the parser
        self._eval_parser.names["current_data"] = input_data
        self._eval_parser.names["previous_data"] = self._previous_data
        # Check the result of the expression on these data
        try:
            if self._eval_parser.eval(self._expression):
                # Take some action
                self.logger.info("Zoinks! %s is true!", self._expression)
        # If expression evaluation fails, presumably due to bad data values
        except Exception as e:
            self.logger.error(
                "%s evaluating expression %r in %s on step %s: %s",
                type(e).__name__, self._expression, type(self), self.name, e)
            self.logger.info("Error details:", exc_info=True)
            for pretty_name, data in [("Current", input_data),
                                      ("Previous", self._previous_data)]:
                self.logger.info(
                    "%s data: %r", pretty_name,
                    {key: str(value) for key, value in data.items()})

        # Update state for next pass through the pipeline
        self._previous_data = input_data

        # Passthrough the input for consumption by any further steps
        return input_data
