# Scratch
A record review site (Letterbox but for albums)

## Development

Built in Django

### Required pip packages

- `django-extensions`
- `spotipy`
- `django`

### Commands 

start developemnt environment

```bash
python manage.py runserver 0.0.0.0:8000

# '0.0.0.0:8000' is required for other systems on the same local network to access the project
```

## Project Features 

### Data

How will we obtain data to populate our database? From Spotify! 

Users can log into their Spotify accounts which will then provide us with access to album data, which we'll use to build up the Scratch Database. 

### Reviews

Reviews will be able to have sound snippets. 

![Screenshot 2023-04-11 at 9 40 49 AM](https://user-images.githubusercontent.com/22066972/231198766-a7670173-af1c-412c-a5a0-489f33d6dccd.png)
