import webbrowser


def web_page_open(path, freq, counter):

    chart = path+".svg"
    refresh_time = str(freq * (1 + 1 / counter) * 1000)
    counter = str(counter + 10)

    web_page = """
    <!DOCTYPE html>
    <html>
    <head>
        <script>
            var i = localStorage.getItem(" """ + path + """ ");
            if (i == null) {
                i = """ + counter + """;
            }
            setInterval(function () {
                localStorage.setItem(" """ + path + """ ", --i);
                if (i >= 0) {
                    window.location.reload();
                }
            }, """ + refresh_time + """);
        </script>
    </head>
    <body>
        <img src=\""""+chart+"""\" alt="chart" style="width:750px" align="top">
    </body>
    </html>"""

    web_file = open(path+'.html', 'w')
    web_file.writelines(web_page)
    web_file.close()

    webbrowser.open(path+'.html')
