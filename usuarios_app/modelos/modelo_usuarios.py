from usuarios_app.config.mysqlconnection import connectToMySQL

class Usuario:
    def __init__( self, id, first_name, last_name, email, fecha ):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.fecha = fecha
    
    @classmethod
    def agregaUsuario( cls, nuevoUsuario ):
        query = "INSERT INTO users(first_name, last_name, email, created_at, update_at) VALUES(%(first_name)s, %(last_name)s, %(email)s, %(fecha)s, %(fecha)s);"
        resultado = connectToMySQL( "users_CRUD" ).query_db( query, nuevoUsuario )
        query2 = "ALTER TABLE users AUTO_INCREMENT = 1;"
        resultado2 = connectToMySQL( "users_CRUD" ).query_db( query2 )
        return resultado
    
    @classmethod
    def obtenerListaUsuarios( self ):
        query = "SELECT * FROM users;"
        resultado = connectToMySQL( "users_CRUD" ).query_db( query )
        users = []
        for usuario in resultado:
            users.append( Usuario( usuario["id"], usuario["first_name"], usuario["last_name"], usuario["email"], usuario["created_at"]))
        return users
    
    @classmethod
    def eliminarUsuario( self, usuario ):
        query = "DELETE FROM users WHERE id = %(id)s;"
        resultado = connectToMySQL( "users_CRUD" ).query_db( query, usuario )
        return resultado

    @classmethod
    def obtenerDatosUsuario( self, usuario ):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        resultado = connectToMySQL( "users_CRUD" ).query_db( query, usuario )
        return resultado
    
    @classmethod
    def editarUsuario( self, usuarioAEditar ):
        query = "UPDATE users SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s, update_at = %(fecha)s WHERE id = %(id)s;"
        resultado = connectToMySQL( "users_CRUD" ).query_db( query, usuarioAEditar )
        return resultado