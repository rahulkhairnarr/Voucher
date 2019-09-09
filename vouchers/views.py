from .forms import VoucherForm
from django.shortcuts import render
from .models import Voucher


def home_view(request):
    # created new instance of voucher form class
    voucher_form = VoucherForm()

    # create a dictionary to parse data to HTML page
    data_parse = {
        'voucher_form': voucher_form,  # passing form instance to display on view
        'alert_window': 'false',  # this key use to display alert modal or not, default it is false
        'discount_value': 0,  # passing amount of discount offer on code
        'used': 0,  # number of times voucher code is used
        'code_exist': 'true',  # enter code is exist or not
        'max_used': 'false',  # enter code is use maximum times
        'discount_type': 'amount'  # type of discount voucher code is offering
    }

    # When user request page for first time, get request will delivery data
    if request.method == 'GET':
        return render(request, 'index.html', data_parse)

    # When user enter voucher code and click button to apply,
    # post method received data and give response accordingly
    elif request.method == 'POST':
        # Getting Enter code from user
        enter_code = request.POST['discount_code']

        # Checking code exist in database or not
        check_code = Voucher.objects.filter(discount_code=enter_code).count()

        # If Code exist in database first condition will trigger
        if check_code > 0:
            # Query enterd code into database
            query_data = Voucher.objects.get(discount_code=enter_code)

            # Increasing voucher used code by 1
            query_data.voucher_used += 1

            # if voucher used code is less then maximum used limit, following condition will trigger
            if query_data.voucher_used <= query_data.max_voucher_use:

                # Since voucher code is not exceed limit of maximum use setting parameter to inform user
                data_parse['alert_window'] = 'true'

                # Getting Discount value from code
                data_parse['discount_value'] = query_data.discount_value

                # Passing type of discount to inform accordingly
                data_parse['discount_type'] = query_data.discount_value_type

                # Updating voucher used value for updating in database
                data_parse['voucher_used'] = query_data.voucher_used

                # Save updated field in database
                query_data.save(update_fields=['voucher_used'])

            # if voucher used code is reached to maximum used limit, following condition will trigger
            else:
                data_parse['max_used'] = 'true'

        # If code doesn't exist in database else condition will trigger
        else:
            # setting code not exist set to false
            data_parse['code_exist'] = 'false'
        return render(request, 'index.html', data_parse)
