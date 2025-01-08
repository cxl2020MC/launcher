import webview


def custom_logic(window):
    # window.evaluate_js('alert("Nice one brother")')
    pass


window = webview.create_window('Woah dude!', html='')
webview.start(custom_logic, (window,),  gui="gtk")

