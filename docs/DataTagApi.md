# intrinio_sdk.DataTagApi

All URIs are relative to *https://api-v2.intrinio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_data_tags**](DataTagApi.md#get_all_data_tags) | **GET** /data_tags | All Data Tags
[**get_data_tag_by_id**](DataTagApi.md#get_data_tag_by_id) | **GET** /data_tags/{identifier} | Lookup Data Tag
[**search_data_tags**](DataTagApi.md#search_data_tags) | **GET** /data_tags/search | Search Data Tags



[//]: # (START_OPERATION)

[//]: # (OPERATION:get_all_data_tags_v2)

[//]: # (ENDPOINT:/data_tags)

[//]: # (DOCUMENT_LINK:DataTagApi.md#get_all_data_tags)

## **get_all_data_tags**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/api_v2/get_all_data_tags_v2)

> ApiResponseDataTags get_all_data_tags(tag=tag, type=type, parent=parent, statement_code=statement_code, fs_template=fs_template, page_size=page_size, next_page=next_page)

#### All Data Tags


Returns all Data Tags. Returns Data Tags matching parameters when specified.

### Example
[//]: # (START_CODE_EXAMPLE)

```python
from __future__ import print_function
import time
import intrinio_sdk
from intrinio_sdk.rest import ApiException
from pprint import pprint

intrinio_sdk.ApiClient().configuration.api_key['api_key'] = 'YOUR_API_KEY'

data_tag_api = intrinio_sdk.DataTagApi()

tag = '' # str | Tag (optional)
type = '' # str | Type (optional)
parent = '' # str | ID of tag parent (optional)
statement_code = 'income_statement' # str | Statement Code (optional)
fs_template = 'industrial' # str | Template (optional) (default to industrial)
page_size = 100 # int | The number of results to return (optional) (default to 100)
next_page = '' # str | Gets the next page of data from a previous API call (optional)

try:
    api_response = data_tag_api.get_all_data_tags(tag=tag, type=type, parent=parent, statement_code=statement_code, fs_template=fs_template, page_size=page_size, next_page=next_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataTagApi->get_all_data_tags: %s\n" % e)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(api_response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag** | **str**| Tag | [optional] 
 **type** | **str**| Type | [optional] 
 **parent** | **str**| ID of tag parent | [optional] 
 **statement_code** | **str**| Statement Code | [optional] 
 **fs_template** | **str**| Template | [optional] [default to industrial]
 **page_size** | **int**| The number of results to return | [optional] [default to 100]
 **next_page** | **str**| Gets the next page of data from a previous API call | [optional] 
<br/>
### Return type

[**ApiResponseDataTags**](ApiResponseDataTags.md)

[//]: # (END_OPERATION)


[//]: # (START_OPERATION)

[//]: # (OPERATION:get_data_tag_by_id_v2)

[//]: # (ENDPOINT:/data_tags/{identifier})

[//]: # (DOCUMENT_LINK:DataTagApi.md#get_data_tag_by_id)

## **get_data_tag_by_id**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/api_v2/get_data_tag_by_id_v2)

> DataTag get_data_tag_by_id(identifier)

#### Lookup Data Tag


Returns the Data Tag with the given `identifier`

### Example
[//]: # (START_CODE_EXAMPLE)

```python
from __future__ import print_function
import time
import intrinio_sdk
from intrinio_sdk.rest import ApiException
from pprint import pprint

intrinio_sdk.ApiClient().configuration.api_key['api_key'] = 'YOUR_API_KEY'

data_tag_api = intrinio_sdk.DataTagApi()

identifier = 'marketcap' # str | The Intrinio ID or the code-name of the Data Tag

try:
    api_response = data_tag_api.get_data_tag_by_id(identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataTagApi->get_data_tag_by_id: %s\n" % e)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(api_response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| The Intrinio ID or the code-name of the Data Tag | 
<br/>
### Return type

[**DataTag**](DataTag.md)

[//]: # (END_OPERATION)


[//]: # (START_OPERATION)

[//]: # (OPERATION:search_data_tags_v2)

[//]: # (ENDPOINT:/data_tags/search)

[//]: # (DOCUMENT_LINK:DataTagApi.md#search_data_tags)

## **search_data_tags**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/api_v2/search_data_tags_v2)

> ApiResponseDataTagsSearch search_data_tags(query, page_size=page_size)

#### Search Data Tags


Searches for Data Tags matching the text `query`

### Example
[//]: # (START_CODE_EXAMPLE)

```python
from __future__ import print_function
import time
import intrinio_sdk
from intrinio_sdk.rest import ApiException
from pprint import pprint

intrinio_sdk.ApiClient().configuration.api_key['api_key'] = 'YOUR_API_KEY'

data_tag_api = intrinio_sdk.DataTagApi()

query = 'revenue' # str | 
page_size = 100 # int | The number of results to return (optional) (default to 100)

try:
    api_response = data_tag_api.search_data_tags(query, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataTagApi->search_data_tags: %s\n" % e)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(api_response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**|  | 
 **page_size** | **int**| The number of results to return | [optional] [default to 100]
<br/>
### Return type

[**ApiResponseDataTagsSearch**](ApiResponseDataTagsSearch.md)

[//]: # (END_OPERATION)

