from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from comunidade.models import Usuario
from flask_login import current_user

class FormCriarConta(FlaskForm):
    username = StringField('Nome de Usuário', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email(message="Endereço de e-mail inválido.")])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(6, 20, message="Senha inválida. Deve conter entre 6 e 20 caracteres.")])
    confirmacao = PasswordField('Confirmação da senha', validators=[DataRequired(), EqualTo('senha', message="Senhas não coincidem.")])
    botao_submit_create = SubmitField('Criar Conta')

    def validate_email(self, email):
        usuario = Usuario.query.filter_by(email=email.data).first()
        if usuario:
            raise ValidationError('Email já cadastrado.')

class FormLogin(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired(), Email(message="Endereço de e-mail inválido.")])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(6, 20, message="Senha inválida. Deve conter entre 6 e 20 caracteres.")])
    botao_submit_login = SubmitField('Realizar Login')
    botao_lembrar_dados = BooleanField('Lembrar meu acesso')

class FormEditarPerfil(FlaskForm):
    username = StringField('Nome de Usuário', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email(message="Endereço de e-mail inválido.")])
    foto_perfil = FileField('Atualizar Foto de Perfil', validators=[FileAllowed(['jpg', 'png'])])

    curso_excel = BooleanField('Excel')
    curso_vba = BooleanField('VBA')
    curso_powerbi = BooleanField('Power BI')
    curso_python = BooleanField('Python')
    curso_ppt = BooleanField('Power Point')
    curso_sql = BooleanField('SQL')

    botao_submit_editarperfil = SubmitField('Salvar Alterações')

    def validate_email(self, email):
        if current_user.email != email.data:
            usuario = Usuario.query.filter_by(email=email.data).first()
            if usuario:
                raise ValidationError('Email já cadastrado.')


class FormCriarPost(FlaskForm):
    titulo = StringField('Titulo', validators=[DataRequired(), Length(2, 140)])
    corpo = TextAreaField('Escreva seu post', validators=[DataRequired()])
    botao_submit = SubmitField('Criar Post')