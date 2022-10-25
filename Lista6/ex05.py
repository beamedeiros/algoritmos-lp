# E. papagaio
# temos um papagaio que fala alto
# hora é um parâmetro entre 0 e 23
# temos problemas se o papagaio estiver falando
# antes da 7 ou depois das 20
def papagaio(falando, hora):
  return falando and (7 > hora > 20)