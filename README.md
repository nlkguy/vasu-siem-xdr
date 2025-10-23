# vasu-siem-xdr
Vasu :- A lightweight, open-source SIEM &amp; XDR system inspired by Wazuh.
-----------------

![Logo - Smiling](/docs/images/vasu_smile.png)

- the core MVP concept will be a small demo-able e2e system.
- the agent collects system metrics and logs 
- the server ingests and stores data , communicates with database .etc
- a simple rule engine for easy spec.
- a basic web dashboard tied to server that shows metrics,summaries .etc
- vasu-ettan ee code nte aiswaryam.


### Agent

Core MVP Agent Features include :-

    - Resource monitoring : CPU,Memmory,Disk,Uptime.etc
    - Log collection, tailing : auth logs , event logs , journalctl .etc
    - Auth/Access Event monitoring : sudo attempts, remote auth, FP.
    - Process,Service inventory : top,htop on steroids.
    - File Integrity check : checkcheckchecksum.
    - Periodic Heartbeat : telemetry and stuff.
    - Offline buffer : store timestamped data while offline.
    - Agent Auth : use auth tokens for communication to server.

### Server

MVP Server Features include :-

    - Ingestion endpoint : HTTP API endpoint.
    - Agent Auth : auth using api key or JWT.
    - Storage : DB for time series data / .
    - Rule engine : yaml/json rule loading.
    - Alerts : alerts based on rules.
    - Web dashboard : list agents,alerts,events,metrics,serach/filter.
    - WebSocket integration : push alerts.
    - Retention policy : retain logs and data.



```



░░░░░░░░░░░░░░░░░░░░▒▒▒▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░▒▓▓▓▓▒▒▒▒▒▒▒▒▒▒░▒▒▒▒░▒░▒▒▒░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░▒███▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░▒▒░░░░░░░░░░░░░
░░░░░░░░░░░░▓██▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░▒▒░░░░░░░░░░
░░░░░░░░░░▒██▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒░▒░░░░░░░░░
░░░░░░░░░▓██▓▓▓▓▓▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒░▒░░░░░░░
░░░░░░░▒▓████▓▓▓▓▒▓▓▓▓▓▓▓▓▓▓▓██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒░▒░░░░░░
░░░░░░▒▓▓▓▓▓▓▓▓▓▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒░░░░░░░
░░░░░▒▓▒▓▓▓▓▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓█▓▓▓▓▓▓▓████▓▓▓▓▓▓▓▓▓▒▒░░░░░░
░░░░░▒▒▒▓▓▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒░░░░░░
▒░░░░▒▒▒▓▓▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒░░░░░
▓▓░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓███▓████▓▓▓▓▓▒▒▒░░░░░
▓▓▓░▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓█▓▓▓▓▓▓▓▓▓▓▓▓████████▓▓▓▓▓▓▓▓▒▒▒░░░░
▓▓▓▒▒▒▒▒▒▒▒▓▓▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒░░░░
▓▒▓▒▒▒▒▒▒▒▒▒░░░░░▒▒▒▒▒▒▒▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▒▒▒░░░░
▓▒▓▓▒▒▒▒▒▒▒░▒▒▒▒▓▓▓▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▓▓▓▓▓▒▒▒░░░░
██▓▓▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▒▓▒▒▒▒█▓▓▓▓▒▒▒▒▓▓▓▒▓▓▓▒▒▓▓▓▓▓▒▒▒░░░░
██▓▓▒▒▒▒▒▒▒▒▒▒░▒░█▒█▓▒▒▒▒▒▓▓▓▓▓▒▒▒▓░▓░▒░▒▒▒▓▓▓▓▓▓▓▒▒░░░░░
██▓▒▒▒▒▒▒▒▒▒▒▒▒░▒▓▓▓▓▒▒▒▒▒▓▓▓▓▓▓▒▒▒▓▓▓▓█▒▓▓▓▓▓▓▓▓▓▒▒▒▓▓▒░
▓█▒▒▒░▒▒▒▒▒▒▒▒▒▒▒▓▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▓▓▓▒▒░
▓▓░▒▒▒▒▒▒▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓█▓▓▓▒▒▒▓▓▓▓▓▓▓▓▓▓▓▒█▓▓▒░░
▓▓▒░▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▒▒░▒▒▒▓██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▓▓▒░▒░
▓▓▒▒░▒▒▒▒▒▒▒▓▓▓▓▓▓▓▒▒▒▒▒▓▓██▓▓██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓▓▒▒░░
▓▓▒▒░▒▒▒▒▒▒▒▓▓▓▓▓▒▒▒▒▒░▒▒▓▓▓▓▒░▒▓▓▓▒▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒░░░
▓▒░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░▒▒▓▓▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒░░░
▓░░░▓▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░▒░▒▒▓▓▓▓▓▓▓▒▒▓▒░░░░░
▒░░░▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒█▓▒░░░░
▒░░░░▒▒▒▒▒░░░░░░░░░░▒▒▒▒▒▒▓▓▓▒▒▒▒░░░░░░░░░░▒▒▒▓▒▒▒▒░░░░░░
▒░░░░░▒▒▒▒▒▒▒░░░▒▒░░░░░░░░░░░░░ ░░░░░░░░░░░▒▒▒▒▒▒░░░░░░░░
▒░░░░▒▒▒░▒▒▒▒▒▒▒▒▒░░▒▒▒░░░░▒▒▓▓▓▓▒▓▓▒▒▒▒▒▒▒▒▒▒▒▒░░▒░░░░░░
▓░░░▓░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▓▓▒▒▒▒▒▒▒▒░░░░▒░░░░
▓▒▒▒░░░░▒▒░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▒▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒░░░░░░▒▒░░
▓▓▒░░░░░░░░▒░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▓▒▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░▒░
▓▒░░░░░░░▒░░░░░░▒▒▒▒▒▒▒▒▒▓▒▓▓▓▓▓▒▓▒▒▒▒▒▒▒▒▒▒▒▒▒░ ░░░▓░▒▒▓
▒░░░░░░░░░░░░░░░░▒░▒▒▒▒▒▒▒▒▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░ ░░░░░░░▒
▒░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░▒▒▒▒░ ░░░░░░░░
▒░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░ ░░░░░░░
░░░░░░░░░ ░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░  ░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░ ░░░░░░
▒░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░▒



VASU-ETTAN EEE CODE-NTE AISWARYAM                                 


```