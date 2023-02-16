def nav():
    result ='<nav class="navbar navbar-expand-sm bg-dark navbar-dark">'
    result +='<ul class="nav navbar-nav">'
    result +='<li class="nav-item active"><a class="nav-link" href="/">Home</a></li>'
    result +='<li class="nav-item"><a class="nav-link" href="/artist">Artists</a></li>'
    result +='<li class="nav-item "><a class="nav-link" href="/album">Albums</a></li>'
    result +='<li class="nav-item"><a class="nav-link" href="/track">Tracks</a></li>'
    result +='</ul>'
    result +='</nav>'
    result +='<div style="background-color:blue; padding:1px;"></div>'
    result += '<br>'
    return result