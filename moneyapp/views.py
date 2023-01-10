from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .forms import InvestmentForm


class Index(View):

    def get(self, request):
        form = InvestmentForm()
        return render(request, 'index.html', {'form': form})

    def post(self, request):
        form = InvestmentForm(request.POST)
        if form.is_valid():
            total_result = form.cleaned_data['starting_amount']
            total_interest = 0
            yearly_results = {}

            for i in range(1, int(form.cleaned_data['number_of_years']+1)):
                yearly_results[i] = {}

                # calculating interesrt
                interest = total_result*(form.cleaned_data['return_rate']/100)
                total_result += interest
                total_interest += interest

                # adding the annual increment amount
                total_result += form.cleaned_data['annual_increment_amount']

                # populating the yearly results dictionary
                yearly_results[i]['interest'] = round(total_interest, 2)
                yearly_results[i]['amount'] = round(total_result, 2)

                # craeting context
                context = {
                    'total_result': round(total_result, 2),
                    'yearly_results': yearly_results,
                    'number_of_years': int(form.cleaned_data['number_of_years'])
                }

            return render(request, 'result.html', context)
