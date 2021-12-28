import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br/')
except urllib.error.URLError:
    print('\033[31mNão foi possível acessar o site pudim.')
else:
    print('\033[32mSite acessado com sucesso!\033[m')
    # print(site.read()) // Ler o conteúdo HTML do site.
