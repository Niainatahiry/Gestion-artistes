import web

web.config.debug = True

urls = (
    '/', 'index',
    '/artist', 'artist' ##url vers la class artistes, à indiquer comme suivant href="/artist"
)

class index:
    def GET(self):
        db = web.database(
            dbn='mysql',
            host='tmp-insi.rktmb.org',
            port=3306,
            user='insigroup00',
            pw='insigroup00',
            db='project00',
        )
        albums=db.select('Album',limit=10)
        artists=db.select('Artist', limit=10)
        genres=db.select('Genre',limit=10)
        tracks=db.select('Track',limit=10)
        result='<html><head><title>test</title>'
        result += '<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.css"> '
        result += '</head><body> '

        ##voici les liens
        result +='<nav class="navbar navbar-expand-sm bg-dark navbar-dark">'
        result +='<ul class="nav navbar-nav">'
        result +='<li class="nav-item active"><a class="nav-link" href="/">Home</a></li>'
        result +='<li class="nav-item"><a class="nav-link" href="/artist">Artists</a></li>'
        result +='<li class="nav-item"><a class="nav-link" href="/album">Albums</a></li>'
        result +='<li class="nav-item"><a class="nav-link" href="/track">Tracks</a></li>'
        result +='</ul>'
        result +='</nav>'
        result += '<br>'
        ##
        
        result += '<h1 class="texte-center"><dl>Tableau des "artistes"</dl></h1>'
        result += '<p>Voici le tableau classant les "artistes", leurs Id ,leur genre de music, et un album de chaque artistes</p>'
        result += '<table border="1" class="table">'
        result += '<tr class="table-success"><th>Id_artists</th><th>Artiste</th><th>Genre</th><th>Album</th></tr> '
        for album in albums:
            result += '<tr>'
            for artist in artists:
                result +='<td>'+str(artist.ArtistId)+'</td>'
                result +='<td>'+artist.Name+'</td>'
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
        result += '</body></html> '
        return result

###ajout classe artiste url /artist  
class artist:
    def GET(self):
        db = web.database(
            dbn='mysql',
            host='tmp-insi.rktmb.org',
            port=3306,
            user='insigroup00',
            pw='insigroup00',
            db='project00',
        )


        artists=db.select('Artist', limit=10)
        result='<html><head><title>test</title>'
        result += '<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.css"> '
        result += '</head><body>'

        ##voici les liens
        result +='<nav class="navbar navbar-expand-sm bg-dark navbar-dark">'
        result +='<ul class="nav navbar-nav">'
        result +='<li class="nav-item active"><a class="nav-link" href="/">Home</a></li>'
        result +='<li class="nav-item"><a class="nav-link" href="/artist">Artists</a></li>'
        result +='<li class="nav-item"><a class="nav-link" href="/album">Albums</a></li>'
        result +='<li class="nav-item"><a class="nav-link" href="/track">Tracks</a></li>'
        result +='</ul>'
        result +='</nav>'
        result += '<br>'
        ##
        
        result += '<br>'
        result += '<h1><dl>listes des artistes</dl></h1>'
        result += '<table border="1" class="table">'
        result += '<tr>'
        result += '<tr class="table-success"><th>Id_artists</th><th>Artiste</th></tr>'
        for artist in artists:
            result += '<tr></tr>'
            result +='<td>'+str(artist.ArtistId)+'</td>'
            result +='<td>'+artist.Name+'</td>'
            result += '</tr>'
        result += '</table>'
        result += '</body></html>'
        return result
if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
