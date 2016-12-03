import os, os.path
import random
import string

import cherrypy
import redis

cherrypy.config.update({'server.socket_port': 8000})
cherrypy.engine.restart()

r=redis.Redis("localhost") # conneting redis




class helloworld(object):
	@cherrypy.expose
	def index(self):
		head_tag='''<html>
						<head>
							<!--    Customesed css is added for cards(masonry) -->
							<link href="/static/css/style.css" rel="stylesheet">

								<!--bootstrap makes custom css more beautiful -->
									<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
										<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js"></script>
										<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
					</head>'''

		body_start='<body style="background-color:black;">'
		div_col="<div class='masonry'>" #using masonry css class  to display card posts
		div_item="<div class='item text-center'><b><i>"

		#body=str(r.lindex('value',0))

		div_end="</i></b></div>"
		body_end="</div></body></html>"

		blank="  == "
		blank1=" </br> "

		# value fetches scraped data which is stored in Redis instance

		value1='<h3 class="blue text-center"><b><u>'+"Symbol"+blank+str(r.lindex('value',0)).replace('b','')+blank1+'</u></b></h3>'\
		+str(r.lindex('title',1)).replace('b','')+blank+str(r.lindex('value',1)).replace('b','')+blank1\
		+str(r.lindex('title',2)).replace('b','')+blank+str(r.lindex('value',2)).replace('b','')+blank1\
		+str(r.lindex('title',3)).replace('b','')+blank+str(r.lindex('value',3)).replace('b','')+blank1\
		+str(r.lindex('title',4)).replace('b','')+blank+str(r.lindex('value',4)).replace('b','')+blank1\
		+str(r.lindex('title',5)).replace('b','')+blank+str(r.lindex('value',5)).replace('b','')+blank1\
		+str(r.lindex('title',6)).replace('b','')+blank+str(r.lindex('value',6)).replace('b','')+blank1\
		+str(r.lindex('title',7)).replace('b','')+blank+str(r.lindex('value',7)).replace('b','')+blank1\
		+str(r.lindex('title',8)).replace('b','')+blank+str(r.lindex('value',8)).replace('b','')+blank1\
		+str(r.lindex('title',9)).replace('b','')+blank+str(r.lindex('value',9)).replace('b','')+blank1\
		+blank1+blank1\
		+blank1+blank1\


		value2='<h3 class="light-blue text-center"><b><u>'+"Symbol"+blank+str(r.lindex('value',10)).replace('b','')+blank1+'</u></b></h3>'\
		+str(r.lindex('title',1)).replace('b','')+blank+str(r.lindex('value',11)).replace('b','')+blank1\
		+str(r.lindex('title',2)).replace('b','')+blank+str(r.lindex('value',12)).replace('b','')+blank1\
		+str(r.lindex('title',3)).replace('b','')+blank+str(r.lindex('value',13)).replace('b','')+blank1\
		+str(r.lindex('title',4)).replace('b','')+blank+str(r.lindex('value',14)).replace('b','')+blank1\
		+str(r.lindex('title',5)).replace('b','')+blank+str(r.lindex('value',15)).replace('b','')+blank1\
		+str(r.lindex('title',6)).replace('b','')+blank+str(r.lindex('value',16)).replace('b','')+blank1\
		+str(r.lindex('title',7)).replace('b','')+blank+str(r.lindex('value',17)).replace('b','')+blank1\
		+str(r.lindex('title',8)).replace('b','')+blank+str(r.lindex('value',18)).replace('b','')+blank1\
		+str(r.lindex('title',9)).replace('b','')+blank+str(r.lindex('value',19)).replace('b','')+blank1\

		value3='<h3 class="black text-center"><b><u>'+"Symbol"+blank+str(r.lindex('value',20)).replace('b','')+blank1+'</u></b></h3>'\
		+str(r.lindex('title',1)).replace('b','')+blank+str(r.lindex('value',21)).replace('b','')+blank1\
		+str(r.lindex('title',2)).replace('b','')+blank+str(r.lindex('value',22)).replace('b','')+blank1\
		+str(r.lindex('title',3)).replace('b','')+blank+str(r.lindex('value',23)).replace('b','')+blank1\
		+str(r.lindex('title',4)).replace('b','')+blank+str(r.lindex('value',24)).replace('b','')+blank1\
		+str(r.lindex('title',5)).replace('b','')+blank+str(r.lindex('value',25)).replace('b','')+blank1\
		+str(r.lindex('title',6)).replace('b','')+blank+str(r.lindex('value',26)).replace('b','')+blank1\
		+str(r.lindex('title',7)).replace('b','')+blank+str(r.lindex('value',27)).replace('b','')+blank1\
		+str(r.lindex('title',8)).replace('b','')+blank+str(r.lindex('value',28)).replace('b','')+blank1\
		+str(r.lindex('title',9)).replace('b','')+blank+str(r.lindex('value',29)).replace('b','')+blank1\

		value4='<h3 class="grey text-center"><b><u>'+"Symbol"+blank+str(r.lindex('value',30)).replace('b','')+blank1+'</u></b></h3>'\
		+str(r.lindex('title',1)).replace('b','')+blank+str(r.lindex('value',31)).replace('b','')+blank1\
		+str(r.lindex('title',2)).replace('b','')+blank+str(r.lindex('value',32)).replace('b','')+blank1\
		+str(r.lindex('title',3)).replace('b','')+blank+str(r.lindex('value',33)).replace('b','')+blank1\
		+str(r.lindex('title',4)).replace('b','')+blank+str(r.lindex('value',34)).replace('b','')+blank1\
		+str(r.lindex('title',5)).replace('b','')+blank+str(r.lindex('value',35)).replace('b','')+blank1\
		+str(r.lindex('title',6)).replace('b','')+blank+str(r.lindex('value',36)).replace('b','')+blank1\
		+str(r.lindex('title',7)).replace('b','')+blank+str(r.lindex('value',37)).replace('b','')+blank1\
		+str(r.lindex('title',8)).replace('b','')+blank+str(r.lindex('value',38)).replace('b','')+blank1\
		+str(r.lindex('title',9)).replace('b','')+blank+str(r.lindex('value',39)).replace('b','')+blank1\

		value5='<h3 class="light-grey text-center"><b><u>'+"Symbol"+blank+str(r.lindex('value',40)).replace('b','')+blank1+'</u></b></h3>'\
		+str(r.lindex('title',1)).replace('b','')+blank+str(r.lindex('value',41)).replace('b','')+blank1\
		+str(r.lindex('title',2)).replace('b','')+blank+str(r.lindex('value',42)).replace('b','')+blank1\
		+str(r.lindex('title',3)).replace('b','')+blank+str(r.lindex('value',43)).replace('b','')+blank1\
		+str(r.lindex('title',4)).replace('b','')+blank+str(r.lindex('value',44)).replace('b','')+blank1\
		+str(r.lindex('title',5)).replace('b','')+blank+str(r.lindex('value',45)).replace('b','')+blank1\
		+str(r.lindex('title',6)).replace('b','')+blank+str(r.lindex('value',46)).replace('b','')+blank1\
		+str(r.lindex('title',7)).replace('b','')+blank+str(r.lindex('value',47)).replace('b','')+blank1\
		+str(r.lindex('title',8)).replace('b','')+blank+str(r.lindex('value',48)).replace('b','')+blank1\
		+str(r.lindex('title',9)).replace('b','')+blank+str(r.lindex('value',49)).replace('b','')+blank1\

		value6='<h3 class="blue text-center"><b><u>'+"Symbol"+blank+str(r.lindex('value',50)).replace('b','')+blank1+'</u></b></h3>'\
		+str(r.lindex('title',1)).replace('b','')+blank+str(r.lindex('value',51)).replace('b','',1)+blank1\
		+str(r.lindex('title',2)).replace('b','')+blank+str(r.lindex('value',52)).replace('b','')+blank1\
		+str(r.lindex('title',3)).replace('b','')+blank+str(r.lindex('value',53)).replace('b','')+blank1\
		+str(r.lindex('title',4)).replace('b','')+blank+str(r.lindex('value',54)).replace('b','')+blank1\
		+str(r.lindex('title',5)).replace('b','')+blank+str(r.lindex('value',55)).replace('b','')+blank1\
		+str(r.lindex('title',6)).replace('b','')+blank+str(r.lindex('value',56)).replace('b','')+blank1\
		+str(r.lindex('title',7)).replace('b','')+blank+str(r.lindex('value',57)).replace('b','')+blank1\
		+str(r.lindex('title',8)).replace('b','')+blank+str(r.lindex('value',58)).replace('b','')+blank1\
		+str(r.lindex('title',9)).replace('b','')+blank+str(r.lindex('value',59)).replace('b','')+blank1\

		value7='<h3 class="white text-center"><b><u>'+"Symbol"+blank+str(r.lindex('value',60)).replace('b','')+blank1+'</u></b></h3>'\
		+str(r.lindex('title',1)).replace('b','')+blank+str(r.lindex('value',61)).replace('b','')+blank1\
		+str(r.lindex('title',2)).replace('b','')+blank+str(r.lindex('value',62)).replace('b','')+blank1\
		+str(r.lindex('title',3)).replace('b','')+blank+str(r.lindex('value',63)).replace('b','')+blank1\
		+str(r.lindex('title',4)).replace('b','')+blank+str(r.lindex('value',64)).replace('b','')+blank1\
		+str(r.lindex('title',5)).replace('b','')+blank+str(r.lindex('value',65)).replace('b','')+blank1\
		+str(r.lindex('title',6)).replace('b','').replace('b','')+blank+str(r.lindex('value',66)).replace('b','')+blank1\
		+str(r.lindex('title',7)).replace('b','')+blank+str(r.lindex('value',67)).replace('b','')+blank1\
		+str(r.lindex('title',8)).replace('b','')+blank+str(r.lindex('value',68)).replace('b','')+blank1\
		+str(r.lindex('title',9)).replace('b','')+blank+str(r.lindex('value',69)).replace('b','')+blank1\
		+blank1+blank1\
		+blank1+blank1\

		value8='<h3 class="blue text-center"><b><u>'+"Symbol"+blank+str(r.lindex('value',70)).replace('b','')+blank1+'</u></b></h3>'\
		+str(r.lindex('title',1)).replace('b','')+blank+str(r.lindex('value',71)).replace('b','')+blank1\
		+str(r.lindex('title',2)).replace('b','')+blank+str(r.lindex('value',72)).replace('b','')+blank1\
		+str(r.lindex('title',3)).replace('b','')+blank+str(r.lindex('value',73)).replace('b','')+blank1\
		+str(r.lindex('title',4)).replace('b','')+blank+str(r.lindex('value',74)).replace('b','')+blank1\
		+str(r.lindex('title',5)).replace('b','')+blank+str(r.lindex('value',75)).replace('b','')+blank1\
		+str(r.lindex('title',6)).replace('b','')+blank+str(r.lindex('value',76)).replace('b','')+blank1\
		+str(r.lindex('title',7)).replace('b','')+blank+str(r.lindex('value',77)).replace('b','')+blank1\
		+str(r.lindex('title',8)).replace('b','')+blank+str(r.lindex('value',78)).replace('b','')+blank1\
		+str(r.lindex('title',9)).replace('b','')+blank+str(r.lindex('value',79)).replace('b','')+blank1\

		value9='<h3 class="white text-center"><b><u>'+"Symbol"+blank+str(r.lindex('value',80)).replace('b','')+blank1+'</u></b></h3>'\
		+str(r.lindex('title',1)).replace('b','')+blank+str(r.lindex('value',81)).replace('b','')+blank1\
		+str(r.lindex('title',2)).replace('b','')+blank+str(r.lindex('value',82)).replace('b','')+blank1\
		+str(r.lindex('title',3)).replace('b','')+blank+str(r.lindex('value',83)).replace('b','')+blank1\
		+str(r.lindex('title',4)).replace('b','')+blank+str(r.lindex('value',84)).replace('b','')+blank1\
		+str(r.lindex('title',5)).replace('b','')+blank+str(r.lindex('value',85)).replace('b','')+blank1\
		+str(r.lindex('title',6)).replace('b','')+blank+str(r.lindex('value',86)).replace('b','')+blank1\
		+str(r.lindex('title',7)).replace('b','')+blank+str(r.lindex('value',87)).replace('b','')+blank1\
		+str(r.lindex('title',8)).replace('b','')+blank+str(r.lindex('value',88)).replace('b','')+blank1\
		+str(r.lindex('title',9)).replace('b','')+blank+str(r.lindex('value',89)).replace('b','')+blank1\

		value10='<h3 class="light-blue text-center"><b><u>'+"Symbol"+blank+str(r.lindex('value',90)).replace('b','')+blank1+'</u></b></h3>'\
		+str(r.lindex('title',1)).replace('b','')+blank+str(r.lindex('value',91)).replace('b','')+blank1\
		+str(r.lindex('title',2)).replace('b','')+blank+str(r.lindex('value',92)).replace('b','')+blank1\
		+str(r.lindex('title',3)).replace('b','')+blank+str(r.lindex('value',93)).replace('b','')+blank1\
		+str(r.lindex('title',4)).replace('b','')+blank+str(r.lindex('value',94)).replace('b','')+blank1\
		+str(r.lindex('title',5)).replace('b','')+blank+str(r.lindex('value',95)).replace('b','')+blank1\
		+str(r.lindex('title',6)).replace('b','')+blank+str(r.lindex('value',96)).replace('b','')+blank1\
		+str(r.lindex('title',7)).replace('b','')+blank+str(r.lindex('value',97)).replace('b','')+blank1\
		+str(r.lindex('title',8)).replace('b','')+blank+str(r.lindex('value',98)).replace('b','')+blank1\
		+str(r.lindex('title',9)).replace('b','')+blank+str(r.lindex('value',99)).replace('b','')+blank1\


		#return ''.join(str(r.lindex('title',0)))
		#Html page to display
		html_full=head_tag+body_start+div_col\
		+div_item+value1+div_end\
		+div_item+value2+div_end\
		+div_item+value3+div_end\
		+div_item+value4+div_end\
		+div_item+value5+div_end\
		+div_item+value6+div_end\
		+div_item+value7+div_end\
		+div_item+value8+div_end\
		+div_item+value9+div_end\
		+div_item+value10+div_end\
		+body_end


		return html_full
		#count=-1
		#a=("%s--%s "%(r.lindex('title',0),r.lindex('value',0)
		#return a


if __name__ == '__main__':
	conf = {
        '/': {
            'tools.sessions.on': True,
            'tools.staticdir.root': os.path.abspath(os.getcwd())
        },
        '/static': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': './public'
        }
    }
	cherrypy.quickstart(helloworld(), '/', conf)
