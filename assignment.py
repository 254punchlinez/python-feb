def modify_and_write_file():
    input_filename = input("Enter the input filename: ")
    output_filename = input("Enter the output filename: ")

    try:
        # Read from input file
        with open(input_filename, 'r') as input_file:
            content = input_file.read()
            
            # Simply convert to uppercase
            modified_content = content.upper()
            
            # Write to output file
            with open(output_filename, 'w') as output_file:
                output_file.write(modified_content)
            
            print(f"\nSuccess! Uppercase content written to {output_filename}")
            
    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

#run code
if __name__ == "__main__":
    modify_and_write_file()