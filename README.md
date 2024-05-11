# Invoice Details App

## Introduction

This project is an AI-powered app that leverages Google Gemini Vision Pro to read invoices and extract details such as the invoice date, total due amount, owner address, and more. Users can ask questions in natural language about invoice details, and the app processes their queries using AI to provide accurate information.

## Features

- **Invoice Reading:** The app uses Google Gemini Vision Pro to read invoices and extract key details.
  
- **Natural Language Processing:** Users can ask questions about invoice details using normal English language, and the app processes their queries using AI.

- **Detailed Information:** The app provides comprehensive details from invoices, including invoice date, total due amount, owner address, and more.

- **User-Friendly Interface:** The interface is designed to be intuitive and easy to use, making it accessible for a wide range of users.

## Getting Started

### Prerequisites

Before running the app, ensure you have the following installed:

- Python (version 3.10)
- Google Cloud Platform account with access to Gemini Vision Pro API

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/invoice-details-app.git
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Set up your Google Cloud Platform account and obtain access to the Gemini Vision Pro API.

4. Set your Google Cloud Platform credentials:

   - Download the JSON file containing your service account key.
   - Set the path to this JSON file in your environment variables or directly in the code.

### Usage

1. Run the app:

   ```bash
   python app.py
   ```

2. Open your web browser and navigate to `http://localhost:5000` to access the app.

3. Enter your invoice-related queries in English and press enter to get detailed information.

## Frontend (Streamlit)

The frontend of this app is built using Streamlit, providing a user-friendly interface for interacting with invoice details.

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/yourfeature`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature/yourfeature`).
6. Create a new Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- Google for providing the Gemini Vision Pro API.
- Contributors to libraries and frameworks used in this project.
