# from models.album import Album
from models.artist import Artist

# import repositories.album_repository as album_repository
import repositories.artist_repository as artist_repository

artist_1 = Artist("Freddy Mercury")
artist_repository.save(artist_1)