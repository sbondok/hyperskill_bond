def remove_carriage_returns(input_file, output_file):
    with open(input_file, 'r') as file:
        text = file.read()

    text = text.replace('\n', ' ')

    with open(output_file, 'w') as file:
        file.write(text)


# Example usage
input_file = 'first.txt'  # Replace with the path to your input file
output_file = 'output.txt'  # Replace with the desired output file path

remove_carriage_returns(input_file, output_file)