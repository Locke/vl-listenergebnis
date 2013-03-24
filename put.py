import urllib2
import urllib

wg = 1

e = [
["Alice", 62.34, 345],
["Bob", 73.45, 234],
["Carol", 51.23, 132],
]


n = len(e);


for i in range(0, n+1):
        html = "<table cellpadding='7'>\n"
        html += "\t<tr style='font-weight: bold;'><td>#</td><td>Name</td><td>Zustimmung</td><td>Gewichtung</td></tr>\n"

        if i < n:
                html += "\t<tr><td>...</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr>\n"

        for j in range(n - i, n):
                html += "\t<tr><td>" + str(j+1) + "</td><td>" + e[j][0] + "</td><td>" + str(e[j][1]) + "%</td><td>" + str(e[j][2]) + "</td></tr>\n"

        html += "</table>\n"

        if i == 0:
                title = "Ergebnis Wahlgang " + str(wg)
        else:
                if i < n:
                        title = "Ergebnis Wahlgang " + str(wg) + " (" + str(i) + "/" + str(n) + ")"
                else:
                        title = "Ergebnis Wahlgang " + str(wg)

        slide_id = "ergebnis" + str(i)
        url = "http://beamercontrol.piraten-bpt.de/agenda/" + slide_id + "/save"

        slide = {
                "slide[hidden]": "true",
                "slide[isdone]": "false",
                "slide[hide]": "false",
                "slide[html]": html,
                "slide[title]": title,
                "slide[type]": "html"
        }

        data_encoded = urllib.urlencode(slide)

        opener = urllib2.build_opener(urllib2.HTTPHandler)
        request = urllib2.Request(url, data=data_encoded)
        request.add_header('Content-Type', 'application/x-www-form-urlencoded')
        request.get_method = lambda: 'PUT'

        print data_encoded

        url2 = opener.open(request)

        print url2.read()
