from comunidade.models import Usuario, Post
from comunidade import app, database
#
# with app.app_context():
#     database.drop_all()
#     database.create_all()

# with app.app_context():
#     Usuario.query.all()
#     meus_usuarios=Usuario.query.first()
#     print(meus_usuarios)

#   usuario = Usuario(username='AA', email='asdsd@gmail.com', senha='123456')
 #   usuario2 = Usuario(username='AB', email='asbdd@gmail.com', senha='123456')

  #  database.session.add(usuario)
  #  database.session.add(usuario2)
  #  database.session.commit()

# with app.app_context():
#     meus_usuarios = Usuario.query.all()
#     print(meus_usuarios)
#     primeiro_usuario = Usuario.query.first()
#     print(primeiro_usuario.id)
#     print(meus_usuarios[1].id)
#     usuario_teste=Usuario.query.filter_by(id=2).all()
#     print(usuario_teste)
# with app.app_context():
#     meu_post = Post(id_usuario=1, titulo='A degeneração', corpo='weeee')
#     database.session.add(meu_post)
#     database.session.commit()
# with app.app_context():
#     post = Post.query.first()
#     print(post.titulo)
#     print(post.autor.email)
#with app.app_context():
#     database.drop_all()
#    database.create_all()