import web
import nav
import footer

from DB import Db
from list_artist import artist
from list_album import album
from list_track import track
web.config.debug = True

urls = (
    '/', 'index',
    '/artist', 'artist', ##url vers la class artistes, à indiquer comme suivant href="/artist"
    '/album','album',
    '/track','track'
)

class index:
    def GET(self):
        d=Db()
        db=d.getDb()
        albums=db.select('Album',limit=10)
        artists=db.select('Artist', limit=10)
        playlists=db.select('Playlist',limit=10)
        genres=db.select('Genre',limit=10)
        tracks=db.select('Track',limit=10)
        result='<html><head><title>test</title>'
        result += '<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.css"> '
        result += '</head><body> '

        ##voici les liens
        result += nav.nav()
        result += '<h1 class="row justify-content-center align-items-center"><dl>Tableau des "artistes"</dl></h1>'
        result += '<p class="row justify-content-center align-items-center">Voici le tableau classant les "artistes", leurs Id ,leur genre de music, et un album de chaque artistes</p>'
        result += '<table border="1" class="table">'
        result += '<tr class="table-success"><th>Id_artists</th><th>Artiste</th><th>Album</th><th>Genre</th><th>Playlist</th></tr> '
        for album in albums:
            result += '<tr>'
            for artist in artists:
                result +='<td>'+str(artist.ArtistId)+'</td>'
                result +='<td>'+artist.Name+'</td>'
                break
            for playlist in playlists:
                result +='<td>'+playlist.Name+'</td>'
                break
            for genre in genres:
                result +='<td>'+genre.Name+'</td>'
                break
            result +='<td>'+album.Title+'</td>'           
            result += '</tr>'
        result += '</table>'
        result += '<br>'
        result += '<hr>'
        result += '<br>'
        result += '<h1><dl>classement des "tracks"</dl></h1>'
        result += '<p>Voici le tableau classant les "tracks", leurs compositeurs et le prix unitaire</p>'
        result += '<table border="1" class="table">'
        result += '<tr class="table-success"><th>id-track</th><th>tracks</th><th>Compositeurs</th><th>prix unitaire</th></tr>'
        for track in tracks:
            result += '<tr>'
            result += '<td>'+str(track.TrackId)+'</td>'
            result += '<td>'+track.Name+'</td>'
            result +='<td>'+str(track.Composer)+'</td>'
            result +='<td>'+str(track.UnitPrice)+'</td>'
        result += '</table>'
        result += footer.footer()
        result += '</body></html> '
        return result
if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
