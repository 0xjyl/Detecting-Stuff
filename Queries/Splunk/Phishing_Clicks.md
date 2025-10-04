# Who clicked on a potential phishing link 

```yaml 
(index=LIST YOUR INDEX sourcetype=opendns:dnslogs OR sourcetype=opendns:proxylogs) OR (index=LIST YOUR INDEX sourcetype=zscaler* ) OR (index=LIST YOUR INDEX) AND url=SUSPICIOUS URL | eval src_user=coalesce(user,identities) | table _time src_user src action sourcetype category query record_type reply_code url http_referrer dest_ip ClientIP clientpublicIP category appclass appname contenttype department devicehostname deviceowner http_method http_referrer http_user_agent | sort _time

