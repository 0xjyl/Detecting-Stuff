# Domain Activity Search 

```yaml 
(index=LIST YOUR INDEX sourcetype=opendns:dnslogs OR sourcetype=opendns:proxylogs) OR (index=LIST YOUR INDEX sourcetype=zscaler* ) OR (index=LIST YOUR INDEX) AND "* LIST SUSPICIOUS URL HERE *" | table url urlcategory ClientIP devicehostname deviceowner index

```

```yaml
search(index=LIST YOUR INDEX sourcetype=opendns:dnslogs OR sourcetype=opendns:proxylogs) OR (index=LIST YOUR INDEX sourcetype=zscaler* ) OR (index=LIST YOUR INDEX) url="* TEXT(input.domain) " earliest=-24h@h latest=@m | head 200 | rex field=url "^(?[^\/:?]+)" | search domain=" TEXT(input.domain) *" | table url status user deviceowner devicehostname datetime action
```