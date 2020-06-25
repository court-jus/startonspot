# Start on spot

Despite the name, this script is here to help you have a playlist run until a specific time. For example, during the lockdown, every morning I broadcast some music to my colleagues before our morning meeting, I want the music to stop exactly at 9:01am.

When ran, the script lists the tracks in your playlist, starting by the last one and computes the cumulated play time until it reaches the current time. It can now tell you at which time each track should start and at what position the currently playing track should be.

## How to use it?

You will need a developer account on the spotify platform (https://developer.spotify.com/), create an application and gather the client id and client secret and put those values in environment variables while running the script:

```
SPOTIFY_ID=foobar SPOTIFY_SECRET=1234567489 python start.py
```

By default it will look for my morning playlist but you can change that by using the `SPOTIFY_USERNAME` and `SPOTIFY_PLAYLIST` variables:

```
SPOTIFY_USERNAME=someone SPOTIFY_PLAYLIST=https://open.spotify.com/playlist/123456789foobar SPOTIFY_ID=foobar SPOTIFY_SECRET=1234567489 python start.py
```
