# Automated Blog Post Generator

This project is a simple web application that generates detailed blog posts based on user-provided topics. It leverages OpenAI's GPT-3.5-turbo model to generate content dynamically. The application is built using Python and Flask.

## Features

- **Topic-Based Content Generation**: Users can input a topic, and the application generates a blog post on that topic.
- **Dynamic Content Creation**: Utilizes OpenAI's GPT-3.5-turbo model for generating human-like text.
- **Web-Based Interface**: A simple and user-friendly web interface where users can input topics and view generated content.

## Requirements

- Python 3.x
- Flask
- OpenAI Python client library

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/blog-post-generator.git
   cd blog-post-generator

2. **Set Up a Virtual Environment (Optional but Recommended)**
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. **Install Dependencies**
   pip install flask openai

4. **Set Up Your OpenAI API Key**
   Replace 'your_openai_api_key_here' in app.py with your actual OpenAI API key. You can obtain an API key by signing up at OpenAI's website.

## Usage
    Run the Application
    
    bash
    Copy code
    python app.py
    Access the Web Interface
    
    Open your web browser and go to http://127.0.0.1:5000/.
    
    Generate a Blog Post
    
    Enter a topic in the input field and click the "Generate" button.
    The application will generate a blog post based on the provided topic and display it on the page.   

## Files
    app.py: The main Flask application.
    templates/index.html: The HTML template for the web interface.
    static/style.css: The CSS file for styling the web page.

   
