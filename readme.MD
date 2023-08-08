## About

Devfeel is a unique blog app with a fresh perspective on the tech world. Unlike traditional developer blogs that solely focus on technical details, Devfeel's primary emphasis is on the human side of technology. Here, we share personal stories, experiences, and reflections of developers coping with changes and developments in the tech industry.

## Installation

1. Clone the repository:

```bash
 git clone git@github.com:Swai15/Blog.git
  OR
 git clone https://github.com/Swai15/Blog.git
```

2. Create and activate a virtual environment:

```bash
python -m venv venv
source venv/Scripts/activate
```

3. Install the dependencies:

```bash
pip install -r requirements.txt
```

4. Run the development server:

```bash
python manage.py runserver
```

## Features and bugs tracking

For tracking the development progress, features, and bugs, I use Trello. You can find the Trello board for this project [here](https://trello.com/b/yyQSPjNm)

## Additional info for local setup.

This project's postgres database has been hosted on [Supabase](https://supabase.com/). Comment out it's setup in setting and uncomment the default sqlite3 configuration to revert back to a local database.

The images are stored [cloudinary](https://cloudinary.com/) comment out it's setup in settings to revert back to accepting media files in localhost.
