from django.shortcuts import render

def welcome(request):
    return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):

    context = { 
    	'my_list' : [
    		{
    			'restaurant_name' : 'mcdonalds',
    			'food_type' : 'fast food'
    		},
    		{
    			'restaurant_name' : 'wasabi',
    			'food_type' : 'sushi'
    		},
    		{
    			'restaurant_name' : 'ubon',
    			'food_type' : 'thai'
    		}

    	]

    }
    return render(request, 'list.html', context)


def restaurant_detail(request):

    context = {
    	'my_object': {
    		'restaurant_name' : 'ubon',
    		'food_type' : 'thai'
    	}
    }
    return render(request, 'detail.html', context)
