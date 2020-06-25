"""
Example output preset demonstrating a custom file format.
"""

# Local imports
import brokkr.pipeline.baseoutput


class ExampleFileOutput(brokkr.pipeline.baseoutput.FileOutputStep):
    """Example output plugin that writes the data's repr to a text file."""
    def __init__(self, extension="txt", **file_kwargs):
        """
        Example output plugin that writes the output data repr to a text file.

        Parameters
        ----------
        extension : str, optional
            Extension to use for the output file. The default is "txt".
        **file_kwargs : kwargs
            Additional keyword arguments to pass to FileOutputStep.

        Returns
        -------
        None.

        """
        super().__init__(extension=extension, **file_kwargs)
        # YOUR INIT CODE HERE

    def write_file(self, input_data, output_file_path):
        """
        Appends the given data to file at the given path, as its string repr.

        Parameters
        ----------
        input_data : dict of str: DataValue
            The input data to .
        output_file_path : str or pathlib.Path
            The file path to append to, as either a string or a Path.

        Returns
        -------
        None.

        """
        # YOUR FILE WRITING CODE HERE
        with open(output_file_path, mode="a",
                  encoding="utf-8", newline="") as output_file:
            self.logger.debug("Writing output as repr text")
            try:
                output_data = {
                    key: value.value for key, value in input_data.items()}
            except AttributeError:  # If input data is a dict already
                output_data = input_data
            output_file.write(repr(output_data) + "\n")
