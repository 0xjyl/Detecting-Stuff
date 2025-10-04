# DNS Record Length 
```yaml 
index=* sourcetype=opendns:dnslogs | eval query_length=len(query) | where query_length > 249 | table _time, host, src_ip, query, dest_ip, query_length | sort - query_length
