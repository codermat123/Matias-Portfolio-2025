import requests

#User Prompts for conversion
def convert_curr():
    init_currency = input("Enter Base Currency: ")
    target_currency = input("Enter Quote Currency: ")

    while True:
        try:
            amount = float(input('Enter the amount: '))
        #Handle case if input not numeric
        except:
            print('The amount needs to be numeric')
            continue

        if not amount > 0:
            print('Amount needs to be greater than 0')
            continue
        else:
            break

    #URL for currency conv API
    url = f"https://api.apilayer.com/fixer/convert?to={target_currency}&from={init_currency}&amount={amount}"

    #Define empty payload (data) & Headers for HTTP req
    payload = {}
    headers= {
    "apikey": "n9uWQ2C3c5uli9NrpfZEGKwyXELIuZN9"
    }

    response = requests.request("GET", url, headers=headers, data = payload)
    status_code = response.status_code

    #check for error
    if status_code != 200:
        result = response.json()
        print('Error response: ' + str(result))
        quit()

    #GET request to API endpoint
    result = response.json()
    print('Conversion Result: ' + str(result['result']))

if __name__ == '__main__':
    convert_curr()