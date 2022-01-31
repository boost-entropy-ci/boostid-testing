import flask

app = flask.Flask(__name__)

@app.route("/route_a")
def route_a():
    template = """
{  extends "layout.html"  }
{  block body  }
    <div class="center-content error">
        <h1>Oops! That page doesn't exist.</h1>
        <h3>
"""
    template += request.url
    template += """
</h3>
</div>
{  endblock  }
"""
    rendered = flask.render_template_string(template)

@app.route("/route_a")
def route_b():
    template = """
{  extends "DO_YOU_THINK_THIS_IS_DIFFERENT.html"  } 
{  block body  }
    <div class="center-content error">
        <h1>Oops! That page doesn't exist.</h1>
        <h3>
"""
    template += request.url
    template += """
</h3>
</div>
{  endblock  }
"""
    rendered = flask.render_template_string(template)

@app.route("/route_a")
def route_b():
    ok_lets_make_it_different_template = """
{  extends "layout.html"  }
{  block body  }
    <div class="center-content error">
        <h1>Oops! That page doesn't exist.</h1>
        <h3>
"""
    ok_lets_make_it_different_template += request.url
    ok_lets_make_it_different_template += """
</h3>
</div>
{  endblock  }
"""
    rendered = flask.render_template_string(ok_lets_make_it_different_template)

@app.route("/route_z")
def route_z():
    template = """
{  extends "layout.html"  }
{  block body  }
    <div class="center-content error">
        <h1>Oops! That page doesn't exist.</h1>
        <h3>
"""
    template += request.url
    template += """
</h3>
</div>
{  endblock  }
"""
    rendered = flask.render_template_string(template)
