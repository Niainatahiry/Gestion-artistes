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
        a2=db.select('Album', limit=2)
        result = '<html><head><title>test</title></head>'
        result += '<body>'
        for a in a2:
            result += a.Title + ', <br/>'
        result += '</body>'
        result += '</html>'
        return result

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
