import requests



# @api_view('POST')
def pincode():
    #pincode = request.data.get('pincode')
    pincode = 34151245
    res = requests.get(f'https://api.postalpincode.in/pincode/{pincode}')
    print(res)
    json_res = res.json()
    print(json_res)
    district = json_res[0]['PostOffice'][0]['District']
    print(district)
    state = json_res[0]['PostOffice'][0]['State']
    print(state)

pincode()