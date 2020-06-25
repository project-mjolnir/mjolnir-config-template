"""Example output plugin demonstrating a custom file format."""

# Local imports
import brokkr.pipeline.baseoutput


class ExampleFileOutput(brokkr.pipeline.baseoutput.FileOutputStep):
    def __init__(self, extension="txt", **file_kwargs):
        super().__init__(extension=extension, **file_kwargs)
        # YOUR INIT CODE HERE

    def write_file(self, input_data, output_file_path):
        # YOUR FILE WRITING CODE HERE
        with open(output_file_path, mode="a",
                  encoding="utf-8", newline="\n") as output_file:
            try:
                output_data = {
                    key: value.value for key, value in input_data.items()}
            except AttributeError:  # If input data is a dict already
                output_data = input_data
            output_file.write(repr(output_data) + "\n")
