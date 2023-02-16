import web
import footer
from DB import Db

web.config.debug = True

urls = (
    '/', 'index',
    '/artist', 'artist', ##url vers la class artistes, à indiquer comme suivant href="/artist"
    '/album','album',
    '/track','track'
)


###ajout classe track url/track 
class track:
    def GET(self):
        d=Db()
        db=d.getDb()
        tracks=db.select('Track', limit=10)
        result='<html><head><title>test</title>'
        result += '<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.css"> '
        result += '</head><body>'

        ##tous les liens
        result +='<nav class="navbar navbar-expand-sm bg-dark navbar-dark">'
        result +='<ul class="nav navbar-nav">'
        result +='<li class="nav-item "><a class="nav-link" href="/">Home</a></li>'
        result +='<li class="nav-item"><a class="nav-link" href="/artist">Artists</a></li>'
        result +='<li class="nav-item"><a class="nav-link" href="/album">Albums</a></li>'
        result +='<li class="nav-item active active"><a class="nav-link" href="/track">Tracks</a></li>'
        result +='</ul>'
        result +='</nav>'
        result += '<br>'
        ##
        
        result += '<br>'
        result += '<h1 class="row justify-content-center align-items-center"><dl>Listes des traks</dl></h1>'
        result += '<table border="1" class="table">'
        result += '<tr>'
        result += '<tr class="table-success"><th>id-track</th><th>tracks</th>'
        for track in tracks:
            result += '<tr></tr>'
            result += '<td>'+str(track.TrackId)+'</td>'
            result +='<td>'+track.Name+'</td>'
            result += '</tr>'
        result += '</table>'
        result += footer.footer()
        result += '</body></html>'
        return result
if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()