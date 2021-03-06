# intrinio_sdk.FilingApi

All URIs are relative to *https://api-v2.intrinio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_filings**](FilingApi.md#get_all_filings) | **GET** /filings | All Filings
[**get_all_notes**](FilingApi.md#get_all_notes) | **GET** /filings/notes | All Filing Notes
[**get_filing_by_id**](FilingApi.md#get_filing_by_id) | **GET** /filings/{id} | Lookup Filing
[**get_note**](FilingApi.md#get_note) | **GET** /filings/notes/{identifier} | Filing Note by ID
[**get_note_html**](FilingApi.md#get_note_html) | **GET** /filings/notes/{identifier}/html | Filing Note HTML
[**get_note_text**](FilingApi.md#get_note_text) | **GET** /filings/notes/{identifier}/text | Filing Note Text
[**search_notes**](FilingApi.md#search_notes) | **GET** /filings/notes/search | Search Filing Notes



[//]: # (START_OPERATION)

[//]: # (OPERATION:get_all_filings_v2)

[//]: # (ENDPOINT:/filings)

[//]: # (DOCUMENT_LINK:FilingApi.md#get_all_filings)

## **get_all_filings**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/api_v2/get_all_filings_v2)

> ApiResponseFilings get_all_filings(company, report_type=report_type, start_date=start_date, end_date=end_date, page_size=page_size, next_page=next_page)

#### All Filings


Returns all Filings. Returns Filings matching parameters when supplied.

### Example
[//]: # (START_CODE_EXAMPLE)

```python
from __future__ import print_function
import time
import intrinio_sdk
from intrinio_sdk.rest import ApiException
from pprint import pprint

intrinio_sdk.ApiClient().configuration.api_key['api_key'] = 'YOUR_API_KEY'

filing_api = intrinio_sdk.FilingApi()

company = 'AAPL' # str | Filings for the given `company` identifier (ticker, CIK, LEI, Intrinio ID)
report_type = '' # str | Filter by report type (optional)
start_date = '2015-01-01' # date | Filed on or after the given date (optional)
end_date = '' # date | Filed before or after the given date (optional)
page_size = 100 # int | The number of results to return (optional) (default to 100)
next_page = '' # str | Gets the next page of data from a previous API call (optional)

try:
    api_response = filing_api.get_all_filings(company, report_type=report_type, start_date=start_date, end_date=end_date, page_size=page_size, next_page=next_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FilingApi->get_all_filings: %s\n" % e)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(api_response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company** | **str**| Filings for the given &#x60;company&#x60; identifier (ticker, CIK, LEI, Intrinio ID) | 
 **report_type** | **str**| Filter by report type | [optional] 
 **start_date** | **date**| Filed on or after the given date | [optional] 
 **end_date** | **date**| Filed before or after the given date | [optional] 
 **page_size** | **int**| The number of results to return | [optional] [default to 100]
 **next_page** | **str**| Gets the next page of data from a previous API call | [optional] 
<br/>
### Return type

[**ApiResponseFilings**](ApiResponseFilings.md)

[//]: # (END_OPERATION)


[//]: # (START_OPERATION)

[//]: # (OPERATION:get_all_notes_v2)

[//]: # (ENDPOINT:/filings/notes)

[//]: # (DOCUMENT_LINK:FilingApi.md#get_all_notes)

## **get_all_notes**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/api_v2/get_all_notes_v2)

> ApiResponseFilingNotes get_all_notes(company=company, report_type=report_type, filing_start_date=filing_start_date, filing_end_date=filing_end_date, period_ended_start_date=period_ended_start_date, period_ended_end_date=period_ended_end_date, page_size=page_size, next_page=next_page)

#### All Filing Notes


Return all Notes from all Filings, most-recent first. Returns notes matching parameters when supplied.

### Example
[//]: # (START_CODE_EXAMPLE)

```python
from __future__ import print_function
import time
import intrinio_sdk
from intrinio_sdk.rest import ApiException
from pprint import pprint

intrinio_sdk.ApiClient().configuration.api_key['api_key'] = 'YOUR_API_KEY'

filing_api = intrinio_sdk.FilingApi()

company = 'AAPL' # str | A Company identifier (Ticker, CIK, LEI, Intrinio ID) (optional)
report_type = '10-Q' # str | Notes contained in filings that match the given report type (optional)
filing_start_date = '2018-07-15' # date | Limit search to filings on or after this date (optional)
filing_end_date = '2018-11-15' # date | Limit search to filings on or before this date (optional)
period_ended_start_date = '2018-07-15' # date | Limit search to filings with a period end date on or after this date (optional)
period_ended_end_date = '2018-11-15' # date | Limit search to filings with a period end date on or before this date (optional)
page_size = 100 # int | The number of results to return (optional) (default to 100)
next_page = '' # str | Gets the next page of data from a previous API call (optional)

try:
    api_response = filing_api.get_all_notes(company=company, report_type=report_type, filing_start_date=filing_start_date, filing_end_date=filing_end_date, period_ended_start_date=period_ended_start_date, period_ended_end_date=period_ended_end_date, page_size=page_size, next_page=next_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FilingApi->get_all_notes: %s\n" % e)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(api_response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company** | **str**| A Company identifier (Ticker, CIK, LEI, Intrinio ID) | [optional] 
 **report_type** | **str**| Notes contained in filings that match the given report type | [optional] 
 **filing_start_date** | **date**| Limit search to filings on or after this date | [optional] 
 **filing_end_date** | **date**| Limit search to filings on or before this date | [optional] 
 **period_ended_start_date** | **date**| Limit search to filings with a period end date on or after this date | [optional] 
 **period_ended_end_date** | **date**| Limit search to filings with a period end date on or before this date | [optional] 
 **page_size** | **int**| The number of results to return | [optional] [default to 100]
 **next_page** | **str**| Gets the next page of data from a previous API call | [optional] 
<br/>
### Return type

[**ApiResponseFilingNotes**](ApiResponseFilingNotes.md)

[//]: # (END_OPERATION)


[//]: # (START_OPERATION)

[//]: # (OPERATION:get_filing_by_id_v2)

[//]: # (ENDPOINT:/filings/{id})

[//]: # (DOCUMENT_LINK:FilingApi.md#get_filing_by_id)

## **get_filing_by_id**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/api_v2/get_filing_by_id_v2)

> Filing get_filing_by_id(id)

#### Lookup Filing


Returns the Filing with the given `identifier`

### Example
[//]: # (START_CODE_EXAMPLE)

```python
from __future__ import print_function
import time
import intrinio_sdk
from intrinio_sdk.rest import ApiException
from pprint import pprint

intrinio_sdk.ApiClient().configuration.api_key['api_key'] = 'YOUR_API_KEY'

filing_api = intrinio_sdk.FilingApi()

id = 'fil_7Kn2P6' # str | The Intrinio ID of the Filing

try:
    api_response = filing_api.get_filing_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FilingApi->get_filing_by_id: %s\n" % e)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(api_response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The Intrinio ID of the Filing | 
<br/>
### Return type

[**Filing**](Filing.md)

[//]: # (END_OPERATION)


[//]: # (START_OPERATION)

[//]: # (OPERATION:get_note_v2)

[//]: # (ENDPOINT:/filings/notes/{identifier})

[//]: # (DOCUMENT_LINK:FilingApi.md#get_note)

## **get_note**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/api_v2/get_note_v2)

> FilingNote get_note(identifier, content_format=content_format)

#### Filing Note by ID



### Example
[//]: # (START_CODE_EXAMPLE)

```python
from __future__ import print_function
import time
import intrinio_sdk
from intrinio_sdk.rest import ApiException
from pprint import pprint

intrinio_sdk.ApiClient().configuration.api_key['api_key'] = 'YOUR_API_KEY'

filing_api = intrinio_sdk.FilingApi()

identifier = 'xbn_3fghz' # str | The Intrinio ID of the filing note
content_format = 'text' # str | Returns content in html (as filed) or plain text (optional) (default to text)

try:
    api_response = filing_api.get_note(identifier, content_format=content_format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FilingApi->get_note: %s\n" % e)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(api_response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| The Intrinio ID of the filing note | 
 **content_format** | **str**| Returns content in html (as filed) or plain text | [optional] [default to text]
<br/>
### Return type

[**FilingNote**](FilingNote.md)

[//]: # (END_OPERATION)


[//]: # (START_OPERATION)

[//]: # (OPERATION:get_note_html_v2)

[//]: # (ENDPOINT:/filings/notes/{identifier}/html)

[//]: # (DOCUMENT_LINK:FilingApi.md#get_note_html)

## **get_note_html**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/api_v2/get_note_html_v2)

> str get_note_html(identifier)

#### Filing Note HTML



### Example
[//]: # (START_CODE_EXAMPLE)

```python
from __future__ import print_function
import time
import intrinio_sdk
from intrinio_sdk.rest import ApiException
from pprint import pprint

intrinio_sdk.ApiClient().configuration.api_key['api_key'] = 'YOUR_API_KEY'

filing_api = intrinio_sdk.FilingApi()

identifier = 'xbn_3fghz' # str | The Intrinio ID of the filing note

try:
    api_response = filing_api.get_note_html(identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FilingApi->get_note_html: %s\n" % e)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(api_response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| The Intrinio ID of the filing note | 
<br/>
### Return type

**str**

[//]: # (END_OPERATION)


[//]: # (START_OPERATION)

[//]: # (OPERATION:get_note_text_v2)

[//]: # (ENDPOINT:/filings/notes/{identifier}/text)

[//]: # (DOCUMENT_LINK:FilingApi.md#get_note_text)

## **get_note_text**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/api_v2/get_note_text_v2)

> str get_note_text(identifier)

#### Filing Note Text



### Example
[//]: # (START_CODE_EXAMPLE)

```python
from __future__ import print_function
import time
import intrinio_sdk
from intrinio_sdk.rest import ApiException
from pprint import pprint

intrinio_sdk.ApiClient().configuration.api_key['api_key'] = 'YOUR_API_KEY'

filing_api = intrinio_sdk.FilingApi()

identifier = 'xbn_3fghz' # str | The Intrinio ID of the filing note

try:
    api_response = filing_api.get_note_text(identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FilingApi->get_note_text: %s\n" % e)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(api_response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| The Intrinio ID of the filing note | 
<br/>
### Return type

**str**

[//]: # (END_OPERATION)


[//]: # (START_OPERATION)

[//]: # (OPERATION:search_notes_v2)

[//]: # (ENDPOINT:/filings/notes/search)

[//]: # (DOCUMENT_LINK:FilingApi.md#search_notes)

## **search_notes**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/api_v2/search_notes_v2)

> ApiResponseFilingNotesSearch search_notes(query, filing_start_date=filing_start_date, filing_end_date=filing_end_date, page_size=page_size, page_size2=page_size2)

#### Search Filing Notes


Searches for Filing Notes using the `query`

### Example
[//]: # (START_CODE_EXAMPLE)

```python
from __future__ import print_function
import time
import intrinio_sdk
from intrinio_sdk.rest import ApiException
from pprint import pprint

intrinio_sdk.ApiClient().configuration.api_key['api_key'] = 'YOUR_API_KEY'

filing_api = intrinio_sdk.FilingApi()

query = 'inflation' # str | Search for notes that contain all or parts of this text
filing_start_date = '2018-07-15' # date | Limit search to filings on or after this date (optional)
filing_end_date = '2018-11-30' # date | Limit search to filings on or before this date (optional)
page_size = 100 # int | The number of results to return (optional) (default to 100)
page_size2 = 100 # int | The number of results to return (optional) (default to 100)

try:
    api_response = filing_api.search_notes(query, filing_start_date=filing_start_date, filing_end_date=filing_end_date, page_size=page_size, page_size2=page_size2)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FilingApi->search_notes: %s\n" % e)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(api_response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Search for notes that contain all or parts of this text | 
 **filing_start_date** | **date**| Limit search to filings on or after this date | [optional] 
 **filing_end_date** | **date**| Limit search to filings on or before this date | [optional] 
 **page_size** | **int**| The number of results to return | [optional] [default to 100]
 **page_size2** | **int**| The number of results to return | [optional] [default to 100]
<br/>
### Return type

[**ApiResponseFilingNotesSearch**](ApiResponseFilingNotesSearch.md)

[//]: # (END_OPERATION)

