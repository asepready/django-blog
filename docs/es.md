# Integrate Elasticsearch
If you already have the `Elasticsearch` environment, you can change the search from `Whoosh` to `Elasticsearch`, the integration method is also very simple,
First of all, you need to pay attention to the following points:
1. Your `Elasticsearch` supports `ik` Chinese word segmentation
2. Your `Elasticsearch` version>=7.3.0

Then make the following changes in `settings.py`:
-Add es link, as shown below:
```python
ELASTICSEARCH_DSL = {
     'default': {
         'hosts': '127.0.0.1:9200'
     },
}
```
-Modify `HAYSTACK` configuration:
```python
HAYSTACK_CONNECTIONS = {
     'default': {
         'ENGINE':'DjangoBlog.elasticsearch_backend.ElasticSearchEngine',
     },
}
```
Then the terminal executes:
```shell script
./manage.py build_index
```
This will create two indexes in your es, namely `blog` and `performance`, where the `blog` index is used for search, and `performance` will record the response time of each request for future Optimized use.
