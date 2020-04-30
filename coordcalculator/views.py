from django.shortcuts import render, redirect
from . forms import CoordForm

def index(request):
	form = CoordForm()
	return render(request, 'coordcalculator/form.html', { 'form':form })


def result(request):
	if request.method == 'POST':
		form = CoordForm(request.POST)
		
		if form.is_valid():
			x = int(form.cleaned_data['x'])
			y = int(form.cleaned_data['y'])

		coord_more = coord_finder_more(x, y)
		coord_less = coord_finder_less(x, y)
		coord_user = 'x{}, y{}'.format(x, y) 
		
		result = {'coord_more': coord_more, 
				  'coord_less': coord_less, 
				  'coord_user': coord_user}
	
	return render(request, 'coordcalculator/result.html', result)


def divisible_by_8(num):
	return num % 8 == 0


def make_divisible_more(num):
	while not divisible_by_8(num):
		num += 1 
	return num


def make_divisible_less(num):
	while not divisible_by_8(num):
		num -= 1 
	return num


def coord_finder_less(x, y):
	x = make_divisible_less(x)
	y = make_divisible_less(y)
	coord = 'x{}, y{}'.format(x, y) 
	
	return coord


def coord_finder_more(x, y):
	x = make_divisible_more(x)
	y = make_divisible_more(y)
	coord = 'x{}, y{}'.format(x, y) 

	return coord