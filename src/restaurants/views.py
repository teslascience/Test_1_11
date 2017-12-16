import random
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# function based view
def home_old(request):
    html_var = 'f strings'
    num = random.randint(0, 100000000)
    html_ = f"""<!DOCTYPE html>
    <html lang=en>

    <head>
    </head>
    <body>
      <h1>Hello World!</h1>
      <p>This is {html_var} coming through</p>
      <p>This is a random number: {num}</p>
    </body>
    </html>
    """
    return HttpResponse(html_)

def home(request):
    num = None
    some_list = [
    random.randint(0, 100000000),
    random.randint(0, 100000000),
    random.randint(0, 100000000)
    ]
    condition_bool_item = False
    if condition_bool_item:
        num = random.randint(0, 100000000)
    context = {
    "num": num,
    "some_list": some_list}
    return render(request, "base.html", context)
