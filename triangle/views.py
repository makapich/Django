from django.shortcuts import render

from .forms import TriangleForm


def triangle(request):
    hypotenuse = None
    if "Submit" in request.GET:
        user_form = TriangleForm(request.GET)

        if user_form.is_valid():
            leg1 = user_form.cleaned_data['leg1']
            leg2 = user_form.cleaned_data['leg2']
            hypotenuse = round((((leg1 ** 2) + (leg2 ** 2)) ** 0.5), 2)

            user_form = TriangleForm()
    else:
        user_form = TriangleForm()

    return render(request, 'triangle/triangle.html', {'form': user_form, 'hypotenuse': hypotenuse})