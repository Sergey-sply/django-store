from django.db.models import Q

from products.models import Products

def q_search(query):

    # search bt id
    if query.isdigit() and len(query) <= 5:
        return Products.objects.filter(id=int(query))
    
    keywords = [word for word in query.split() if len(word) > 2]

    q_objects = Q()

    for token in keywords:
        q_objects |= Q(description__icontains=token)
        q_objects |= Q(name_icontains=token)
    
    return Products.objects.filter(q_objects)