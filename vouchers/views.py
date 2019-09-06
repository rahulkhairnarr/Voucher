from .forms import VoucherForm
from django.shortcuts import render
from .models import Voucher


# Create your views here.
def home_view(request, *args, **kwargs):
    discount_field = VoucherForm()
    data_parse = {
        'discount_field': discount_field,
        'alert_window': 'false',
        'discount_percent': 0,
        'used': 0,
        'code_exist': 'true',
        'max_used': 'false'
    }
    if request.method == 'POST':
        enter_code = request.POST['discount_code']
        check_code = Voucher.objects.filter(discount_code=enter_code).count()
        if check_code > 0:
            query_data = Voucher.objects.get(discount_code=enter_code)
            query_data.used += 1
            print(query_data.used)
            if query_data.used <= query_data.max_use :
                data_parse['alert_window'] = 'true'
                data_parse['discount_percent'] = query_data.discount_percent
                data_parse['used'] = query_data.used
                query_data.save(update_fields=['used'])
            else:
                data_parse['max_used'] = 'true'
        else:
            data_parse['code_exist'] = 'false'
        return render(request, 'index.html', data_parse)
    elif request.method == 'GET':
        return render(request, 'index.html', data_parse)