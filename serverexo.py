import web

web.config.debug = False

urls = (
    '/', 'index'
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
        a2=db.select('Album',limit=10)
        artists=db.select('Artist', limit=10)
        genres=db.select('Genre',limit=10)
        result='<html><head><title>test</title></head><body> '
        result += '<table border="1">'
        result += '<tr><th>Id_artists</th><th>Artiste</th><th>Genre</th><th>Album</th></tr> '
        for a in a2:
            result += '<tr>'
            for artist in artists:
                result +='<td>'+str(artist.ArtistId)+'</td>'
                result +='<td>'+artist.Name+'</td>'
                break
            for genre in genres:
                result +='<td>'+genre.Name+'</td>'
                break
            result +='<td>'+a.Title+'</td>'           
            result += '</tr>'
        result += '</table>'
        result += '</body></html> '
        return result

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
