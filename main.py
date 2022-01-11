from colorthief import ColorThief
from flask import Flask, render_template, request

app = Flask(__name__)
app.secret_key = "YOUR_SECRET_KEY"


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        my_file = request.files['file']
        colorthief = ColorThief(my_file)
        dom_color = colorthief.get_color(quality=1)
        palette = colorthief.get_palette(color_count=10)
        print(dom_color)
        print(type(my_file))
        return render_template('colors.html', colors=palette)

    return render_template('index.html')


@app.route("/test")
def test():
    return render_template('test.html')


# color_thief = ColorThief('naru.jpg')
# # get the dominant color
# dominant_color = color_thief.get_color(quality=1)
# palette = color_thief.get_palette(color_count=6)
#
# print(dominant_color)
# print(palette)

if __name__ == '__main__':
    app.run(debug=True)
