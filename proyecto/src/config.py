class Config:
    SECRET_KEY = 'B!1w8NAt1T^%kvhUI*S^'




class DevelopmentCOnfig(Config):
    DEBUG=True
    MYSQL_HOST='localhost'
    MYSQL_USER='josev646'
    MYSQL_PASSWORD='josev646'
    MYSQL_BD ='loggin'

config = {
    'development' : DevelopmentCOnfig
    
}