from models.album import Album
from models.artist import Artist

import repositories.album_repository as album_repository
import repositories.artist_repository as artist_repository

album_repository.delete_all()
artist_repository.delete_all()

artist_1 = Artist("Freddy Mercury")
artist_repository.save(artist_1)

album_1 = Album("Album 1", "Rock", artist_1)
album_repository.save(album_1)