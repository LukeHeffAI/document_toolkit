# Welcome to my Document Toolkit

## Prerequisites

Before you begin, make sure you have the following installed:

- Python (version 3.7 or later): [Download Python](https://www.python.org/downloads/)
- pip (Python package installer): Usually comes with Python.

## Setup Instructions

1. **Clone the Repository**: First, clone this repository to your local machine using Git. If you're unfamiliar with Git, check out this [guide](https://git-scm.com/book/en/v2/Getting-Started-Git-Basics).

    ```bash
    git clone https://github.com/LukeHeffAI/document_toolkit.git
    cd document_toolkit
    ```

2. **Install Dependencies**: Install the necessary Python packages using pip:

    ```bash
    pip install -r requirements.txt
    ```

3. **Set Up .env File**: Create a `.env` file in the root directory of this project. Inside, you need to provide your OpenAI API key:

    ```Properties
    OPENAI_API_KEY=your_api_key_here
    ```

    This is crucial for the text processing functionalities. Replace `your_api_key_here` with your actual OpenAI API key. If you don't have one, go to/setup your OpenAI account and get one [here](https://platform.openai.com/api-keys).

## How to Use

1. **Choose a Tool**: Open `main.py` and choose a tool by setting the `tool` variable. Options include:
    - `summarise`
    - `key_points`
    - `latex`
    - `query`
    - `edit_json`

2. **Choose Input Type**: Set the `input_type` to either `text` for direct text input or `pdf` for PDF file input. _Input limit is set to 128k tokens (approx. 100,000 words)._

3. **Provide Input**:
    - If you chose `text`, you will be prompted to enter the text when you run the script.
    - If you chose `pdf`, replace `insert\pdf\path\to\test.pdf` with the path to your PDF file.

4. **Run the Program**: Execute the script with:

    ```bash
    python main.py
    ```

5. **Check Output**: The result will be displayed in the console. If you processed a PDF, the output would also be saved in the `output` folder as a `.txt` file.

## Additional Information

- **.gitignore**: Files in the `output` folder and any `.env` files are ignored by Git to protect your outputs and secrets.
- **Contribute**: Feel free to contribute to the repository by submitting pull requests or reporting issues.

## Troubleshooting & Support

If you encounter any problems or need help, please open an issue in this repository or reach out to me directly.
