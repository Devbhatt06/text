# this is a created file

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, "Home.html")

def analyse(request):
    # getting the text form the text area
    text = request.GET.get('text', "default")

    # check bok values
    charcount = request.GET.get('charcount' , " ")
    removespace = request.GET.get('removespace' , " ")
    capitalize = request.GET.get('capitalize' , " ")
    invert_text = request.GET.get('invert_text' , " ")


    # special var for each operations
    char_count_var = 0
    removespace_var = 0
    capitalize_var = 0
    invert_text_var = 0

    # logic for char count operation
    if (charcount == 'on'):
        frist1 = 'charcount'
        for i in text:
            char_count_var += 1
        special_var_charcount = str(char_count_var)
    else:
        frist1 = ""
        special_var_charcount = ""

    # logic for remove space operation
    if (removespace == 'on'):
        second2 = "removespace"
        removespace_var = text.replace(" " , "")
    else:
        second2 = ""
        removespace_var = ""

    # logic for capitalize operation
    if (capitalize == 'on'):
        third3 = "capitalize"
        capitalize_var = text.upper()
    else:
        third3 = ""
        capitalize_var = ""

    # logic for invert text operation
    if (invert_text == 'on'):
        forth = "invert text"
        invert_text_var = text[::-1]
    else:
        forth = ""
        invert_text_var = ""




    # creating dictionary to use vale in html file
    textul = {'text' : text , 'charcount' : frist1 , 'removespace' : second2 , 'capitalize' : third3 , "capitalize_var" : capitalize_var , 'special_var_charcount' : special_var_charcount , "removespace_var" : removespace_var , "inverted_text" : forth , "inverted_text_var" : invert_text_var}

    # connecting the html file with this fuction
    return render(request, "analyse.html" , textul)


def about(request):
    return render( request , "about.html") 


