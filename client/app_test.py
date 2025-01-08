import webview


def custom_logic(window):
    # window.evaluate_js('alert("Nice one brother")')
    pass


window = webview.create_window('Woah dude!', "web/index.html", width=800, height=600)
webview.start(custom_logic, (window,),  gui="gtk")
