Stormbot role plugin
====================

This is a Stormbot_ plugin that let user volunteer for some roles. And then
assign those role randomly for a given duration::

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

.. _Stormbot: https://pypi.org/project/stormbot

Example
=======

::

    stormbot --plugins stormbot_role.role --role Grand-Pedestre --role-start 2017-05-29T00 --role-duration P1W

License
=======

::

    Permission to use, copy, modify, and distribute this software for any
    purpose with or without fee is hereby granted, provided that the above
    copyright notice and this permission notice appear in all copies.

    THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
    WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
    MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
    ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
    WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
    ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
    OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.