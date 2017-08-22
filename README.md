Stormbot role plugin
====================

Let user volunteer for some roles. And then assign those role randomly for a
given duration.

```
<master>   | stormbot: whois Grand-Pedestre
<stormbot> | nobody is willing to be Grand-Pedestre

<master>   | stormbot: whocouldbe Grand-Pedestre
<stormbot> | nobody is volunteer to be Grand-Pedestre

<master>   | stormbot: icouldbe Grand-Pedestre
<stormbot> | master: glad to here that
<stormbot> | master is volunteer for Grand-Pedestre

<master>   | stormbot: iam Grand-Pedestre
<stormbot> | master: thanks !
<stormbot> | master is Grand-Pedestre for 5 days, 13:32:48.239574

<master>   | stormbot: icantbe Grand-Pedestre
<stormbot> | master: sad news…
<stormbot> | nobody is volunteer to be Grand-Pedestre
```

Example
-------

```
stormbot --plugins stormbot_role.role --role Grand-Pedestre --role-start 2017-05-29T00 --role-duration P1W
```
