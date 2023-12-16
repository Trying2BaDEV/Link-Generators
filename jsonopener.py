import json
import webbrowser
import gratient

def open_urls_from_json(json_file):
    try:
        with open(json_file, 'r') as file:
            urls = json.load(file)
            if not urls:
                print(gratient.red(f"No URLs found in the JSON file '{json_file}'."))
                return

            print(gratient.purple(f"Opening {len(urls)} URLs..."))
            for url in urls:
                webbrowser.open(url)

        # Reset the content of the JSON file
        with open(json_file, 'w') as file:
            json.dump([], file, indent=2)

        print(gratient.red(f"Contents of '{json_file}' have been reset."))
    except FileNotFoundError:
        print(gratient.red(f"File '{json_file}' not found."))
    except json.JSONDecodeError:
        print(gratient.red(f"Error decoding JSON from file '{json_file}'. Please ensure the file is valid JSON"))

if __name__ == "__main__":
    json_file_path = input(gratient.purple("Enter the path to the JSON file: "))
    input(gratient.purple("Confirm?? This will reset the JSON file!! (y/n)")).lower() == "y"
    open_urls_from_json(json_file_path)
