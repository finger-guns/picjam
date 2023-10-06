# Setup

```sh
docker compose build
```

# Running
```
docker compose up
```

## Short comings
this was an hours worth of work, ideally there are a handufl of things i'd have liked to implement.
- check that the image hasn't already been converted.
- Check the image type and implement some saftey around that.
- typing on the django inputs, even though its a little bit messier than it needs to be, validation should be on that side.
- Some of the styling is a little bit messy, i did just throw tailwind in there to make it somewhat nicer, but there could be some more padding and what not around certian elements.
The flex stuff could be cleaner too, its right to left insead of left to right.
All you'd need to do is wrap the images in their own block level container and deal with it like that.
Oh and i'd round the convert to greyscale button to an actual button - round it.

