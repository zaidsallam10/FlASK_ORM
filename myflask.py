from flask import Flask

app=Flask(__name__)

@app.route('/')
def wlc():
    return "<h1>Hello to my fucking world</h1>"

# getVendorRequests
if __name__ == "__main__":
    app.run()
