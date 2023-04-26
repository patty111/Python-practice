import json
from azure.ai.formrecognizer import FormTrainingClient
from azure.ai.formrecognizer import FormRecognizerClient
from azure.core.credentials import AzureKeyCredential
from azure.ai.formrecognizer import DocumentAnalysisClient



credentials = json.load(open("api.json"))
ENDPOINT = credentials['ENDPOINT']
API_KEY = credentials['API_KEY']

url = "https://getjobber.com/wp-content/uploads/2022/01/invoice-template-example.png"


form_recognizer_client = FormRecognizerClient(ENDPOINT, AzureKeyCredential(API_KEY))
poller = form_recognizer_client.begin_recognize_invoices_from_url(url)
result = poller.result()

# turn data to dictionary type
rd = result[0].to_dict()['fields']  # result_dict


# extracting data
customer_address = rd['CustomerAddress']['value']
customer_name = rd['CustomerAddressRecipient']['value']
total_cost = rd['InvoiceTotal']['value']
due_date = rd['InvoiceDate']['value']
invoiceID = rd['InvoiceId']['value']


products_list = rd['Items']['value']
products_description = []
quantity = []
price = []


for i in products_list:
    price.append(i['value']['Amount']['value_data']['text'])
    products_description.append(i['value']['Description']['value'])
    quantity.append((i['value']['Quantity']['value']))


print('---------------------------------------------------------------------------------------')
print('ID:  ', invoiceID, '                                               Total Cost:  ', str(total_cost) + '$')
print('Name:  ', customer_name, '                                         Due Date:  ', due_date, end='\n')
print('Address:  ', customer_address, end='\n')
print('---------------------------------------------------------------------------------------')


for i in range(len(products_description)):
    print(products_description[i].ljust(15),end='')
    print("         " + str(quantity[i]).ljust(15) + str(price[i]))



with open('out.json', 'w', encoding='utf-8') as f:
    f.write(json.dumps(result[0].to_dict(), indent=2, default=str))    # default = str to deal with dates

