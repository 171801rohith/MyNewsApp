# MyNewsApp

MyNewsApp is a simple web application that allows users to search for the latest news articles on any topic using a user-friendly interface. Built with Flask, it fetches news from the NewsAPI and displays results in a clean, responsive layout.

## Features

- **Search News**: Enter any topic or keyword to instantly fetch and display the most recent news articles.
- **Interactive UI**: Responsive and modern interface styled with custom CSS.
- **Live Results**: News results include article titles, descriptions, and images, each linked to the original source.

## How It Works

1. Enter a search query on the main page.
2. The app sends a request to the NewsAPI using your query.
3. News articles matching your query are fetched and displayed with their title, description, and image.

## Tech Stack

- **Backend:** Python, Flask
- **Frontend:** HTML (Jinja2 templates), CSS
- **APIs:** NewsAPI
- **Other:** Docker support, Python-dotenv for environment management

## Setup & Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/171801rohith/MyNewsApp.git
   cd MyNewsApp
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Environment variables:**
   - Create a `.env` file in the root directory.
   - Add your NewsAPI key and a Flask secret key:
     ```
     NEWS_API=your_newsapi_key_here
     SECRET_KEY=your_secret_key_here
     ```

4. **Run the app:**
   ```bash
   python app.py
   ```

   Or use Docker:
   ```bash
   docker build -t mynewsapp .
   docker run -p 5000:5000 mynewsapp
   ```

5. **Access the app:**
   - Open your browser and go to [http://localhost:5000](http://localhost:5000)

## File Structure

```
├── app.py               # Flask app
├── requirements.txt     # Python dependencies
├── Dockerfile           # For Docker deployment
├── templates/
│   ├── layout.html      # Main layout and search form
│   └── result.html      # Results display
├── static/
│   └── css/style.css    # Custom styles
```

## License

This project is licensed under the MIT License.

---

*Happy news reading!*
