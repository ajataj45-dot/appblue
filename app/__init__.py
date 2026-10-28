from flask import Flask, render_template

def create_app():
    app = Flask(__name__, template_folder='templates') 
    
    # Registro de los blueprints existentes
    from app.usuarios.routes import usuarios_bp
    from app.productos.routes import productos_bp
    from app.auth.routes import auth_bp

    from app.admin.routes import admin_bp
    from app.blog.routes import blog_bp



    
    app.register_blueprint(usuarios_bp)
    app.register_blueprint(productos_bp)
    app.register_blueprint(auth_bp)

    app.register_blueprint(admin_bp)
    app.register_blueprint(blog_bp)


    @app.route("/")
    def index():
        return render_template('base.html')
    

    
    return app