from flask import Blueprint, render_template

blog_bp = Blueprint('blog', __name__, url_prefix="/blog", template_folder="templates")

# /blog/entrada/<id>
@blog_bp.route("/entrada/<int:id>")
def entrada(id):
    titulo_entrada = f"Entrada del Blog numero {id}"
    return render_template('entrada.html', titulo=titulo_entrada, id=id)