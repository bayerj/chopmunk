Chopmunk
========


Chopmunk is a minimalist logging approach. The idea is to use coroutines as
adivsed in Dave Beazley's tutorial:

    http://www.dabeaz.com/coroutines/


Evaluating JSON logs with underscore-cli
----------------------------------------

Since a json file sink preceded by a jsonifier sink leads to one JSON document
per line, it cannot be processed with tools like underscore-cli directly. This
bash command helps:

    cat <yourlog> | while read line; do echo $line | underscore pretty; done

This will pretty print each document after the other.


