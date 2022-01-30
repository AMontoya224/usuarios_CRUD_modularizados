from flask import render_template, request, redirect, session, url_for
from usuarios_app import app
from usuarios_app.modelos.modelo_usuarios import Usuario
from datetime import datetime

@app.route( '/users', methods=["GET"] )
def inicioUsuario():
    users = Usuario.obtenerListaUsuarios()
    return render_template( "leer.html", users=users )

@app.route( '/users/new', methods=["GET"] )
def crearUsuario():
    return render_template("crear.html")

@app.route( '/users/<idUsuario>', methods=["GET"] )
def mostrarUsuario( idUsuario ):
    usuarioAEditar = {
        "id" : idUsuario
    }
    users = Usuario.obtenerDatosUsuario( usuarioAEditar )
    return render_template( "mostrar.html", users=users[0])

@app.route( '/users/<idUsuario>/edit', methods=["GET"] )
def editarUsuario( idUsuario ):
    usuarioAEditar = {
        "id" : idUsuario
    }
    users = Usuario.obtenerDatosUsuario( usuarioAEditar )
    return render_template( "editar.html", users=users[0] )

@app.route( '/home', methods=["POST"] )
def irHome():
    return redirect( '/users' )

@app.route( '/new', methods=["POST"] )
def new_P():
    return redirect( '/users/new' )

@app.route( '/users/new', methods=["POST"] )
def crearUsuario_P():
    nuevoUsuario = {
        "first_name" : request.form["first_name"],
        "last_name" : request.form["last_name"],
        "email" : request.form["email"],
        "fecha" : datetime.today()
    }
    session["first_name"] = request.form["first_name"]
    session["last_name"] = request.form["last_name"]
    session["email"] = request.form["email"]
    session["fecha"] = datetime.today()
    idUsuario = Usuario.agregaUsuario( nuevoUsuario )
    return redirect(url_for( 'mostrarUsuario', idUsuario=idUsuario ))

@app.route( '/users/<idUsuario>', methods=["POST"] )
def mostrarUsuario_P(idUsuario):
    return redirect(url_for( 'mostrarUsuario', idUsuario=idUsuario ))

@app.route( '/edit/<idUsuario>', methods=["POST"] )
def edit_P(idUsuario):
    return redirect(url_for( 'editarUsuario', idUsuario=idUsuario ))

@app.route( '/users/<idUsuario>/edit', methods=["POST"] )
def editarUsuario_P( idUsuario ):
    usuarioAEditar = {
        "id" : idUsuario,
        "first_name" : request.form["first_name"],
        "last_name" : request.form["last_name"],
        "email" : request.form["email"],
        "fecha" : datetime.today()
    }
    Usuario.editarUsuario( usuarioAEditar )
    session["first_name"] = request.form["first_name"]
    session["last_name"] = request.form["last_name"]
    session["email"] = request.form["email"]
    session["fecha"] = datetime.today()
    return redirect(url_for( 'mostrarUsuario', idUsuario=idUsuario ))

@app.route( '/users/<idUsuario>/destroy', methods=["POST"] )
def eliminarUsuario( idUsuario ):
    usuarioAEliminar = {
        "id": idUsuario
    }
    Usuario.eliminarUsuario( usuarioAEliminar )
    return redirect( '/users' )