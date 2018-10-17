import webbrowser


def web_page_open(path, freq):

    chart = path+".svg"

    web_page = """
    <!DOCTYPE html>
    <html>
    <head>
    <script>
    <!--
    function timedRefresh(timeoutPeriod) {setTimeout("location.reload(true);",timeoutPeriod);}
    window.onload = timedRefresh("""+str(freq*1000)+""");
    //   -->
    </script>
    </head>
    <body>
    <img src=\""""+chart+"""\" alt="chart" style="width:750px">
    </body>
    </html>"""

    web_file = open(path+'.html', 'w')
    web_file.writelines(web_page)
    web_file.close()

    webbrowser.open(path+'.html')
