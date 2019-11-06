# Query to return all sellers from Egypt
def test(request):
    sellers_in_egypt = Seller.objects.filter(country_name='Egypt')
    return render(request, 'test.html', {'sellers_in_egypt': sellers_in_egypt})